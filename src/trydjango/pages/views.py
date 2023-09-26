from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def homepage_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hellow World</h1>") # string of html code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contact Page</h1>") # string of html code
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "This_is_true": True,
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": { 123, 456, 789 }
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>") # string of html code