"""fhrs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core import views
from django.urls import  include,path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home.as_view(), name='home'),
    path('about', views.about.as_view(), name='about'),
    path('contact', views.contact.as_view(), name='contact'),
    path('accomodation', views.accomodation.as_view(), name='accomodation'),
    path('gallery', views.gallery.as_view(), name='gallery'),
    path('test', views.test.as_view(), name='test'),
    path('insert', views.insert.as_view(), name='insert'),
    path('staff/', views.staff.as_view(), name='staff'),
    path('hotel/', views.hotel.as_view(), name='hotel'),
    path('room/', views.room.as_view(), name='room'),
    path('booking/', views.booking.as_view(), name='booking'),
    path('payment/', views.payment.as_view(), name='display'),
    path('room_view/', views.room_view.as_view(), name='room_view'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
