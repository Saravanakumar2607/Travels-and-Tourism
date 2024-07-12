from django import forms
from django.contrib.auth.forms import UserCreationForm
from tour.models import CustomUser, Booking


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label="Username",initial="Username")
    email = forms.EmailField(label="Email" ,initial="Email address")
    password = forms.CharField(label="Password",initial="Password",widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password",initial="Confirm Password",widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = '__all__'

class BookingForm(forms.ModelForm):
    from_location = forms.CharField(label="From Location")
    to_location = forms.CharField(label="To Location")
    persons = forms.IntegerField(label="Persons")
    arrival_date = forms.DateField(widget=forms.SelectDateWidget)
    leaving_date = forms.DateField(widget=forms.SelectDateWidget)
    details = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Booking
        fields = '__all__'
