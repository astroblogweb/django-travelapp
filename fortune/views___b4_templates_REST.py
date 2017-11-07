from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
# import random
# import json
from .models import Fortune
from django.views.generic import View
# from django.core.serializers.json import DjangoJSONEncoder

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FortuneSerializer,UserSerializer, GroupSerializer

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

class FortuneList(View):  # not REST, just generic view
    def get(self,request,*args,**kwargs):
        return render_to_response("fortune_list.html",{"fortune":Fortune.objects.all()})
        #datavalue=random.sample(range(1, 100), 5)   #[1,1,10,1,4]
        #return render_to_response(,"fortune_list.html",{'data':json.dumps(list(datavalue),cls=DjangoJSONEncoder)})
        #return render_to_response("fortune_list.html",{'data':json.dumps(list(datavalue),cls=DjangoJSONEncoder)})


class FortuneAPIList(APIView):  # REST - view
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self,request):
        # get objects, serialize objects using Serializer, return/render
        fortune=Fortune.objects.all()
        serializer=FortuneSerializer(fortune, many=True)  #many=True:multiple
        return Response(serializer.data)

    def post(self,request):
        serializer = FortuneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer