from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('product', ProductViewSet)
router.register('cart', CartViewSet)


urlpatterns = [
    path('', include(router.urls))
]