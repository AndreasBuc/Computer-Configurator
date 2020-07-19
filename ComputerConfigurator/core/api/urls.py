from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cpu.api.views import AllCPUSIDSViewSet, AllCPUSViewSet
from graphic_card.api.views import (AllGraphic_CardsViewSet,
                                    AllGraphic_Card_IDSViewSet)

router = DefaultRouter()
router.register('cpu/', AllCPUSViewSet, basename='all-cpus')
router.register('cpu-ids/', AllCPUSIDSViewSet, basename='all-cpus-ids')
router.register('graphic-cards', AllGraphic_CardsViewSet, basename='all-graphic-cards')
router.register('graphic-cards-ids', AllGraphic_Card_IDSViewSet, basename='all-graphic-cards-ids')

urlpatterns = [
    path('', include(router.urls))
]
