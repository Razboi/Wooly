from django.conf.urls import url

from .views import AddToCart, CartDelete

urlpatterns = [
    url(r'^add/(?P<pk>\d+)/$', AddToCart.as_view(), name="create"),
    url(r'^delete/$', CartDelete.as_view(), name="delete"),

]
