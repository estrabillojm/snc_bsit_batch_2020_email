from django.contrib import admin
from django.urls import path, include
from content import views as content_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', content_views.content_create),
    path('snc-bsit/', include('content.urls')),
]

urlpatterns += staticfiles_urlpatterns()