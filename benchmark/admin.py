from django.contrib import admin
from .models import Bank, Indicator, DimDate

# Register your models here.
admin.site.register(Bank)
admin.site.register(Indicator)
admin.site.register(DimDate)