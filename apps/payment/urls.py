from django.conf.urls import url
from .views import PersonalView, FinancialView

urlpatterns = [
    url(r'^personal/$', PersonalView.as_view(), name="personal"),
    url(r'^financial/$', FinancialView.as_view(), name="financial"),

]
