from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='landing'),
    path('admin/', admin.site.urls, name='admin'),
    path('students/', include('student.urls', namespace='student')),
    path('teachers/', include('teacher.urls', namespace='teacher')),
    path('administration/', include('administration.urls', namespace='administration')),
    path('guardian/', include('guardian.urls', namespace='guardian')),
    path('auth/', include('authentication.urls', namespace='auth')),
    path('fees/', include('fees.urls', namespace='fees')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
