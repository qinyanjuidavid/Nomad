from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from modules.accounts.models import Administrator, Nomad, User


@receiver(post_save, sender=User)
def create_users(sender, instance, created, *args, **kwargs):
    if created:
        if (instance.role == "Administrator" or
                instance.is_admin or instance.is_staff):
            Administrator.objects.update_or_create(user=instance)
        elif (instance.role == "Nomad"):
            Nomad.objects.update_or_create(user=instance)
