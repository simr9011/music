from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Album,Song


class Mylogin(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        u=self.cleaned_data['username']
        p=self.cleaned_data['password']
        v=authenticate(username=u,password=p)
        if v is None:
            raise forms.ValidationError('Username or Password did not match')
class Register(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    re_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
    def clean(self):
        data=super(Register,self).clean()
        p=data['password']
        p1=data['re_password']
        if p!=p1:
            raise forms.ValidationError('Password did not match')
class Addalbum(forms.ModelForm):
    class Meta:
        model=Album
        fields=['title','artist','genre','image','year']
class Addsong(forms.ModelForm):
    class Meta:
        model=Song
        fields=['al_id','title','artist','genre','soundfile','image']