from django.shortcuts import render, render_to_response
from .models import Shortlist
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
# Create your views here.
from .models import Shortlist
import requests
import json
from geopy.geocoders import GoogleV3


def geomaps__(request):
    return render_to_response('geomaps.html')



def geomaps(request):
    print("inside geomaps")
    #return render_to_response("base_geomaps.html")
    #return render_to_response("single_site.html")
    #return render_to_response("multiple_site.html")

    #return render_to_response("schedule.html")
    shortlisted=Shortlist.objects.all()
    return render(request,"schedule.html",{"shortlisted":shortlisted})  # works



@csrf_protect
def geomaps_shortlist(request):
    #print("inside shortlist places.. ajax")

    if request.method=="POST":
        val=request.POST['val']
        lat=request.POST['lat']
        lng=request.POST['lng']
        location=request.POST['location']
        formatted_address=request.POST['formatted_address']
        sitelabel=request.POST['sitelabel']
        placeid=request.POST['placeid']
        order=Shortlist.objects.all().count()

        Shortlist.objects.create(
            val=val,lat=lat,lng=lng,location=location,
            formatted_address=formatted_address,
            sitelabel=sitelabel,placeid=placeid,order=order
            )
        #return HttpResponse("created")
        #print("new entry created")
        print(Shortlist.objects.all().count(),"post :)","lat:",lat,"lng:",lng,"address:",formatted_address,"sitelabel:",sitelabel)
        #return render_to_response("schedule.html",{"site_latlng":site_latlng})


        #site_latlng={"lat":0.0,"lng":100.100}
        #return render_to_response("pure_ajax_extract_latlng.html",{"site_latlng":site_latlng})



        shortlisted=Shortlist.objects.all()
        return render(request,"schedule.html",{"shortlisted":shortlisted})
        #return render(request,"pure_ajax_extract_latlng.html",{"site_latlng":site_latlng})  # works
        # @csrf_token +   render()  : takes care of Forbidden csrf token


        #return HttpResponse('')
    else:
        print("request method is not post")
    return HttpResponse("ajax shortlisting failed")


def geomaps_shortlisted_display(request):
    shortlisted=Shortlist.objects.all()
    return render(request, "display_shortlisted.html",{"shortlisted":shortlisted})


def rev_geocode(lat, lng):
    latlng=str(lat)+',  '+str(lng)
    print(latlng)
    geolocator = GoogleV3()
    #location = geolocator.reverse("52.509669, 13.376294")
    location = geolocator.reverse(latlng)
    print("in reverse geocoding",*location,sep="\n") #.addres)
    return location


def rev_geocode_google_api(lat, lng):
    url="http://maps.googleapis.com/maps/api/geocode/json?latlng=%f,%f&sensor=false" %(lat,lng)
    print(url)
    json_result=requests.get(url)
    print(json_result)
    return json_result


def reverse_geocoding(request):
    lat=12.992933851703029 #52.509669
    lng=80.15189921788328 #13.376294

#    location=rev_geocode(lat,lng)
#    return HttpResponse(location)
    location=rev_geocode_google_api(lat,lng)
    return HttpResponse(location) #,content_type="application/json") #.address)


def geomaps_directions(request):
    return render(request,"directions.html",{})


@csrf_protect
def geomaps_ordering(request):
    print("inside geomaps_ordering")
    if request.method=="POST":
        button=request.POST['pressed_button']
        site,action,orderpk=button.split('_')
        orderpk=int(orderpk)
        print(action,orderpk)

        if action=="delete":
            print("order:",orderpk,"number of entries b4 del:",Shortlist.objects.all().count())
            s=Shortlist.objects.filter(order=orderpk-1).delete()
            print("number of entries after del:",Shortlist.objects.all().count())

        if action=="moveup":
            current_down_to_up=Shortlist.objects.filter(order=orderpk-1)[0]
            print(current_down_to_up.order)
            current_down_to_up.order=min(1,current_down_to_up.order-1)
            print(current_down_to_up.order)
            current_up_to_down=Shortlist.objects.filter(order=(orderpk-2))[0]
            print(current_up_to_down.order)
            current_up_to_down.order+=1
            print(current_up_to_down.order)


        if action=="movedown":
            # current_up_to_down=Shortlist.objects.filter(order=orderpk-1)[0]
            # print(current_up_to_down.order)
            # current_up_to_down.order=min(current_up_to_down.order+1,Shortlist.objects.all().count())
            # print(current_up_to_down.order)
            # current_down_to_up=Shortlist.objects.filter(order=(orderpk))[0]
            # print(current_down_to_up.order)
            # current_down_to_up.order-=1
            # print(current_down_to_up.order)
            current_up_to_down=Shortlist.objects.filter(order=orderpk-1)[0]
            print(current_up_to_down.order)
            current_up_to_down.update(order=max(orderpk,Shortlist.objects.all().count()))
            print(current_up_to_down.order)
            current_down_to_up=Shortlist.objects.filter(order=(orderpk))
            print(current_down_to_up.order)
            current_down_to_up.update(order=min(orderpk-1,1))
            print(current_down_to_up.order)



        #shortlisted=Shortlist.objects.all()
        shortlisted=Shortlist.objects.order_by('order')
        return render(request,"schedule.html",{"shortlisted":shortlisted})
    else:
        shortlisted=Shortlist.objects.order_by('order')
        return render(request,"schedule.html",{"shortlisted":shortlisted})