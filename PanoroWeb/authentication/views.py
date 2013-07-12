# Create your views here.
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext


def login_user(request):
    state = "Please login below!"
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return HttpResponseRedirect("/")
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    
    #context_instance to help with the csrf_token        
    return render_to_response('login.html',{'state':state, 'username': username,'password':password},context_instance=RequestContext(request))
                           


def invalidAccount(request):
    return render_to_response("login.html")
    

def logout_view(request):
    auth.logout(request)
    #return HttpResponseRedirect("/account/loggedout/")
    return HttpResponseRedirect("/")
    
def logout_show(request):
    return render_to_response('index.html')