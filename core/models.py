from django.db import models

# Create your models here.

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
