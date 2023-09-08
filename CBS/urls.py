from django.contrib import admin
from django.urls import path
from CBS_manage import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("/", views.home),
]
