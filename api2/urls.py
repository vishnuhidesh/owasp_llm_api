from django.urls import path
from .views import llm02

urlpatterns = [
    path('', llm02, name='llm02'),
]
