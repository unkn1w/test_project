from graphene import Argument, Field, ID, ObjectType, Schema, String
from graphene_django import DjangoConnectionField

from users.models import Profile
from users.types import ProfileType
from transactions.models import Transaction
from transactions.types import TransactionType
from gql.transactions.mutations import TransactionMaker


class Query(ObjectType):
    profiles = DjangoConnectionField(ProfileType)
    profile = Field(ProfileType, id=Argument(ID, required=True))

    transactions = DjangoConnectionField(TransactionType)
    transaction = Field(TransactionType, id=Argument(ID, required=True))


    def resolve_profiles(root, info, **kwargs):
        return Profile.objects.all()

    def resolve_profile(root, info, **kwargs):
        return Profile.objects.get(id=kwargs.get('id'))

    def resolve_transactions(root, info, **kwargs):
        return Transaction.objects.all()
    
    def resolver_transaction(root, info, **kwargs):
        return Transaction.objects.get(id=kwargs.get('id'))


class Mutation(ObjectType):
    transaction_maker = TransactionMaker.Field()
    

schema = Schema(query=Query, mutation=Mutation)