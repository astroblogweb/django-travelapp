from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext



#@login_required
def homepage(request):
    print("in homepage view func")
    return render(request,'homepage.html') # works better than r_2_r
    #return render_to_response('homepage.html') # works, but username not appearing on homepage-alone


def new_admin(request):
    return render_to_response('new_admin.html')

def logout_page(request):
    print("redir logout screen to homepage")
    logout(request)
    return HttpResponseRedirect('homepage')
