#! /usr/bin/env python

import csv, sys

raw_data_file = sys.argv[1]
processed_data_file = sys.argv[2]

if __name__ == '__main__':

    with open(raw_data_file, 'rU') as f_in, open(processed_data_file, 'w') as f_out:
        
        reader = csv.reader(f_in, quoting = csv.QUOTE_MINIMAL)
        writer = csv.writer(f_out, quoting = csv.QUOTE_MINIMAL, lineterminator = '\n')
        
        header = reader.next()

        for row in reader:
            
            for i in range(1, len(row)):

                # print i, row[i]
                writer.writerow([row[i]])






