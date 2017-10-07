from django.shortcuts import render,render_to_response
# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


def homepage(request):
    return render_to_response('homepage.html')


def new_admin(request):
    return render_to_response('new_admin.html')

def logout_page(request):
    print("redir logout screen to homepage")
    logout(request)
    return HttpResponseRedirect('/')
#    return render_to_response('homepage.html')
