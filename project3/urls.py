"""
URL configuration for project3 project.

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

from my_app1.views import *
""" or you can also write 
from my_app1.views import string_response, second_string, third_string 
each time one function you need you have to import from app views, so use universal operator which 
will allow to access all views created"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('string_response/', string_response, name='string_response'),
    path('second_string/', second_string, name='second_string'),
    path('third_string/', third_string, name='third_string'),
]
