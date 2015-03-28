from django.db import models

import datetime

# Create your models here.
class EconCategory(models.Model):
    category_name = models.CharField(max_length=200)
    category_desc = models.CharField(max_length=1000)

    def __unicode__(self):
        return unicode(self.category_name)

class EconSeries(models.Model):
    series_name = models.CharField(max_length=200)
    series_id = models.CharField(max_length=20)
    series_start_date = models.DateField(default=datetime.date(2004,1,1))
    series_end_date = models.DateField(default=datetime.date(2014,1,1))
    econ_category = models.ForeignKey(EconCategory)

    def __unicode__(self):
        return unicode(self.series_id)

class SeriesItem(models.Model):
    item_year = models.CharField(max_length=4)
    item_period = models.CharField(max_length=3)
    item_value = models.DecimalField(max_digits=12,decimal_places=4)
    item_normalized_value = models.DecimalField(max_digits=12,decimal_places=4)
    series = models.ForeignKey(EconSeries)

    def __unicode__(self):
        series_info = self.item_year + " " + self.item_period + ": " + self.item_value
        return unicode(series_info)

