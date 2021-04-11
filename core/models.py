
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email),)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255, default=None, null=True)
    last_name = models.CharField(max_length=255, default=None, null=True)

    email = models.EmailField(max_length=100, unique=True)

    username = None
    user_permissions = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    session_token = models.CharField(max_length=10, default=0)

    active = models.BooleanField(default=False)
    # a admin user; non super-user
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # a superuser

    phone = models.CharField(max_length=255, default=None, null=True)
    address = models.TextField(default=None, null=True)
    city = models.CharField(max_length=255, default=None, null=True)
    state = models.CharField(max_length=255, default=None, null=True)
    zip_code = models.CharField(max_length=255, default=None, null=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()








class Staff(models.Model):
    # role=models.
    # hotel_id=F.key
    f_name=models.CharField(max_length=50,null=True)
    l_name=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
    phone = models.IntegerField( null=True)
    address=models.CharField(max_length=50,null=True)
    images = models.ImageField(null=True)
    gender=models.CharField(max_length=50,null=True)
    join_date=models.DateTimeField(auto_now=False, auto_now_add=False)


class Division(models.Model):
    division = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.division

class District(models.Model):
    district=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.district




class Thana(models.Model):

    division=models.ForeignKey(Division, blank = True, null = True, on_delete=models.CASCADE)
    district=models.ForeignKey(District, blank = True, null = True, on_delete=models.CASCADE)
    thana = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.thana

class Hotel(models.Model):
    name=models.CharField(max_length=20,null=True)
    location = models.ForeignKey(Thana, blank=True, null=True, on_delete=models.CASCADE)
    email=models.EmailField(max_length=50,null=True)
    phone=models.IntegerField(null=True)
    images = models.ImageField(null=True)


class Room(models.Model):
    # room_id=models
    # hotel_id=models.IntegerField() F key
    type=models.CharField(max_length=20,null=True)
    service=models.CharField(max_length=20,null=True)
    images=models.ImageField(null=True)
    description=models.TextField(max_length=100,null=True)
    price=models.IntegerField(null=True)
    booking=models.BooleanField(default=True)

class Booking(models.Model):
    # booking_id=models.
    # customer_id=models. F.key
    booking_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    check_in=models.DateTimeField(auto_now=False, auto_now_add=False)
    check_out=models.DateTimeField(auto_now=False, auto_now_add=False)
    adults=models.IntegerField(null=True)
    childrens=models.IntegerField(null=True)


class Payment(models.Model):
    # payment_id=models.IntegerField(null=True)
    # customer_id=models. F.key
    # book_id=models. F.key
    amount=models.IntegerField(null=True)
    credit_no=models.IntegerField(null=True)
    date=models.DateTimeField(auto_now_add=False)


