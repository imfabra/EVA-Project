from django.urls import path
from . import views

urlpatterns = [
    path('etiquetas/', views.etiqueta_list, name='etiqueta_list'),
    path('etiquetas/<int:etiqueta_id>/', views.etiqueta_detail, name='etiqueta_detail'),
    path('etiquetas/create/', views.etiqueta_create, name='etiqueta_create'),
    path('etiquetas/<int:etiqueta_id>/update/', views.etiqueta_update, name='etiqueta_update'),
    path('etiquetas/<int:etiqueta_id>/delete/', views.etiqueta_delete, name='etiqueta_delete'),

    path('movimientos/', views.movimiento_list, name='movimiento_list'),
    path('movimientos/<int:movimiento_id>/', views.movimiento_detail, name='movimiento_detail'),
    path('movimientos/create/', views.movimiento_create, name='movimiento_create'),

    path('submovimientos/', views.submovimiento_list, name='submovimiento_list'),
    path('submovimientos/<int:submovimiento_id>/', views.submovimiento_detail, name='submovimiento_detail'),
    path('submovimientos/create/', views.submovimiento_create, name='submovimiento_create'),
]
