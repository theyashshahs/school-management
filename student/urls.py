from rest_framework.routers import SimpleRouter
from . import views

app_name = 'student'

router = SimpleRouter()
router.register('student', views.StudentViewSet, basename = 'api-student')
router.register('answer', views.AnswerViewSet, basename = 'api-answer')

urlpatterns = router.urls
