from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
import uuid


# Create your models here.


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    token = models.CharField(max_length=255, blank=True, null=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        return self.name

    def __str__(self):
        return self.email


class Post(models.Model):
    post_id = models.CharField(primary_key=True, max_length=20, unique=True)
    content = models.TextField()
    author = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.post_id = str(uuid.uuid4())[:10]  # Use a portion of the UUID
        super().save(*args, **kwargs)

    def __str__(self):
        return self.author


class Project(models.Model):
    project_id = models.CharField(primary_key=True, max_length=50, unique=True)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.project_id:
            self.project_id = str(uuid.uuid4())[:10]  # Use a portion of the UUID
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
