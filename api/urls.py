from django.urls import path, include
from rest_framework import routers
from api.views import MatchViewSet, GroundViewSet, SportViewSet

router = routers.DefaultRouter()
router.register('Match', MatchViewSet)
router.register('Ground', GroundViewSet)
router.register('Sport', SportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('match', include('rest_framework.urls', namespace='rest_framework')),
]
