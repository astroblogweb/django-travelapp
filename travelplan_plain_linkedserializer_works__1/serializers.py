from rest_framework import serializers
from .models import Traveller, Trip, Itinerary
# from django.contrib.auth.models import User, Group

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


class ItinerarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Itinerary
        fields='__all__'


#  works:  url = serializers.HyperlinkedIdentityField(view_name="fortune:user-detail")



#     def _include_additional_options(self, *args, **kwargs):
#         return self.get_extra_kwargs()

#     def _get_default_field_names(self, *args, **kwargs):
#         return self.get_field_names(*args, **kwargs)


# class CustomDocumentSerializer(CustomModelSerializer, DocumentSerializer):
#     pass