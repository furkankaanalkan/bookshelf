from django.urls import path 
from . import views

app_name = "main_page_app"

urlpatterns = [
    path("main_page/",views.deneme ,name="deneme")
]
