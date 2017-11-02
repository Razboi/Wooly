from django.conf.urls import url

from .views import AddToCart

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', AddToCart.as_view(), name="create"),

]