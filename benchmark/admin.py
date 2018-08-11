from django.contrib import admin
from .models import Bank, Financial, DimDate

# Register your models here.
admin.site.register(Bank)
admin.site.register(Financial)
admin.site.register(DimDate)