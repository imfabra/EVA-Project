from django.urls import path
from . import views

urlpatterns = [
    # path('movimiento/',views.robot_motion_post, name='robot_motion_post')
    path("movimiento/<str:motion>", views.robot_motion_post, name='robot_motion_post'),
    path("movimiento_zero/go_zero", views.robot_go_zero,name='robot_go_zero')
]