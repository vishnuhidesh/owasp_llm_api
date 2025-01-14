from django.urls import path
from .views import llm07

urlpatterns = [
    path('', llm07, name='llm07'),
]
