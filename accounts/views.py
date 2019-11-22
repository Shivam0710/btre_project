from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
	if request.method == "POST":
		
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')

		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			messages.success(request, "You have successfully logged in")
			return redirect('dashboard')
		else:
			messages.error(request, "Invalid Credentials")
			return redirect('login')

		return redirect('login')
	else:
		return render(request, 'accounts/login.html')

def logout(request):
	if request.method == "POST":
		messages.success(request, "You have successfully logged out")
		auth.logout(request)
		return redirect('index')

def register(request):
	if request.method == "POST":
		firstname = request.POST.get('first_name', '')
		lastname = request.POST.get('last_name', '')
		username = request.POST.get('username', '')
		email = request.POST.get('email', '')
		password = request.POST.get('password', '')
		password2 = request.POST.get('password2', '')

		if password != password2:
			messages.error(request, "Password do not match")
			return redirect('register')
		else:
			if User.objects.filter(username=username).exists():
				messages.error(request,"Username already exists")
				return redirect('register')
			else:
				if User.objects.filter(email=email).exists():
					messages.error(request,"Email is already taken")
					return redirect('register')
				else:
					User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname, password=password)
					messages.success(request, "You are registered and can log in now")
					return redirect('login')
	else:
		return render(request, 'accounts/register.html')

def dashboard(request):
	return render(request, 'accounts/dashboard.html')