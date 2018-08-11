from django.db import models
from django.utils import timezone

# Create your models here.
class Bank(models.Model):
    institution_name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    tin = models.CharField(max_length=50, blank=True, null=True)
    swift_code = models.CharField(max_length=50, blank=True, null=True)
    est_date = models.DateField(blank=True, null=True)
    forex_date = models.DateField(blank=True, null=True)
    listing_date = models.DateField(blank=True, null=True)
    website = models.CharField(max_length=100)
    
    def __str__(self):
        return self.bank_name

class Financial(models.Model):
    bank = models.ForeignKey('benchmark.Bank', on_delete=models.CASCADE)
    period = models.ForeignKey('benchmark.DimDate', on_delete=models.PROTECT)
    pbt = models.DecimalField(max_digits=20, decimal_places=2)
    asset = models.DecimalField(max_digits=20, decimal_places=2)
    funding = models.DecimalField(max_digits=20, decimal_places=2)
    lending = models.DecimalField(max_digits=20, decimal_places=2)
    pers_exp = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return '%s %d' % (self.period, self.bank)

class DimDate(models.Model):
    date = models.DateField(default=timezone.now)
    date_as_integer = models.IntegerField()
    month = models.SmallIntegerField()
    month_name = models.CharField(max_length=50)
    quarter = models.SmallIntegerField()
    quarter_name = models.CharField(max_length=10)
    year = models.SmallIntegerField()

    def __str__(self):
        return self.month_name