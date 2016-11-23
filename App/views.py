from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from App import forms

@login_required(login_url="login/")

def home(request):
	return render(request,"home.html")


def register(request):
	if not request.user.is_authenticated():
		if request.method == "POST":
			form1 = forms.UserSignUpForm(request.POST)
			if form1.is_valid():
				user = form1.save(commit=False)
				user.password = make_password(form1.cleaned_data['password'])
				user.email = form1.cleaned_data['email']
				user.save()
				return HttpResponseRedirect('/')
		else:
			form1 = forms.UserSignUpForm()
		return render(request,'App/register.html',context={
			'form':form1
			})
	else:
		messages.error(request, 'You Are logged In')
		return redirect('/')


def change_password(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = PasswordChangeForm(request.user, request.POST)
			if form.is_valid():
				user = form.save()
				update_session_auth_hash(request, user)
				messages.success(request, 'Your password was successfully updated!')
				return redirect('/')
			else:
				messages.error(request, 'Please correct the error below.')
		else:
			form = PasswordChangeForm(request.user)
		return render(request, 'App/change_password.html', {
			'form': form
		})
	else:
		messages.error(request, 'You Are not logged In')
		return redirect('/')

