from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'puntos', views.PuntosView, 'punto')
router.register(r'secuenciaps', views.SecuenciaPuntosView, 'secuenciaps')
router.register(r'secuenciacs', views.SecuenciaCombinadaView, 'secuenciacs')

#router.register(r'play', views.PuntoPlayPostView, 'puntoplay')

urlpatterns = [
    path('controller/crud/', include(router.urls)),

    path('controller/command/play/punto/', views.PuntoPlayPostView.as_view(), name='play-punto'),
    path('controller/command/play/zero/', views.GoZero.as_view(), name='play-zero'),
    path('controller/command/play/secuencia/', views.SecuenciaPlayPuntosView.as_view(), name='play-secuencia-puntos'),

    path('controller/docs/', include_docs_urls(title='Controller API Documentation'))
]
