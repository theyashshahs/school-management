from rest_framework.routers import SimpleRouter
from . import views

app_name = 'guardian'

router = SimpleRouter()
router.register('', views.GuardianViewSet, basename = 'api-guardian')

urlpatterns = router.urls