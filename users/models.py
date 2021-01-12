from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.CharField(max_length=150, blank=True)
    profile_pic = models.ImageField(upload_to='Profile_pics',verbose_name='profile pic')

    user_types = [
        ("teacher","teacher"),
        ("student", "student"),
        ("parent", "parent")
    ]

    user_type = models.CharField(max_length=100,choices=user_types, default="student")

    def __str__(self):
        return self.user.username

