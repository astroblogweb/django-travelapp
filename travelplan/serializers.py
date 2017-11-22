from rest_framework import serializers
from .models import Traveller, Trip, Itinerary
# from django.contrib.auth.models import User, Group
from placesdata.models import Place


class TravellerSerializer(serializers.HyperlinkedModelSerializer):
    # trips=serializers.StringRelatedField(many=True)
    trips=serializers.HyperlinkedIdentityField(
        many=True, read_only=True, view_name='trip-detail')
    # trips=serializers.HyperlinkedIdentityField('trips',view_name='traveller-list', lookup_field='username')
    class Meta:
        model=Traveller
        fields=('traveller','followers','trips')


class TripSerializer(serializers.HyperlinkedModelSerializer):
    # author=TravellerSerializer(required=False)
    # itinerary=serializers.StringRelatedField(many=True)
    itinerary=serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='itinerary-detail')

    # following..
    # def get_validation_exclusions(self):
    #     exclusions=super(TripSerializer,self).get_validation_exclusions()
    #     return exclusions + ['author']
    class Meta:
        model=Trip
        # fields=('author','title','body','itinerary')
        fields=('title','body','itinerary')
        #depth=2


class ItinerarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Itinerary
        fields=('spot','title')#'__all__'
        # depth=2

# ModelSeri: no url, site_name="cyber hub"
# hyperlinkedModelSeri: url: http://127.0.0.1:8000/api/places-travelplan/Cyber%20Hub/
class PlacesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Place
        fields='__all__'



# class meta: model=.. fields=.., depth=2 : gives nested json.




# todo:...... 191117 https://coderwall.com/p/wrns8a/build-todo-list-with-angular-and-drf
# http://djangorestframework.readthedocs.io/en/latest/api-guide/relations/