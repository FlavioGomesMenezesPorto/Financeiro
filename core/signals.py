from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Transaction

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Transaction)
def update_account_balance_on_creation(sender, instance, created, **kwargs):
    if created:
        account = instance.account
        if instance.transaction_type == 'IN':
            account.balance += instance.amount
        elif instance.transaction_type == 'OUT':
            account.balance -= instance.amount
        account.save()