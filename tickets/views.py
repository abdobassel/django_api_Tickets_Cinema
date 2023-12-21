from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse 
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import status,filters
# Create your views here.

# 1 - json without rest framework
def noModelNoRest(request):
    geusts = [
        {
            "name":"abdo",
            'id':1,
            "num":'01111222',

        },{
            "name":"bassel",
            'id':2,
            "num":'012121245455',
        },
        
    ]

    return JsonResponse(geusts,safe=False)

# 2 - json with model and stil noo rest

def modelNoRest(request):
    model = Geust.objects.all()
    response = {"geusts":list(model.values('name','phone'))}

    return JsonResponse(response)
##### start rest ######
# 3 - Fbv with restframe work 
@api_view(['GET','POST'])
def FbvList(request):
    if request.method == 'GET':
        geusts = Geust.objects.all()
        serializer = GeustSerializer(geusts,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = GeustSerializer(data=request.data,)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

        