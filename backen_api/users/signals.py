from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def user_post_save_or_update(sender, instance, created, *args, **kwargs):
    if created:
        instance.profile = Profile.objects.create(user=instance)
    instance.profile.save()
    
