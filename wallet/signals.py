from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Category, Notification

@receiver(post_save, sender=Category)
def create_or_update_notification(sender, instance, **kwargs):
    notification_85_exists = Notification.objects.filter(
        category=instance,
        message__contains="over 85%"
    ).exists()

    notification_100_exists = Notification.objects.filter(
        category=instance,
        message__contains="exceeded your limit"
    ).exists()

    if instance.currently_spent > 0.85 * instance.the_limit and not notification_85_exists:
        Notification.objects.create(
            user=instance.user,
            category=instance,
            message=f"You have spent {instance.currently_spent}{instance.currency}, which is over 85% of your limit in {instance.cat_name}."
        )

    if instance.currently_spent > instance.the_limit and not notification_100_exists:
        Notification.objects.create(
            user=instance.user,
            category=instance,
            message=f"You have exceeded your limit in {instance.cat_name}."
        )
