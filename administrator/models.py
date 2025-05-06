from django.contrib.auth.models import AbstractUser 
from django.db import models

class Administrator(AbstractUser ):
    # Specify related names to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='administrators',  # Change this to avoid clash
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='administrators',  # Change this to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


