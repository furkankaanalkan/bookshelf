from django.shortcuts import render



def main_page(request):
    if request.POST:
        message = request.POST["message"]
        models.Book.objects.create(name=request.name, message=request.book_description,image=request.image)
        return redirect(reverse('main_page_app:Book'))
    else:
        return render ( request,"main_page_app/main_page.html")


def login_page(request):
    return render ( request,"main_page_app/login_page.html")


def cart(request):
    return render ( request,"main_page_app/cart.html")
