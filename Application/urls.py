from django.urls import path
from Application import views


urlpatterns = [
    path('', views.home),
    path('verifie_mail', views.verifie_mail),
    path('create_account', views.create_account)
]
