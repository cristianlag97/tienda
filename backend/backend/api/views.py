from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
# Create your views here.

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
# Create your views here.