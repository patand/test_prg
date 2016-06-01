from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, Context, loader
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
def main_page(request):
   
    state = " "
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
       
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/main/")
                
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Try again, username and/or password incorrect."

    return render_to_response('registration/main_page.html',{'state':state, 'username': username}, context_instance=RequestContext(request))
