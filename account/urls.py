from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/',views.UserLogin.as_view(), name='user_login'),
    path('singup/',views.OtpLoginView.as_view(), name='user_otp'),
    path('checkotp/',views.CheckOtpView.as_view(), name='check_otp'),
    path('logout/',views.LogoutView.as_view(), name='user_logout')

]
