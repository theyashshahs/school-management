from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='landing'),
    path('admin/', admin.site.urls),
    path('student/', include('student.urls', namespace='student')),
    # path('teacher/', include('teacher.urls', namespace='teacher')),
    # path('administration/', include('administration.urls', namespace='administration')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

