# -*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save

from django.dispatch import receiver


class UserProfile(models.Model):
    USER_CHOICES = (
        ('EXAMINER', 'Examiner'),
        ('HEAD', 'Head'),
        ('EXTERNAL', 'External'),
        ('ADMIN', 'Admin')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, blank=True, default='')
    user_type = models.CharField(max_length=10, choices=USER_CHOICES)


def def__str__(self):
    return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
