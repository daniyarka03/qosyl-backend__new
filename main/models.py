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
    image_src = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    author_id = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.project_id:
            self.project_id = str(uuid.uuid4())[:40]  # Use a portion of the UUID
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
