from django.conf.urls import url

from .views import ProductsList, ProductSearch, IndexView, ProductDetails


urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^search$', ProductSearch.as_view(), name="search"),
    url(r'^(?P<category>[\w-]+)/$', ProductsList.as_view(), name="category"),
    url(r'^details/(?P<slug>[\w-]+)/$', ProductDetails.as_view(), name="details"),

]
