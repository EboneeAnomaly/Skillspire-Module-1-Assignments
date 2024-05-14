from django import forms

class ContactForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    streetaddress = forms.CharField(max_length=200)
    state = forms.CharField(max_length=100)
    zip = forms.CharField(max_length=10)
