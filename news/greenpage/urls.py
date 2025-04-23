from django.urls import path
from greenpage import views

urlpatterns = [
    path('', views.about),
    path('test/', views.hello),
]