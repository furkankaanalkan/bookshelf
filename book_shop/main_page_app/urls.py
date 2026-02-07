from django.urls import path 
from . import views

app_name = "main_page_app"

urlpatterns = [
    path("",views.main_page ,name="main_page"),
    path("log-in.page/",views.login_page ,name="login_page"),
    path("MyCart/",views.login_page ,name="cart"),
]
