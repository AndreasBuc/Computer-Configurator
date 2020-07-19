from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cpu.api.views import AllCPUSIDSViewSet, AllCPUSViewSet
from graphic_card.api.views import (AllGraphic_CardsViewSet,
                                    AllGraphic_Card_IDSViewSet)
from software.api.views import (All_Games_ViewSet,
                                All_Games_IDs_ViewSet,
                                All_OfficeWare_ViewSet,
                                All_OfficeWare_IDs_ViewSet,
                                All_Operating_System_ViewSet,
                                All_Operating_System_IDs_ViewSet)
from configurator.api.views import (All_Configurator_Viewset,
                                    All_Configurator_Ids_Viewset,
                                    Users_Configurator_Viewset,
                                    Users_Configurator_Ids_Viewset,
                                    Users_Configurator_Add_Remove_Game_APIView,
                                    Users_Configurator_Add_Remove_OfficeWare_APIView
                                    )

router = DefaultRouter()
router.register('cpu',
                AllCPUSViewSet,
                basename='all-cpus')

router.register('cpu-ids',
                AllCPUSIDSViewSet,
                basename='all-cpus-ids')

router.register('graphic-cards',
                AllGraphic_CardsViewSet,
                basename='all-graphic-cards')

router.register('graphic-cards-ids',
                AllGraphic_Card_IDSViewSet,
                basename='all-graphic-cards-ids')

router.register('games',
                All_Games_ViewSet,
                basename='all-games')

router.register('games-ids',
                All_OfficeWare_ViewSet,
                basename='all-games-ids')

router.register('officewares',
                All_OfficeWare_IDs_ViewSet,
                basename='all-officewares')

router.register('officewares-ids',
                All_Games_IDs_ViewSet,
                basename='all-officeware-ids')

router.register('operating-systems',
                All_Operating_System_ViewSet,
                basename='all-operating-systems')

router.register('operating-systems-ids',
                All_Operating_System_IDs_ViewSet,
                basename='all-operating-systems-ids')

router.register('configurators',
                All_Configurator_Viewset,
                basename='configurators')

router.register('configurator-ids',
                All_Configurator_Ids_Viewset,
                basename='all-configurator-ids')

router.register('users-configurator',
                Users_Configurator_Viewset,
                basename='users-configurator')

router.register('user-configurator-ids',
                Users_Configurator_Ids_Viewset,
                basename='user-configurator-ids')


urlpatterns = [
    path('', include(router.urls)),
    path('add-or-remove-a-game/<int:g_pk>/<int:c_pk>/',
         Users_Configurator_Add_Remove_Game_APIView.as_view(),
         name="add-or-remove-a-game"),
    path('add-or-remove-a-officeware/<int:o_pk>/<int:c_pk>/',
         Users_Configurator_Add_Remove_OfficeWare_APIView.as_view(),
         name="add-or-remove-a-officeware"),
]
