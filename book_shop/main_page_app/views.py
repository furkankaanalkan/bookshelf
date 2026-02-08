from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

def add_book(request):
    if request.POST:
        name = request.POST['name']
        description = request.POST['book_description']
        image = request.FILES['image'] 

        models.Book.objects.create( name=name, book_description=description, image=image)
        
        return redirect ( reverse ('main_page_app:Book'))
    
    return render(request, "main_page_app/main_page.html")


def list_books(request):
    all_books = models.Book.objects.all()
    book_dict = {"books":all_books}
    return render(request,'main_page_app/main_page.html',context=book_dict)







def cart(request):
    return render ( request,"main_page_app/cart.html")



class Sign_up(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"