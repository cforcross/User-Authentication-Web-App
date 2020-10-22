from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserRegistrationModel


@receiver(post_save, sender=User)
def creater_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserRegistrationModel.objects.create(user=instance)
        profile.save()
