from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers
from gestor import views

router = routers.DefaultRouter()
router.register(r'profesiones', views.Profview,'profesion')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('',include('gestor.urls')),

]
