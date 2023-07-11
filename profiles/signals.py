from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(signal=post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a profile automatically after a new user is registered.

    Args:
        sender: The built-in User model in Django sends the signal.
        instance: The instance of the User model that was created.
        created (bool): Indicates if the User model instance was created.
        kwargs: Additional keyword arguments.
    """
    if created:
        Profile.objects.create(user=instance)
