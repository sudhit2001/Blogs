from django.urls import path,re_path
from . import views

app_name='accounts'

urlpatterns = [
    path('signup',views.signup,name="signup"),
    path('login',views.loginn,name="login"),
    path('logout',views.logoutt,name="logout")
]
