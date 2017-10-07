from django.contrib.auth import get_user_model
import json
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render_to_response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.serializers.json import DjangoJSONEncoder
# {# <!-- url-endpoint="{% url api-data %}"> --> #}

User=get_user_model()

class HomeView(View):
    def get(self,request,*args,**kwargs):
        #print("inside homeview")
        default_data={"datavalue":[1,2,3,4,5]}
        datalist={"datavalue":[1,2,3,4,5]}
        datavalue=[1,1,10,1,4];	
        #return render_to_response('charts_____backup_faulty.html')
        #return render_to_response("analysis.html")
        return render_to_response('charts_backup_5.html',{'data':json.dumps(list(datavalue),cls=DjangoJSONEncoder)})
#        return render_to_response('charts_backup_5.html',{'data':json.dumps(datalist)})



def get_data(request,*args,**kwargs):
    print("inside get_data/api-data")
    data={
        "sales":100,"customers":10,
    }
    return JsonResponse(data)



def get_data_api_data(request,*args,**kwargs):
    print("inside get_data/api-data")
    data={
        "sales":100,"customers":10,
    }
    return JsonResponse(data)

def analysis(request):
    return render_to_response("analysis.html")


#from rest_framework import authentication, permissions
#from django.contrib.auth.models import User

class ChartData(APIView):
    authentication_classes = []#(authentication.TokenAuthentication,)
    permission_classes =[]# (permissions.IsAdminUser,)
    def get(self, request, format=None):
        data={
        "sales":100,"customers":10,"users":User.objects.all().count(),
        }
        return Response(data)
