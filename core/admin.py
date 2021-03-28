from django.contrib import admin

# Register your models here.
from .models import Staff,Hotel,Room,Booking,Payment

# admin.site.register(Staff)
# admin.site.register(Hotel)
# admin.site.register(Room)
# admin.site.register(Booking)
# admin.site.register(Payment)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('f_name','l_name','email','password','phone','address','images','gender','join_date')


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name','location','email','phone','images')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('type','service','images','description','price')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_date','check_in','check_out','amount','status','payment_status','updated_by')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount','credit_no','date')
