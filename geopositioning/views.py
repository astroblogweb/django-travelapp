from django.shortcuts import render, render_to_response

# Create your views here.

def geo(request):
    return render_to_response('geo.html')

