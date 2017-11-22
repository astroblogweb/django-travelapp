from rest_framework import serializers
from .models import ToDo, Place
from django.contrib.auth.models import User, Group



class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Place
        fields=('site_name', 'site_category','site_state','site_city_parent')


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     # url = serializers.HyperlinkedIdentityField(view_name="fortune:user-detail")
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')