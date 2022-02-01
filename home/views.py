from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import SignUp
from .forms import SignUpForm,LoginForm,UpdateForm,ChangePasswordForm
from django.contrib import messages
from django.contrib.auth import logout as logouts

# Create your views here.
def func1(request):
	return HttpResponse("Welcome to Django")

def index(request):
	
	return render(request,'index.html')

def register(request):
	if request.method=='POST':
		form1=SignUpForm(request.POST,request.FILES)
		if form1.is_valid():
			name=form1.cleaned_data['Name']
			age=form1.cleaned_data['Age']
			email=form1.cleaned_data['Email']
			password=form1.cleaned_data['Password']
			confirmPassword=form1.cleaned_data['ConformPassword']
			photo=form1.cleaned_data['Photo']
			user=SignUp.objects.filter(Email=email).exists()
			if user:
				messages.success(request,'Email Already Exist')
				return redirect('register/')
			elif password!=confirmPassword:
				messages.success(request,'Password missmatch')
				return redirect('register/')
			else:
				table=SignUp(Name=name,Age=age,Email=email,Password=password,Photo=photo)
				table.save()
				messages.success(request,'Registration Successful')
				return redirect('/')
	else:
		form1 =SignUpForm
	return render(request,'SignUp.html',{'form':form1})

def login(request):
	if request.method=='POST':
		form2=LoginForm(request.POST)
		if form2.is_valid():
			email=form2.cleaned_data['Email']
			password=form2.cleaned_data['Password']
			user=SignUp.objects.get(Email=email)
			if not user:
				messages.success(request,'Email does not exist')
				return redirect('login/')
			else:
				messages.success(request,'login successful')
				return redirect('/home/%s' % user.id)
	else:
		form2=LoginForm
	return render(request,'Login.html',{'form':form2})

def home(request,id):
	user=SignUp.objects.get(id=id)
	return render(request,'home.html',{'user':user})

def update(request,id):
	user=SignUp.objects.get(id=id)
	form=UpdateForm(request.POST or None,request.FILES or None,instance=user)
	if form.is_valid():
		form.save()
		messages.success(request,'Updated successfully')
		return redirect('/home/%s' % user.id)
	return render(request,'update.html',{'user':user,'form':form})

def changePassword(request,id):
	user=SignUp.objects.get(id=id)

	if request.method=='POST':
		form=ChangePasswordForm(request.POST)
		if form.is_valid():
			oldPassword=form.cleaned_data['OldPassword']
			password=form.cleaned_data['Password']
			confirmPassword=form.cleaned_data['ConformPassword']
			if oldPassword!=user.Password:
				messages.success(request,'Password does not exist')
				return redirect('/changePassword/%s' % user.id)
			elif password!=confirmPassword:
				messages.success(request,'Password missmatch')
				return redirect('changePassword/%s' % user.id)
			else:
				user.Password=password
				user.save()
				messages.success(request,'Password change successful')
				return redirect('/home/%s' % user.id)
	else:
		form=ChangePasswordForm()
	return render(request,'ChangePassword.html',{'user':user,'form':form})

def logout(request):
	logouts(request)
	messages.success(request,'logout successfully')
	return redirect('/')
