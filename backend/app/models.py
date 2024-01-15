from django.db import models

class User(models.Model):
    USER_TYPE_CHOICES = (
        ('individual', 'Individual'),
        ('business', 'Business'),
    )

    fullname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='individual')
    reason_to_join = models.TextField(null=True)
    card_number = models.CharField(max_length=9, unique=True)
    # date_created = models.DateField(auto_now_add = True)
    # expiry_date = models.DateField()
    points = models.IntegerField(default=0)
