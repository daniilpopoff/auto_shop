from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Customer

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created and instance.is_customer:
        Customer.objects.get_or_create(user=instance)