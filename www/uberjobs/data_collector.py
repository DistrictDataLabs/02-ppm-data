import requests
import json
import prettytable

class DataCollector:

    def __init__(self, data_url = 'http://api.bls.gov/publicAPI/v1/timeseries/data/'):
        self.data_url = data_url

    def collect_data(self, series_id, series_start_date, series_end_date):

        headers = {'Content-type': 'application/json'}
        data = json.dumps(
            {
                "seriesid": [series_id],
                "startyear": series_start_date.year, 
                "endyear": series_end_date.year
            }
        )

        p = requests.post(self.data_url, data=data, headers=headers)
        json_data = json.loads(p.text)
        return json_data