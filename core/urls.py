import django.conf
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url
from core.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', get_categories),
    path('tweeprints/', get_tweeprints),
    path('submit/', submit)

] + static(
    django.conf.settings.MEDIA_URL,
    document_root=django.conf.settings.MEDIA_ROOT
)
