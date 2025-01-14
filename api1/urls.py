from django.urls import path
from .views import llm01

urlpatterns = [
    path('', llm01, name='llm01'),
]
