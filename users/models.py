from django.db import models
from django.contrib.auth import models as dj_models
from includes.helpers import models as helper_models
from django.core.validators import EmailValidator, MinValueValidator

class UserAccount(dj_models.AbstractUser, helper_models.PrimaryKeyMixin, helper_models.DateHistoryMixin):
    username = None
    email = models.EmailField(
        unique=True,
        validators=[EmailValidator(message="Enter a valid email address.")],
        error_messages={'unique': "User with this email already exists."}
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0, message="Age must be a positive number.")]
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        db_table = 'users'
        ordering = ['-date_created']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    def update_fields(self, **kwargs):
        
        updated = False
        valid_fields = ['first_name', 'last_name', 'age']
        
        for field, value in kwargs.items():
            if field in valid_fields and getattr(self, field) != value:
                setattr(self, field, value)
                updated = True
        
        if updated:
            self.save(update_fields=list(kwargs.keys()) + ['date_updated'])
        
        return updated