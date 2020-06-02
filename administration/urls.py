from django.urls import path, include
from django.conf import settings
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'administration'

router = SimpleRouter()
router.register('course', views.CourseViewSet, basename='api-course')

urlpatterns = router.urls