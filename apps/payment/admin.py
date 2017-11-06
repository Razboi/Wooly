from django.contrib import admin

from .models import UserPersonalModel, UserFinancialModel, UserOrder

admin.site.register(UserPersonalModel)
admin.site.register(UserFinancialModel)
admin.site.register(UserOrder)