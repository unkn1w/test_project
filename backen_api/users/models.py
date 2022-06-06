from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, 
                                related_name="profile",
                                verbose_name=("user"),
                                on_delete=models.CASCADE)
    wallet_address = models.CharField(max_length=42, help_text="Please provide correct eth address!" ,blank=True)
    private_key = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'User: {self.user}, Wallet: {self.wallet_address}'

