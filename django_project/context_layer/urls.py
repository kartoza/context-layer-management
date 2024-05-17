# coding=utf-8

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from context_layer.api.layer import LayerViewSet
from context_layer.api.vector_tile import (VectorTileLayer)

router = DefaultRouter()
router.register(r'layer', LayerViewSet, basename='layer-view-set')

urlpatterns = [
    path(
        '<str:identifier>/tile/<int:z>/<int:x>/<int:y>/',
        VectorTileLayer.as_view(),
        name='layer-tile-api'
    ),
    path('api/', include(router.urls)),
]
