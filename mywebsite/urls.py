# mywebsite/urls.py

from django.contrib import admin
from django.urls import path

# ────────────────────────────── Option A (class-based)
from core.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),   # ← .as_view() is required!
]

