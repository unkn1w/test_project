from graphene import Float
from graphene_django import DjangoObjectType

from users.models import Profile
from testproj.w3 import check_balance


class ProfileType(DjangoObjectType):
    balance = Float()

    class Meta:
        model = Profile
        only_fields = (
            'id',
            'user',
            'wallet_address',
        )
        use_connection = True

    def resolve_balance(root, *args):
        return check_balance(root.wallet_address)
        