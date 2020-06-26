from rest_framework.routers import SimpleRouter
from . import views

app_name = 'fees'

router = SimpleRouter()
router.register('', views.FeeViewSet, basename='api-fees')

urlpatterns = router.urls