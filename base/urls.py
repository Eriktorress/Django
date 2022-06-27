from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from gestor import views

router = routers.DefaultRouter()
router.register(r'Profesion', views.Profview,'Profesion')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('gestor.urls'))
]
