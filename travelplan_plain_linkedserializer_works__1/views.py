from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .serializers import TravellerSerializer, TripSerializer, ItinerarySerializer
# Create your views here.
from .models import Traveller, Trip, Itinerary
# from .scrapper import *
# from .forms import StateForm
from rest_framework import viewsets
from rest_framework import permissions


@login_required
def user_todo(request):
    # users = Traveller.objects.filter(user=request.user)
    trips=Trip.objects.all()
    return render(request, 'user_todo.html', {'todos' : todos,'places':places})

def plan(request):
    return HttpResponse("in plan func")

class TravellerViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Traveller.objects.all()
    serializer_class = TravellerSerializer


class TripViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class ItineraryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer
