from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class CustomerUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name='customuser_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_user_permissions', blank=True)

    class Meta:
        # Specify a unique related_name for groups and user_permissions
        # to avoid clashes with the default User model
        permissions = [
            ("view_customer", "Can view customer users"),
        ]

class PersonalDetail(models.Model):
    email = models.EmailField(unique=True)
    bank_name = models.CharField(max_length=200)
    bank_account = models.CharField(max_length=200)
    whatsapp_number = models.CharField(max_length=200)


class CardDetail(models.Model):
    amount = models.CharField('Amount', max_length=200)
    card_code = models.CharField('Card Code',max_length=200)
    image_1 = models.ImageField(null=True, blank=True, upload_to= 'images/')
    image_2 = models.ImageField(null=True, blank=True, upload_to='images/')