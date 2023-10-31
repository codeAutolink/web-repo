from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('utilisateurs/', include('django.contrib.auth.urls')),
    path('', include('utilisateurs.urls')),
]
