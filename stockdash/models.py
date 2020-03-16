from django.db import models
class PriceHistory(models.Model):
    symbol = models.CharField(max_length=10, blank=True, null=True)
    date_traded = models.DateField(blank=True, null=True)
    open_price = models.FloatField(blank=True, null=True)
    high_price = models.FloatField(blank=True, null=True)
    low_price = models.FloatField(blank=True, null=True)
    close_price = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price_history'


class Return14Day(models.Model):
    symbol = models.CharField(max_length=10, primary_key=True)
    sector = models.CharField(max_length=200, blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    symbolname = models.CharField(max_length=200, blank=True, null=True)
    date_traded = models.DateField(blank=True, null=True)
    latest_close = models.FloatField(blank=True, null=True)
    prior_close = models.FloatField(blank=True, null=True)
    return_percentage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    timestamp_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_14_day'


class Return1Day(models.Model):
    symbol = models.CharField(max_length=10, primary_key=True)
    sector = models.CharField(max_length=200, blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    symbolname = models.CharField(max_length=200, blank=True, null=True)
    date_traded = models.DateField(blank=True, null=True)
    latest_close = models.FloatField(blank=True, null=True)
    prior_close = models.FloatField(blank=True, null=True)
    return_percentage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    timestamp_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_1_day'


class Return30Day(models.Model):
    symbol = models.CharField(max_length=10, primary_key=True)
    sector = models.CharField(max_length=200, blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    symbolname = models.CharField(max_length=200, blank=True, null=True)
    date_traded = models.DateField(blank=True, null=True)
    latest_close = models.FloatField(blank=True, null=True)
    prior_close = models.FloatField(blank=True, null=True)
    return_percentage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    timestamp_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_30_day'


class Return7Day(models.Model):
    symbol = models.CharField(max_length=10, primary_key=True)
    sector = models.CharField(max_length=200, blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    symbolname = models.CharField(max_length=200, blank=True, null=True)
    date_traded = models.DateField(blank=True, null=True)
    latest_close = models.FloatField(blank=True, null=True)
    prior_close = models.FloatField(blank=True, null=True)
    return_percentage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    timestamp_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_7_day'


class StockPriceHistory(models.Model):
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    open = models.FloatField(db_column='Open', blank=True, null=True)  # Field name made lowercase.
    high = models.FloatField(db_column='High', blank=True, null=True)  # Field name made lowercase.
    low = models.FloatField(db_column='Low', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(db_column='Close', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    symbol = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_price_history'


class Stockinfo(models.Model):
    stockinfo_id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=10, blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    symbolname = models.CharField(max_length=200, blank=True, null=True)
    sector = models.CharField(max_length=200, blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stockinfo'