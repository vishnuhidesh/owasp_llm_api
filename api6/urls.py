from django.urls import path
from .views import llm06

urlpatterns = [
    path('', llm06, name='llm06'),
]
