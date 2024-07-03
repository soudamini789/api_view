from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from app.models import *
from app.serilaization import *
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
def first(request):
    return Response({'msg':'hi'})

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def Studentdata(request):
    LSO=Student.objects,all
    MSSO=StudentMS(LSO,many=True)
    return Response(MSSO.data)