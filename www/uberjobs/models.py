from django.db import models
from django.db.models import Avg
from django.db.models import StdDev

from uberjobs.data_collector import DataCollector

import datetime, collections
from math import sqrt

# Create your models here.
class EconCategory(models.Model):
    category_id = models.IntegerField(default=1)
    category_name = models.CharField(max_length=200)
    category_desc = models.CharField(max_length=1000)

    def __unicode__(self):
        return unicode(self.category_name)

class EconSeries(models.Model):
    series_name = models.CharField(max_length=200)
    series_id = models.CharField(max_length=20)
    series_start_date = models.DateField(default=datetime.date(2004,1,1))
    series_end_date = models.DateField(default=datetime.date(2015,1,1))
    econ_category = models.ForeignKey(EconCategory)
    data_table = None
    series_average = 0
    series_stdev = 0

    def __unicode__(self):
        return unicode(self.series_id)

    def get_data(self):
        series_data_dict = {}

        if self.seriesitem_set.count() == 0:
            dc = DataCollector()
            self.download_data(dc)
            self.save_data()
            self.normalize_data()

        for item in self.seriesitem_set.all().order_by('item_year'):
            date_id = item.item_year + "-" + item.item_period[-2:]
            series_data_dict[date_id] = item.item_normalized_value

        return collections.OrderedDict(sorted(series_data_dict.items()))

    def get_raw_data(self):
        series_data_dict = {}

        if self.seriesitem_set.count() == 0:
            dc = DataCollector()
            self.download_data(dc)
            self.save_data()
            self.normalize_data()

        for item in self.seriesitem_set.all().order_by('item_year'):
            date_id = item.item_year + "-" + item.item_period[-2:]
            series_data_dict[date_id] = item.item_value

        return collections.OrderedDict(sorted(series_data_dict.items()))

    def download_data(self, data_collector):
        api_results = data_collector.collect_data(
            self.series_id, 
            self.series_start_date, 
            self.series_end_date)
        self.data_table = api_results['Results']['series'][0]

    def save_data(self):
        if self.data_table is not None:
            for item in self.data_table['data']:
                if self.seriesitem_set.filter(item_year=item['year']).filter(item_period=item['period']).count() == 0:

                    series_item = self.seriesitem_set.create(
                        item_year=item['year'], 
                        item_period=item['period'], 
                        item_value=item['value'])
                    series_item.save()

    def normalize_data(self):
        if self.seriesitem_set.count() > 0:
            
            # First get the series average
            self.series_average = self.seriesitem_set.all().aggregate(Avg('item_value'))['item_value__avg']

            # Second get the series standard deviation
            sum_of_squares = 0
            for series_item in self.seriesitem_set.all():
                sum_of_squares += pow( series_item.item_value - self.series_average , 2)
            self.series_stdev = sqrt(sum_of_squares/self.seriesitem_set.count())

            # Third, normalize data
            for series_item in self.seriesitem_set.all():
                series_item.item_normalized_value = (series_item.item_value - self.series_average)/self.series_stdev
                series_item.save()

class SeriesItem(models.Model):
    item_year = models.CharField(max_length=4)
    item_period = models.CharField(max_length=3)
    item_value = models.FloatField()
    item_normalized_value = models.FloatField(default=0)
    series = models.ForeignKey(EconSeries)

    def __unicode__(self):
        series_info = self.item_year + " " + self.item_period + ": " + str(self.item_value)
        return unicode(series_info)

