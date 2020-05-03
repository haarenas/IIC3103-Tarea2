"""ApiHamburger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from burger_service import views

""" router = routers.DefaultRouter()
router.register('hamburguesas', views.HamburgesaViewSet)
router.register('ingredientes', views.IngredienteViewSet) """

urlpatterns = [
    #path('', include(router.urls)),
    #path('admin/', admin.site.urls),
    path('hamburguesa/', views.hamburgesaList.as_view()),
    path('hamburguesa', views.hamburgesaList.as_view()),
    path('hamburguesa/<pk>/', views.hamburgesaList.as_view()),
    path('hamburguesa/<pk>', views.hamburgesaList.as_view()),
    path('hamburguesa/<pk>/ingrediente/<pk2>/', views.hamburgesaIngrediente.as_view()),
    path('hamburguesa/<pk>/ingrediente/<pk2>', views.hamburgesaIngrediente.as_view()),
    path('ingrediente/', views.ingredienteList.as_view()),
    path('ingrediente', views.ingredienteList.as_view()),
    path('ingrediente/<pk>/', views.ingredienteList.as_view()),
    path('ingrediente/<pk>', views.ingredienteList.as_view()),
]
