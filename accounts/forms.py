from django import forms
from . models import profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
    
class userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']



 
class profileform(forms.ModelForm):
    class Meta:
        model=profile
        fields=['phone','address']