#!/usr/bin/env python
import csv
import os.path

#config

#output directory
subdirectory = 'output'

#file type (txt or md)
file_type = 'md'

try:
    os.mkdir(subdirectory)
except Exception:
    pass

with open('reviews.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1
    for row in csv_reader:
        review_file_name = f'{row[0]} {row[1]} ({row[2]}).{file_type}'
        print(f'extracting review to {subdirectory}/{review_file_name}')
        review_file = open(os.path.join(subdirectory, review_file_name), 'w')
        review_file.write(f'{row[6]}')
        review_file.close()
        line_count += 1 
    print(f'Processed {line_count} reviews.')
