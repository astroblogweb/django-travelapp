from django.shortcuts import render, render_to_response

# Create your views here.

def geomaps__(request):
    return render_to_response('geomaps.html')



def geomaps(request):
    print("inside geomaps")
    return render_to_response("base_geomaps_withoutdjango.html")
