from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("chat/", include("djangoChannels.urls")),
    path("signals", include("signalsApp.urls")),
    path("admin/", admin.site.urls),
]
