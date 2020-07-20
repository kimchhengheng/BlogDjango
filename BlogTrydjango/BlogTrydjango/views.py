from django.shortcuts import render
from django.http import HttpResponse
from .forms import Contactform

def home(request):
    #html = "<h1>Home</h1>"
    #return HttpResponse(html)
    name = "home.html"
    context = {'title': "home" , 'content': "home"}
    return render(request, name, context)

def contact(request):
    form = Contactform(request.POST or None)
    if form.is_valid():
        form=Contactform()
    name = "contact.html"
    context = {'title': "contact" , 'content': "contact", 'form':form}
    return render(request, name, context)
    #html = "<h1>contact</h1>"
    #return HttpResponse(html)

def about(request):
    name = "about.html";
    context = {'title': "about" , 'content': "about"}
    return render(request, name, context)
    #html = "<h1>about</h1>"
    #return HttpResponse(html)