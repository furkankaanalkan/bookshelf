from django.shortcuts import render



def deneme(request):
    return render ( request,"main_page_app/main_page.html")

# Create your views here.
