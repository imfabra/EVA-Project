from django.urls import path
from . import views

urlpatterns = [
    path('movimiento/',views.robot_motion_post, name='robot_motion_post')
]