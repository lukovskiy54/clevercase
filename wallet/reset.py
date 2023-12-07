from django.utils import timezone
from datetime import timedelta
from wallet.models import Category



def reset_currently_spent():
    categories_to_reset = Category.objects.filter(
        date_of_rent__lt=timezone.now() - timedelta(days=30)
    )
    for category in categories_to_reset:
        category.currently_spent = 0
        category.due_date = category.due_date + timedelta(days=30)
        category.save()