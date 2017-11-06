from django.conf.urls import url
from .views import PersonalView, FinancialView, ConfirmationView, CompletePaymentView

urlpatterns = [
    url(r'^personal/$', PersonalView.as_view(), name="personal"),
    url(r'^financial/$', FinancialView.as_view(), name="financial"),
    url(r'^confirmation/$', ConfirmationView.as_view(), name="confirmation"),
    url(r'^complete/$', CompletePaymentView.as_view(), name="complete"),

]
