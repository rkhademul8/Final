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
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="core/password_reset.html"), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="core/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="core/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="core/password_reset_done.html"), name ='password_reset_complete'),
    # path('', include('django.contrib.auth.urls')),
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
    path('room_details/', views.room_details.as_view(), name='room_details'),
    path('cart/', views.cart.as_view(), name='cart'),
    # path('authentic/', views.authentic.as_view(), name='authentic'),
    # path('signup/', views.handleSignup.as_view(), name='handleSignup'),
    # path('login/', views.handleLogin.as_view(), name='handleSignup'),
    path('activate/<uidb>/<token>/', views.ActivateURL.as_view(), name='activate'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('user/', views.Mul_user.as_view(), name='user'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
