"""
URL configuration for owasp_llm_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/allchallenges', views.allchallenges, name='allchallenges'),
    path('api/llm01/', include('api1.urls')),
    path('api/llm02/', include('api2.urls')),
    path('api/llm03/', include('api3.urls')),
    path('api/llm04/', include('api4.urls')),
    path('api/llm05/', include('api5.urls')),
    path('api/llm06/', include('api6.urls')),
    path('api/llm07/', include('api7.urls')),
    path('api/llm08/', include('api8.urls')),
    path('api/llm09/', include('api9.urls')),
    path('api/llm10/', include('api10.urls')),
]
