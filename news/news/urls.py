
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('about/', include('greenpage.urls')),
    path('next/', include('redpage.urls')),
]
