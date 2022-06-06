from transactions.models import Transaction

def create_succeeded_transaction(sender, receiver, amount):
    Transaction.objects.create(sender=sender.user, receiver=receiver.user, amount=amount, status=2)

def create_failed_transaction(sender, receiver, amount):
    Transaction.objects.create(sender=sender.user, receiver=receiver.user, amount=amount, status=3)

