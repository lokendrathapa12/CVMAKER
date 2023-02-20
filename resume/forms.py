from django import forms
class registration_Form(forms.Form):
    username = forms.CharField(max_length=100)
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

class PersonalForm(forms.Form):
    image = forms.ImageField(widget=forms.ImageField())
    fullname = forms.CharField(widget=forms.TextInput())
    jobtitle = forms.CharField(widget=forms.TextInput())
    address1 = forms.CharField(widget=forms.TextInput())
    address2 = forms.CharField(widget=forms.TextInput())
    address3 = forms.CharField(widget=forms.TextInput())
    phone = forms.IntegerField(widget=forms.NumberInput())
    mobile = forms.IntegerField(widget=forms.NumberInput())
    email = forms.EmailField(widget=forms.EmailInput())

