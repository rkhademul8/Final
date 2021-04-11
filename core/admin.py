from django.contrib import admin
from .models import CustomUser

# Register your models here.
from .models import Staff,Hotel,Room,Booking,Payment,District,Thana,Division
from django.contrib.auth.models import User

# admin.site.register(Staff)
# admin.site.register(Hotel)
# admin.site.register(Room)
# admin.site.register(Booking)
# admin.site.register(Payment)

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name')


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone','address','city',)



@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name','location','email','phone','images')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('type','service','images','description','price')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_date','check_in','check_out','adults','childrens')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount','credit_no','date')



@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('division',)

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('district',)

@admin.register(Thana)
class ThanaAdmin(admin.ModelAdmin):
    list_display = ('thana',)

