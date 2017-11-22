from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .serializers import PlaceSerializer
# Create your views here.
from .models import State,Place,ToDo
from .scrapper import *
from .forms import StateForm
from rest_framework import viewsets
from rest_framework import permissions

#site_name,site_city_parent,site_link,site_rating,site_category,site_speciality

def placesdata(request):
    return render(request, 'places.html', {'places':Place.objects.all()})


def places_scrapper(request):
    if request.method=="POST":
        state_form=StateForm(request.POST)
#        print("yes POST.. checking for valid")
        if state_form.is_valid():
#            print("yes POST, yes valid")
#            print("if req.post is true..")
#            print("state_form:",state_form)
            state_add_location_for=state_form.cleaned_data['state_name']
#            print("\n\n\n",state_add_location_for,"\ncalling add_location function","\n\n\n")
            add_location(request,state_add_location_for,100)
        else:
            print("yes POST, not valid")
    else:
        print("request mtd: NOT POST")
    return render(request, 'places_scrapper.html', {'places':Place.objects.all()})
#    states=['meghalaya']
#    for state in states:
#        sites_df=choose_state(state)
#    return render(request, 'detail.html', {'article': article, 'title':title})
#    return HttpResponse("in places scrapper views")


def add_location(request,state,max_listing):  # size 1 (list)
#    print("inside add_location")
#    states=['meghalaya']
#    print("states:",states)
#    for state in states:
#        print("processing for state:",state)
#        sites_df=choose_state(state)

    sites_df=choose_state(state,max_listing)
#    short_df=sites_df[1:5]
    short_df=sites_df
    print("short_df:",short_df)
    for index, row in short_df.iterrows():
        new_place=Place()
        new_place.site_state=row['site_state']
        new_place.site_slug=row['site_slug']
        new_place.site_name=row['site_name']
        new_place.site_city_parent=row['site_city_parent']
        new_place.site_link=row['site_link']
        new_place.site_rating=row['site_rating']
        new_place.site_category=row['site_category']
        new_place.site_speciality=row['site_speciality']
        new_place.save()
#    return HttpResponse("done adding data to DB")
    print("success in form posting..")
#    return render(request, 'places_scrapper.html', {'places':Place.objects.all()})
    return render(request, 'places_scrapper.html', {'places':Place.objects.all()})





@login_required
def user_todo(request):
    todos = ToDo.objects.filter(user=request.user)
    places=Place.objects.all()
    print("in user_todo")
    return render(request, 'user_todo.html', {'todos' : todos,'places':places})


class PlaceViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Place.objects.all().order_by('-site_rating')
    serializer_class = PlaceSerializer
