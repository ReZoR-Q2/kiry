from django.urls import path
from redpage import views

urlpatterns = [
    path('', views.next),
]
