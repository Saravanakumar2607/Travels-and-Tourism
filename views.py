
from django.shortcuts import render, redirect
from travel.forms import UserRegisterForm
from travel.forms import BookingForm

def index(request):
    return render(request, 'index.html')
# Define the registration form


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to login page after successful registration
        else:
            print("Errors: ", form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def book_trip(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
        else:
            print("Booking Errors", form.errors)
    else:
        form = BookingForm()
    return render(request, 'book_trip.html', {'form': form})


def success(request):
    return render(request, 'success.html' )


def booking_success(request):
    return render(request, 'booking_success.html')



