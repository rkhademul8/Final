
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from core.models import Staff,Hotel,Payment,Booking,Room


from core.forms import SignUpForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage


from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


# Create your views here.


class Signup(View):
    def get(self, request):
        return render(request, 'core/signup.html')

    def post(self, request):
        form = SignUpForm(request.POST)

        customer_group, created = Group.objects.get_or_create(name='Customer')
        # print(SignUpForm)
        # print(form.fields)
        # print(form.errors.as_json())
        print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            customer_group.user_set.add(user)
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('core/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            # form = SignUpForm()
            return render(request, 'core/signup.html', {'form': form})





def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model()._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')












class home(View):
    def get(self, request):
        q=Room.objects.all()

        return render(request,'core/index.html',{"data":q})




class about(View):
    def get(self, request):
        return render(request,'core/about.html',)

class contact(View):
    def get(self, request):
        return render(request,'core/contact.html',)

class accomodation(View):
    def get(self, request):
        return render(request,'core/accomodation.html',)

class gallery(View):
    def get(self, request):
        return render(request,'core/gallery.html',)


class test(View):
    def get(self, request):

        a=Staff.objects.all()

        return render(request,'core/test.html', {'data':a})


class insert(View):
    def get(self, request):
        return render(request,'core/insert.html')



class staff(View):
    def get(self,request):
        return render(request, 'core/staff.html')

    def post(self, request):
        f_name=request.POST["f_name"]
        l_name=request.POST["l_name"]
        contact=request.POST["contact"]
        address=request.POST["address"]
        gender=request.POST["gender"]
        image=request.POST["image"]
        date=request.POST["date"]
        email=request.POST["email"]
        password=request.POST["password"]

        # print(f_name,l_name,contact,address,gender,image,date,email,password)

        data=Staff(f_name=f_name,l_name=l_name,phone=contact,address=address,gender=gender,images=image,join_date=date,email=email,password=password)
        data.save()
        return render(request, 'core/staff.html')



class hotel(View):
    def get(self, request):
        return render(request, 'core/hotel.html')

    def post(sejf, request):
        name = request.POST["hotel_name"]
        location = request.POST['location']
        email = request.POST['email']
        number = request.POST['number']
        image = request.POST['image']


        data = Hotel(name=name, location=location, email=email, phone=number, images=image)
        data.save()

        return render(request, 'core/hotel.html')



class room(View):
    def get(self, request):
        return render(request,'core/room.html')

    def post(self, request):
        type=request.POST["type"]
        service=request.POST["service"]
        images=request.POST["image"]
        description=request.POST["description"]
        price=request.POST["price"]

        # print(type,service,images,description,price)

        data=Room(type=type,service=service,images=images,description=description,price=price)
        data.save()
        return render(request, 'core/room.html')


class booking(View):
    def get(self, request):
        return render(request, 'core/booking.html')

    def post(self, request):
        booking_date=request.POST["book_date"]
        check_in=request.POST["check_in_date"]
        check_out = request.POST["check_out_date"]
        adults = request.POST["adults"]
        childrens = request.POST["childs"]

        print(booking_date,check_in,check_out,adults,childrens)

        data=Booking(booking_date=booking_date,check_in=check_in,check_out=check_out, adults=adults,childrens=childrens,)

        data.save()
        return render(request,'core/booking.html')


class payment(View):
    def get(self, request):
        return render(request, 'core/payment.html')

    def post(self,request):
        amount=request.POST["amount"]
        credit=request.POST["credit"]
        date=request.POST["date"]



        data=Payment(amount=amount,credit_no=credit,date=date)
        data.save()

        return render(request, 'core/payment.html')


class room_view(View):
    def get(self,request):
        q=Room.objects.all()
        return render(request, 'core/room_view.html',{"data":q})


class room_details(View):
    def get(self,request):
        q = Room.objects.all()
        return render(request, 'core/room_details.html',{"data":q})


class cart(View):
    def get(self,request):

       return render(request, 'core/cart.html')



# class authentic(View):
#     def get(self,request):
#
#        return render(request, 'core/authentic.html')
#
#
# class handleSignup(View):
#
#     def post(self,request):
#
#         #  collect User information
#         groups=request.POST['group']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#
#         # form validation
#         if password1 != password2:
#             # messages.error(request, "Password didn't match! please try again.")
#             return redirect(request.META['HTTP_REFERER'])
#         if not username.isalnum():
#             # messages.error(request,
#             #                "Username should only contain lowercase letters and numbers without any special charecter.")
#             return redirect(request.META['HTTP_REFERER'])
#
#             # create user
#         myuser = User.objects.create_user(username, email, password1)
#
#         myuser.first_name = fname
#         myuser.last_name = lname
#         myuser.type=type
#
#         myuser.save()
#         group = Group.objects.get(name=groups)
#         myuser.groups.add(group)
#         # messages.success(request, "Your account has been successfully created")
#         return redirect(request.META['HTTP_REFERER'])
#
#
#
# class handleLogin(View):
#     def post(self,request):
#
#
#         #  collect User information
#         loginusername = request.POST['loginusername']
#         loginpassword = request.POST['loginpassword']
#
#         # validating user information
#         user = authenticate(username=loginusername, password=loginpassword)
#
#         # saving user information
#         if user is not None:
#             login(request, user)
#             # messages.success(request, "You have successfully logged in")
#             return redirect(request.META['HTTP_REFERER'])
#         else:
#             # messages.error(request, "Username or Password is not matched. Please try again !")
#             return redirect(request.META['HTTP_REFERER'])
#
#
#
#
#
#     # def handleLogout(request):
#     #     try:
#     #         logout(request)
#     #         messages.success(request, "Successfully log out!")
#     #         return redirect(request.META['HTTP_REFERER'])
#     #     except:
#     #         return render(request, 'home/home.html')