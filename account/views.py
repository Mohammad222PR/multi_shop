from django.shortcuts import render, redirect, reverse
from django.views import View
from account.forms import LoginForm, OtpLoginForm, CheckOtpCodeForm
from account.models import User, Otp
from django.contrib.auth import authenticate, login, logout
import ghasedakpack
from random import randint
from uuid import uuid4
# Create your views here.


# def user_login(request):
#     return render(request,'account/login.html')
SMS = ghasedakpack.Ghasedak("04f9bb08893e4ca0565187eaa3a51903ae2bf2b4c4c2b8864a8339b73742c5a6")


class UserLogin(View):
    form_class = LoginForm
    template_name = 'account/login.html'
    def get(self, request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'], password = cd['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('username','Invalid username number')

        else:
            form.add_error('username','invalid data')

        return render(request,self.template_name, {'form':form})
    

class OtpLoginView(View):
    form_class = OtpLoginForm
    template_name = 'account/otp_login.html'
    def get(self, request):
        form = self.form_class()
        return render(request,self.template_name, {'form':form})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000, 9999)
            SMS.verification({'receptor': cd['phone'],'type': '1','template': 'randcode','param1': randcode})
            token = str(uuid4())
            Otp.objects.create(phone = cd['phone'], code = randcode, token = token)
            print(randcode)
            return redirect(reverse('account:check_otp') + f'?token={token}')
        else:
            form.add_error('phone','Invalid Phone number')

        return render(request,self.template_name, {'form': form})
    

class CheckOtpView(View):
    form_class = CheckOtpCodeForm
    template_name = 'account/check_otp.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        token = request.GET.get('token')
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code= cd['code'], token=token):
                otp = Otp.objects.get(token = token)
                user, is_created = User.objects.get_or_create(phone=otp.phone)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                otp.delete()
                return redirect('/')

        return render(request,self.template_name, {'form':form})
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')