from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import login


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




def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # 1. Kullanıcıyı oluştur ve değişkene ata
            user = form.save() 
            
            # 2. Otomatik giriş yaptır (Kritik nokta burası)
            login(request, user) 
            
            # 3. Giriş yaptıktan sonra yönlendir
            return redirect('main_page_app:cart') 
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})













"""
class Sign_up(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Manüel olarak her alana Bootstrap sınıfı ekliyoruz
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        return form
"""