from django.urls import path
from .views import llm09

urlpatterns = [
    path('', llm09, name='llm09'),
]
