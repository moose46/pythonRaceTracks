__author__ = 'Robert W. Curtiss'
__project__ = 'Python Basics'

"""
====================================================
Author: Robert W. Curtiss
    Project: 
    File: main3
    Created: May, 15, 2022
    
    Description:
    
===================================================
"""

import read_data_files as rdf


data = rdf.get_data('kansas')

for d in data:
    if int(d.finish) <= 2:
        print(d.driver,d.finish, d.year)
