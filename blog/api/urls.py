from rest_framework.routers import DefaultRouter
from .views import PostApi
from django.urls import path,include


router = DefaultRouter()
router.register('crud',PostApi,basename='post')

urlpatterns = [
    path('',include(router.urls)),
    path('',include('rest_framework.urls'))
]