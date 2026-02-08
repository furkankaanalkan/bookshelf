from django.urls import path 
from . import views

app_name = "main_page_app"

urlpatterns = [
    path("",views.list_books ,name="main_page"),
    path("MyCart/",views.cart ,name="cart"),
    path('signup/',views.Sign_up.as_view(),name="signup"),
]

