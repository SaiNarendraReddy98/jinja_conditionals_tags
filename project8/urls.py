"""
URL configuration for project8 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('if_condition/',if_condition,name='if_conditions'),
    path('if_else/',if_else,name='if_else'),
    path('if_elif/',if_elif,name='if_elif'),
    path('nested_if/',nested_if,name='nested_if'),
    
]
