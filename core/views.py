
from django.shortcuts import render

# Create your views here.
from django.views import View

from django.http import HttpResponse

from core.models import Staff,Hotel,Payment,Booking,Room


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
        amount=request.POST["amount"]
        payments=request.POST["payments"]
        update=request.POST["update"]

        # print(booking_date,check_in,check_out,amount,payments,update)
        data=Booking(booking_date=booking_date,check_in=check_in,check_out=check_out, amount=amount,payment_status=payments,updated_by=update)

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