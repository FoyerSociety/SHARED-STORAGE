from django.urls import path
from Application import views


urlpatterns = [
    path('', views.home),
]