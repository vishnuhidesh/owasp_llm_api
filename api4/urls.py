from django.urls import path
from .views import llm04

urlpatterns = [
    path('', llm04, name='llm04'),
]
