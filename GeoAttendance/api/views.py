from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserData
from .serializers import serializer

@api_view()
def get_data(request):
    queryset = UserData.objects.all()
    serial = serializer(queryset)
    return Response({
        "data":serial.data
    })
