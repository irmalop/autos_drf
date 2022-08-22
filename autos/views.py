from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from .serializers import MarcaSerializer, AutoSerializer
from .models import Marca, Auto

class MarcaCreateAPIView(APIView):
    def post(self, request):
        serializer = MarcaSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MarcaListAPIView(APIView):
    permission_classes = (AllowAny, )
    def get(self, request):
        marca_list = Marca.objects.all()
        serializer = MarcaSerializer(marca_list, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AutoCreateAPIView(APIView):
    def post(self, request):
        serializer = AutoSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AutoListAPIView(APIView):
    permission_classes = (AllowAny, )
    def get(self, request):
        auto_list = Auto.objects.all()
        serializer = AutoSerializer(auto_list, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
