from django.urls import path
from .views import llm08

urlpatterns = [
    path('', llm08, name='llm08'),
]
