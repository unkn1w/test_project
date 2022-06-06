from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Transaction(models.Model):
    PENDING = 1
    COMPLETED = 2
    ERROR = 3
    STATUS = (
        (PENDING, ('Transcation is on progress')),
        (COMPLETED, ('Transcation is completed successfully')),
        (ERROR, ('Transcation is failed')),
    )
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='receiver')
    status = models.PositiveSmallIntegerField(choices=STATUS, default=PENDING)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'From {self.sender} to {self.receiver}. Amount: {self.amount}'