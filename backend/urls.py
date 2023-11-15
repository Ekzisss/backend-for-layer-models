from django.contrib import admin
from django.urls import path
import backend.links as links

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', links.main)
]
