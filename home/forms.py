from django import forms
from . models import SignUp

class SignUpForm(forms.ModelForm):
	Password=forms.CharField(max_length=12,widget=forms.PasswordInput)
	ConformPassword=forms.CharField(max_length=12,widget=forms.PasswordInput)
	class Meta():
		model=SignUp
		fields='__all__'

class LoginForm(forms.ModelForm):
	Password=forms.CharField(max_length=12,widget=forms.PasswordInput)
	class Meta():
		model=SignUp
		fields=('Email','Password')

class UpdateForm(forms.ModelForm):
	class Meta():
		model=SignUp
		fields=('Name','Age','Email','Photo')

class ChangePasswordForm(forms.Form):
	OldPassword=forms.CharField(max_length=12,widget=forms.PasswordInput)
	Password=forms.CharField(max_length=12,widget=forms.PasswordInput)
	ConformPassword=forms.CharField(max_length=12,widget=forms.PasswordInput)
	