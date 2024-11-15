from django.urls import path, include
from .views import ProductDetails
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'ProductDetails',ProductDetails,basename='ProductDetails')

urlpatterns = [
    path('',include(router.urls)),
]
