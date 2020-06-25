from rest_framework.routers import SimpleRouter
from . import views

app_name = 'auth'

router = SimpleRouter()
router.register('', views.AuthViewSet, basename='api-auth')

urlpatterns = router.urls