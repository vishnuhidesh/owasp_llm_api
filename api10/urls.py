from django.urls import path
from .views import llm10

urlpatterns = [
    path('', llm10, name='llm10'),
]
