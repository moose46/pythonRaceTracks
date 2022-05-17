__author__ = 'Robert W. Curtiss'
__project__ = 'Python Basics'

"""
====================================================
Author: Robert W. Curtiss
    Project: 
    File: main3
    Created: May, 15, 2022
    
    Description: Returns a list of the TOP_FINISHERS for a track for all years available
    
===================================================
"""

import read_data_files as rdf

TOP_FINISHERS = 5

data = rdf.get_data('kansas')
year: str = '2016'

for d in data:
    # year = d.year if d.year == year else d.year

    if int(d.pos) <= TOP_FINISHERS:
        if year != d.year:
            print(f'==== {year} ====')
            year = d.year
        print(f'{d.pos:<2} {d.driver:20} ')
