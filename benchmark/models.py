from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField

# Create your models here.
class Bank(models.Model):
    OWNERSHIP = (
        ('1', 'Stated Owned Bank'),
        ('2', 'Regional Bank'),
        ('3', 'Private Forex Bank'),
        ('4', 'Private Non-Forex Bank'),
        ('5', 'Joint Venture Bank'),
        ('6', 'Foreign Bank'),
    )
    BUKU = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    institution_name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo', blank=True, null=True)
    tin = models.CharField(max_length=50, blank=True, null=True)
    est_date = models.DateField(blank=True, null=True)
    forex_date = models.DateField(blank=True, null=True)
    listing_date = models.DateField(blank=True, null=True)
    category = models.CharField(max_length=1, choices=OWNERSHIP, blank=True, null=True)
    group = models.CharField(max_length=1, choices=BUKU, blank=True, null=True)
    periods = models.ManyToManyField('benchmark.DimDate', through='Indicator')
    
    def __str__(self):
        return self.bank_name

class Contact(models.Model):
    bank = models.OneToOneField(Bank, on_delete=models.CASCADE, primary_key=True)
    building_name = models.CharField(max_length=50, blank=True, null=True)
    address_line = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    website = models.URLField(max_length=50, blank=True, null=True)
    swift_code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "%s Contact" % self.bank.bank_name
    
class Indicator(models.Model):
    bank = models.ForeignKey('benchmark.Bank', on_delete=models.CASCADE)
    period = models.ForeignKey('benchmark.DimDate', on_delete=models.CASCADE)
    pbt = MoneyField(max_digits=19, decimal_places=4, default_currency='IDR')
    funding = MoneyField(max_digits=19, decimal_places=4, default_currency='IDR')
    lending = MoneyField(max_digits=19, decimal_places=4, default_currency='IDR')
    asset = MoneyField(max_digits=19, decimal_places=4, default_currency='IDR')
    headcount = models.PositiveIntegerField()
    is_current = models.BooleanField(max_length=1, default=False)

    def __str__(self):
        return '%s at %s' % (self.bank, self.period.calendar_year_qtr)

class Executive(models.Model):
    TITLE = (
        ('1', 'President Director'),
        ('2', 'Head of Foreign Bank Branch'),
        ('3', 'Vice President Director'),
        ('4', 'Director'),
        ('5', 'Compliance Director'),
        ('6', 'Others Executive')
    )
    bank = models.ForeignKey('benchmark.Bank', on_delete=models.CASCADE)
    period = models.ForeignKey('benchmark.DimDate', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=1, choices=TITLE, default='6')
    report_to = models.ForeignKey('benchmark.Executive', on_delete=models.PROTECT, blank=True, null=True)
    photo = models.ImageField(upload_to='exec', blank=True, null=True)
    is_current = models.BooleanField(max_length=1, default=False)

    def __str__(self):
        return '%s of %s at %s' % (self.name, self.bank, self.period.calendar_year)

class DimDate(models.Model):
    full_date = models.DateField(default=timezone.now, null=True)
    date_name = models.CharField(max_length=11)
    date_name_us = models.CharField(max_length=11)
    date_name_eu = models.CharField(max_length=11)
    day_of_week = models.SmallIntegerField()
    day_name_of_week = models.CharField(max_length=11)
    day_of_month = models.SmallIntegerField()
    day_of_year = models. SmallIntegerField()
    weekday_weekend = models.CharField(max_length=11)
    week_of_year = models.SmallIntegerField()
    month_name = models.CharField(max_length=11)
    month_of_year = models.SmallIntegerField()
    is_last_day_of_month = models.CharField(max_length=1)
    calendar_quarter = models.SmallIntegerField()
    calendar_year = models.SmallIntegerField()
    calendar_year_month = models.CharField(max_length=11)
    calendar_year_qtr = models.CharField(max_length=11)
    fiscal_month_of_year = models.SmallIntegerField()
    fiscal_quarter = models.SmallIntegerField()
    fiscal_year = models.SmallIntegerField()
    fiscal_year_month = models.CharField(max_length=11)
    fiscal_year_qtr = models.CharField(max_length=11)

    def __str__(self):
        return self.date_name