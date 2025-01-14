from django.urls import path
from .views import llm03

urlpatterns = [
    path('', llm03, name='llm03'),
]
