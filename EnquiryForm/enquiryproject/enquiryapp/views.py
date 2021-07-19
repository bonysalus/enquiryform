from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
# Create your views here.
def index(request):


    if request.method == "POST":
        name = request.POST.get('name', )
        email = request.POST.get('email', )
        subject = request.POST.get('subject', )
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        return render(request,'detail.html',{'contact':contact})



    return render(request,'index.html')

def detail(request,id):
    contact = Contact.objects.get(id=id)

    return render(request,'detail.html',{'contact':contact})

def update(request,id):
    contact=Contact.objects.get(id=id)
    form=ContactForm(request.POST or None ,request.FILES ,instance=contact)
    if form.is_valid():
        form.save()
        return render(request,'detail.html',{'contact':contact})
    return render(request,'edit.html',{'form':form,'contact':contact})

def delete(request,id):
    if request.method=="POST":
        contact=Contact.objects.get(id=id)
        contact.delete()
        return redirect('/')
    return render(request,'delete.html')