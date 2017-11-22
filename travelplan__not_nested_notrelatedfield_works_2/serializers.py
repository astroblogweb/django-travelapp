from rest_framework import serializers
from .models import Traveller, Trip, Itinerary
# from django.contrib.auth.models import User, Group
from placesdata.models import Place


class TravellerSerializer(serializers.HyperlinkedModelSerializer):
    # trips=serializers.HyperlinkedIdentityField(view_name='travelplan:traveller-detail', lookup_field='traveller')
    # trips=serializers.HyperlinkedIdentityField('trips',view_name='traveller-list', lookup_field='username')
    class Meta:
        model=Traveller
        fields='__all__'


class TripSerializer(serializers.HyperlinkedModelSerializer):
    # author=TravellerSerializer(required=False)
    # itinerary=serializers.HyperlinkedIdentityField(view_name='trips-list')
    # itinerary=serializers.HyperlinkedIdentityField('itinerary',view_name='trips-list')

    # following..
    # def get_validation_exclusions(self):
    #     exclusions=super(TripSerializer,self).get_validation_exclusions()
    #     return exclusions + ['author']
    class Meta:
        model=Trip
        fields='__all__'
        # depth=2


class ItinerarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Itinerary
        fields='__all__'
        # depth=2

# ModelSeri: no url, site_name="cyber hub"
# hyperlinkedModelSeri: url: http://127.0.0.1:8000/api/places-travelplan/Cyber%20Hub/
class PlacesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Place
        fields='__all__'



# class meta: model=.. fields=.., depth=2 : gives nested json.