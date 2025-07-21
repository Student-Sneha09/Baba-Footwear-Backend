from django.shortcuts import render,redirect
from .models import Product
from django.contrib import messages 

# Create your views here.
def home(request):
    products= Product.objects.all()
    return render(request, 'shop/index.html', {'products':products})

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST["name"]
        whatsapp=request.POST["whatsapp"]
        email=request.POST["email"]
        reason=request.POST["reason"]
        messages.success(request,"Submitted Successfully! Continue Shopping.")
        return redirect('home')
    return render(request, 'shop/contact.html')
