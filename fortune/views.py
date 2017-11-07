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
from rest_framework.renderers import TemplateHTMLRenderer

class FortuneList(View):  # not REST, just generic view
    def get(self,request,*args,**kwargs):
        return render_to_response("fortune_list.html",{"fortune":Fortune.objects.all()})
        #datavalue=random.sample(range(1, 100), 5)   #[1,1,10,1,4]
        #return render_to_response(,"fortune_list.html",{'data':json.dumps(list(datavalue),cls=DjangoJSONEncoder)})
        #return render_to_response("fortune_list.html",{'data':json.dumps(list(datavalue),cls=DjangoJSONEncoder)})


class FortuneAPIList_template(APIView):  # REST - view
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "fortune_list_REST.html"
    def get(self,request):
        # get objects, serialize objects using Serializer, return/render
        fortune=Fortune.objects.all()
        return Response({'fortune':fortune})
        # serializer=FortuneSerializer(fortune, many=True)  #many=True:multiple
        # return Response(serializer.data)
    def post(self,request):
        serializer = FortuneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FortuneAPIDetail_template(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'fortune_list_REST.html'

    def get(self, request, pk):
        fortune = get_object_or_404(Fortune, pk=pk)
        serializer = FortuneSerializer(fortune)
        return Response({'serializer': serializer, 'fortune': fortune})

    def post(self, request, pk):
        fortune = get_object_or_404(Fortune, pk=pk)
        serializer = FortuneSerializer(fortune, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'fortune': fortune})
        serializer.save()
        return redirect('fortune_api-list-template')


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


class FortuneViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # GET for all, POST for authenticated users
    queryset = Fortune.objects.all().order_by('-value')
    serializer_class = FortuneSerializer


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # GET for all, POST for authenticated users
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # GET for all, POST for authenticated users
    queryset = Group.objects.all()
    serializer_class = GroupSerializer