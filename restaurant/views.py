# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu, Booking
from django.core import serializers
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .serializers import MenuItemsSerializer, BookingSerializer
from rest_framework.viewsets import generics, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.filter()
    serializer_class = MenuItemsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def home(request):
    return render(request, 'index-home.html')


def about(request):
    return render(request, 'about.html')


def reservations(request):
    # date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    context = {"bookings": booking_json}
    return render(request, 'bookings.html', context)


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)


# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    context = {"menu": main_data}
    return render(request, 'menu.html', context)


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 


@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        reservation_date = data['reservation_date']
        reservation_slot = data['reservation_slot']
        exist = Booking.objects.filter(reservation_date=reservation_date).filter(reservation_slot=reservation_slot).exists()
        if not exist:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=reservation_date,
                reservation_slot=reservation_slot,
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date', datetime.today().date())

    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, {'content_type': 'application/json'})