from django.shortcuts import render, render_to_response

# Create your views here.

def geomaps(request):
    return render_to_response('geomaps.html')

