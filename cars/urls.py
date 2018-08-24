from django.conf.urls import include, url
from rest_framework import routers

from cars import views

router = routers.DefaultRouter()
router.register(r'cars', views.CarViewSet)
router.register(r'manufacturers', views.ManufacturerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
