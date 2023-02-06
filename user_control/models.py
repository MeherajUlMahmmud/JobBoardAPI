from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from base.g_models import BaseModel


class MyUserManager(BaseUserManager):
    def create_applicant(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            is_applicant=True,
        )

        user.set_password(password)
        user.save(using=self._db)

        # applicant = ApplicantModel.objects.create(user=user, first_name=first_name, last_name=last_name)
        # applicant.save(using=self._db)

        return user

    def create_organization(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            is_organization=True,
        )

        user.set_password(password)
        user.save(using=self._db)

        # organization = OrganizationModel.objects.create(user=user, name=name)
        # organization.save(using=self._db)

        return user

    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser, BaseModel, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_expiry = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'users'

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


class ApplicantModel(BaseModel):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE,
                                related_name='applicant')  # OneToOneField is used to create a one-to-one
    # relationship between the two models and related_name is used to access the related object from the other side
    # of the relationship.
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    resume = models.FileField(upload_to='resumes', null=True, blank=True)

    class Meta:
        db_table = 'applicants'

        verbose_name = 'Applicant'
        verbose_name_plural = 'Applicants'

    def __str__(self):
        return self.user.email


class OrganizationModel(BaseModel):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='organization')
    name = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='company_logos', null=True, blank=True)
    cover_picture = models.ImageField(upload_to='cover_pictures', null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'organizations'

        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'

    def __str__(self):
        return self.name
