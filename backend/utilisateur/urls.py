from rest_framework.routers import DefaultRouter
from .views import (
    UtilisateurViewSet,
    SleepTrackerViewSet,
    AnalyseViewSet
)

router = DefaultRouter()
router.register('users', UtilisateurViewSet)
router.register('sleep', SleepTrackerViewSet)
router.register('analyse', AnalyseViewSet)

urlpatterns = router.urls