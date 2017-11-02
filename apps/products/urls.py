from django.conf.urls import url

from .views import ProductsList, ProductSearch, IndexView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^search/$', ProductSearch.as_view(), name='search'),
    url(r'^(?P<category>[\w-]+)$', ProductsList.as_view(), name='category'),

]
