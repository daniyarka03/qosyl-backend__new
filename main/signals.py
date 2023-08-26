from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model


def updateUser(sender, instance, **kwargs):
    user = instance
    if user.email != '':
        user.username = user.email


pre_save.connect(updateUser, sender=get_user_model())
