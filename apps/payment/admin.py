from django.contrib import admin

from .models import UserPersonalModel, UserFinancialModel

admin.site.register(UserPersonalModel)
admin.site.register(UserFinancialModel)
