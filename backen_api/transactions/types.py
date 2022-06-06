from graphene import String
from graphene_django import DjangoObjectType

from transactions.models import Transaction


class TransactionType(DjangoObjectType):
    sender = String()
    receiver = String()

    class Meta:
        model = Transaction
        only_fields = (
            'id',
            'amount',
            'status',
        )
        use_connection = True
    
    def resolve_sender(root, *args):
        return root.sender.username
    
    def resolve_receiver(root, *args):
        return root.receiver.username