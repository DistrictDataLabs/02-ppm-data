#! /usr/bin/env python

import csv, sys

raw_data_file = sys.argv[1]
processed_data_file = sys.argv[2]

def read_funding_data(path):
    with open(path, 'rU') as data:
        reader = csv.DictReader(data)
        for row in reader:
            yield row

if __name__ == '__main__':

    output_header = "year,month"
    series_list = []

    output_dict = {}

    for idx, row in enumerate(read_funding_data(raw_data_file)):
        if idx > 13: break
        #print "Series: %(series)s, Year: %(year)s, January: %(jan)s" % row
        #print row

        series_name = row["series"]
        year = row["year"]

        if series_name not in series_list:
            series_list.append(series_name)

        output_dict["year"]["jan"][series_name] = row["jan"]
        output_dict["year"]["feb"][series_name] = row["Feb"]
        output_dict["year"]["mar"][series_name] = row["Mar"]
        output_dict["year"]["apr"][series_name] = row["Apr"]
        output_dict["year"]["may"][series_name] = row["May"]
        output_dict["year"]["jun"][series_name] = row["Jun"]
        output_dict["year"]["jul"][series_name] = row["Jul"]
        output_dict["year"]["aug"][series_name] = row["Aug"]
        output_dict["year"]["sep"][series_name] = row["Sep"]
        output_dict["year"]["oct"][series_name] = row["Oct"]
        output_dict["year"]["nov"][series_name] = row["Nov"]
        output_dict["year"]["dec"][series_name] = row["Dec"]

    series_header = ",".join(series_list)
    print output_header + "," + series_header
