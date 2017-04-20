from django.shortcuts import render, redirect, HttpResponse
from .models import User

def index(request):

    print ("Running index method, calling out to User")
    user = User.objects.login('charles@codingdojo.com', 'charles')

    print (type(user))
    if 'error' in user:
        pass
    if 'theuser' in user:
        pass
    return HttpResponse(User.objects.login('charles@codingdojo.com', 'charles'))

# Create your views here.
