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
    path('controller/', include(router.urls)),

    path('controller/play/', views.PuntoPlayPostView.as_view(), name='play'),
    path('controller/play/zero/', views.GoZero.as_view(), name='playzero'),
    path('controller/docs/', include_docs_urls(title='Controller API Documentation'))
]
