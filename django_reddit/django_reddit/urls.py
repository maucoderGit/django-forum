"""django_reddit URL Configuration"""
# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # FORUM
    path('', include('forum.urls')),
    path('users/', include('users.urls'))
    # USERS
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
