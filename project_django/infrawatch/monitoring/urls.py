from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import NodeViewSet, MetricViewSet

router=DefaultRouter()
router.register(r'nodes',NodeViewSet)
router.register(r'metric',MetricViewSet)

urlpatterns=[
    path('',include(router.urls))
]