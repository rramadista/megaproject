from django.contrib import admin
from .models import Bank, Indicator, DimDate, Executive

# Register your models here.
admin.site.register(Bank)
admin.site.register(Indicator)
admin.site.register(DimDate)
admin.site.register(Executive)