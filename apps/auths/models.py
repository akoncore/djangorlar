# django modules
from typing import Any
from django.db.models import (
    EmailField, CharField, BooleanField, DateField, DateTimeField, DecimalField
)
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.utils import timezone

# Project modules
from apps.auths.validators import (
    validate_email_domain,
    validate_email_payload_not_in_full_name
)
from apps.abstracts.models import AbstractBaseModel


class CustomUserManager(BaseUserManager):

    def __obtain_user_instance(
        self,
        email: str,
        full_name: str,
        password: str,
        **kwargs
    ) -> 'CustomUser':
        if not email:
            raise ValidationError({"message": "The Email must be set"})
        if not full_name:
            raise ValidationError({"message": "The Full Name must be set"})

        new_user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            **kwargs
        ) 
        return new_user

    def create_user(
        self,
        email: str,
        full_name: str,
        password: str,
        **kwargs: dict[str, Any]
    ) -> 'CustomUser':
        new_user:'CustomUser' = self.__obtain_user_instance(
            email=email, 
            full_name=full_name, 
            password=password, 
            **kwargs
        )
        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user

    def create_superuser(
        self,
        email: str,
        full_name: str,
        password: str,
        **kwargs: dict[str, Any]
    ) -> 'CustomUser':
        new_user:'CustomUser' = self.__obtain_user_instance(
            email=email,
            full_name=full_name,
            password=password,
            is_staff=True,
            is_superuser=True,
            **kwargs
        )
        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user


class CustomUser(AbstractBaseModel, PermissionsMixin, AbstractBaseUser):
    DEPARTMENT_CHOICES = (
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('Marketing', 'Marketing'),
        ('Sales', 'Sales'),
    )

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )

    email: EmailField = EmailField(
        unique=True,
        max_length=255,
        db_index=True,
        validators=[validate_email_domain],
        verbose_name="Email Address",
        help_text="Unique email address used for authentication"
    )
    first_name: CharField = CharField(
        max_length=30,
        verbose_name="First Name",
        help_text="User's given name"
    )
    last_name: CharField = CharField(
        max_length=30,
        verbose_name="Last Name",
        help_text="User's family name"
    )
    full_name = CharField(
        max_length=50,
        verbose_name="Full Name",
        help_text="First name + Last name"
    )
    password = CharField(
        max_length=128,
        validators=[validate_password],
        verbose_name="Password",
        help_text="Must meet Django password validation requirements"
    )
    city = CharField(
        max_length=50,
        verbose_name="City",
        help_text="City where the user resides"
    )
    country = CharField(
        max_length=50,
        verbose_name="Country",
        help_text="User's country of residence"
    )
    department = CharField(
        max_length=20,
        choices=DEPARTMENT_CHOICES,
        verbose_name="Department",
        default='IT',
        help_text="Department within the company"
    )
    role = CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        verbose_name="Role",
        default='employee',
        help_text="User's role in the organization"
    )
    birth_date = DateField(
        blank=True,
        null=True,
        verbose_name="Birth Date",
        help_text="User's date of birth (optional)"
    )
    salary = DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Salary",
        help_text="User's monthly salary"
    )
    is_active = BooleanField(
        default=True,
        verbose_name="Is Active",
        help_text="Designates whether this user is active"
    )
    is_staff = BooleanField(
        default=False,
        verbose_name="Is Staff",
        help_text="Designates whether this user can access the admin site"
    )
    date_joined = DateTimeField(
        default=timezone.now,
        verbose_name="Date Joined",
        help_text="Date when the user joined the system"
    )
    last_login = DateTimeField(
        verbose_name='Last Login',
        null=True,
        blank=True,
        help_text="The last time the user logged in"
    )

    REQUIRED_FIELDS = ["full_name"]
    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
        ordering = ["-created_at"]

    def clean(self):
        validate_email_payload_not_in_full_name(
            email=self.email,
            full_name=self.full_name
        )
        return super().clean()
