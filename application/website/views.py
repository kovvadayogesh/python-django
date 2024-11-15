from django.shortcuts import render
from rest_framework import viewsets
from . models import Category,Product
from . serializers import ProductSerializer,CategorySerializer
# Create your views here.


class ProductDetails(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


