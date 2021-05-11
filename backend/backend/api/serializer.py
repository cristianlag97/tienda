from rest_framework import serializers
from .models import *
# Serializers define the API representation.
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'id', 'title', 'description', 'image', 'price']