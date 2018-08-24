from django.conf.urls import include, url
from django.contrib import admin

from cars import urls

urlpatterns = [
    url(r'^api/(?P<version>(v1))/', include(urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
