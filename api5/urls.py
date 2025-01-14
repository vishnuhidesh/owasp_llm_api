from django.urls import path
from .views import llm05

urlpatterns = [
    path('', llm05, name='llm05'),
]
