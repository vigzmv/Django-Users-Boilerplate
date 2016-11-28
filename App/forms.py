from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.contrib.auth.models import User

class UserSignUpForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','password','email','first_name','last_name',)
		help_texts = {
					'username': None,
				}
		widgets = {
			'password':forms.PasswordInput(),
		}

class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Username", max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
	password = forms.CharField(label="Password", max_length=30,widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
