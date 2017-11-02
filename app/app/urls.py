from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('api.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^admin/', admin.site.urls),
]
