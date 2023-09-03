import os

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
import uuid
from PIL import Image


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
    avatar = models.ImageField(upload_to='images/users/avatars/', blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = uuid.uuid4()
            while UserAccount.objects.filter(user_id=self.user_id).exists():
                self.user_id = uuid.uuid4()
        super().save(*args, **kwargs)

    def get_name(self):
        return self.name

    def __str__(self):
        return self.email


class Post(models.Model):
    post_id = models.CharField(primary_key=True, max_length=100, unique=True)
    content = models.TextField()
    author_name = models.CharField(max_length=100, blank=True, null=True)
    author_id = models.CharField(max_length=100, blank=True, null=True)
    likes = models.CharField(max_length=1000000, blank=True, null=True)
    comments = models.JSONField(default=list)

    # created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.post_id:
            self.post_id = str(uuid.uuid4())[:40]  # Use a portion of the UUID
        super().save(*args, **kwargs)

    def __str__(self):
        return self.author_name


class Project(models.Model):
    project_id = models.CharField(primary_key=True, max_length=50, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100, blank=True, null=True)
    image_src = models.ImageField(upload_to='images/projects', blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    author_id = models.CharField(max_length=100, blank=True, null=True)
    subscribers = models.JSONField(default=list)

    # created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.project_id:
            self.project_id = str(uuid.uuid4())[:40]  # Use a portion of the UUID
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Job(models.Model):
    job_id = models.CharField(primary_key=True, max_length=50, unique=True)
    project_id = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100)
    work_format = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    responsibility = models.TextField()
    requirements = models.TextField()
    we_offer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.job_id:
            self.job_id = str(uuid.uuid4())[:40]  # Use a portion of the UUID
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class StudentsClub(models.Model):
    students_club_id = models.CharField(primary_key=True, max_length=50, unique=True)
    title = models.CharField(max_length=100)
    related_by_uni = models.JSONField(default=list)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.JSONField(default=list)
    author_id = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.students_club_id:
            self.students_club_id = str(uuid.uuid4())[:40]  # Use a portion of the UUID
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
