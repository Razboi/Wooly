from django.conf.urls import url

from .views import ProductsList


urlpatterns = [
    url(r'^$', ProductsList.as_view(), name='category'),
]
