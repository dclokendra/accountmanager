from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from account.models import Account


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        e = request.POST.get('email')
        p = request.POST.get('password')
        user = authenticate(email=e, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "login Credential doesnot match")
            return redirect('login')


class SignupView(View):
    template_name = 'signup.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *arg, **kwargs):
        f = request.POST.get('first_name')
        l = request.POST.get('last_name')
        e = request.POST.get('email')
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        if p1 == p2:
            Account.objects.create_user(e, first_name=f, last_name=l, password=p1)
            messages.add_message(request, messages.SUCCESS, "Signup Successfull")
            return redirect('login')
        else:
            messages.add_message(request, messages.ERROR, 'Signup Failed')
            return redirect('signup')


class Dashboard(LoginRequiredMixin,View):
    login_url = '/account/login'
    template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name)
