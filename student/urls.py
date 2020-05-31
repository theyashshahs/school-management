from rest_framework.routers import SimpleRouter
from . import views

app_name = 'student'

router = SimpleRouter()
router.register('student', views.StudentViewSet, basename = 'api-student')

urlpatterns = router.urls
