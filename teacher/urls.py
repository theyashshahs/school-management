from rest_framework.routers import SimpleRouter
from . import views

app_name = 'teacher'

router = SimpleRouter()
router.register('teacher', views.TeacherViewSet, basename='api-teacher')
router.register('assignment', views.AssignmentViewSet, basename='api-assignment')

urlpatterns = router.urls

