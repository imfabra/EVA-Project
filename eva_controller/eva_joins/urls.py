from django.urls import path
from . import views

urlpatterns = [
    path('joins/', views.joins, name='joins')
]