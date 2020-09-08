from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# django rest framework -> routet -> url

router = DefaultRouter()
router.register('post', views.PostViewset)

urlpatterns = [
    path('', include(router.urls)),
]