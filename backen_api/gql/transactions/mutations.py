from graphene import Boolean, ID, Mutation, Int

from users.models import Profile
from transactions.services import create_succeeded_transaction, create_failed_transaction
from testproj.w3 import check_balance, make_transaction



class TransactionMaker(Mutation):
    class Arguments:
        sender = ID(required=True)
        receiver = ID(required=True)
        amount = Int(required=True)
    
    ok = Boolean()
    
    @classmethod
    def mutate(cls, root, info, sender, receiver, amount):
        sender = Profile.objects.get(id=sender)
        receiver = Profile.objects.get(id=receiver)
        if check_balance(sender.wallet_address) >= amount:
            make_transaction(sender.wallet_address, receiver.wallet_address, amount, sender.private_key)
            create_succeeded_transaction(sender, receiver, amount)
            return TransactionMaker(ok=True)
        create_failed_transaction(sender, receiver, amount)
        return TransactionMaker(ok=False)
