__author__ = 'Robert W. Curtiss'
__project__ = 'Python Basics'

import csv
from collections import namedtuple
from pathlib import Path

"""
====================================================
Author: Robert W. Curtiss
    Project: 
    File: read_data_files
    Created: May, 15, 2022
    
    Description:
        returns a list of named tuples for all the race dates
        for a track    
===================================================
"""
file_path = Path.cwd() / 'data'

finish = namedtuple('finish',"POS DRIVER CAR MANUFACTURER LAPS START LED PTS BONUS PENALTY")

def get_data(track_name: str = 'kansas') -> [namedtuple]:
    """
    Gets all data for a track from the data/track name directory
    driver, car, manufacturer,laps,start,led,pts,bonus, penalty
    :param track_name:
    :return: list of named tuples
    """
    cooked = namedtuple("data","driver finish year")
    data = list()
    for f in file_path.glob(f'{track_name}/*.txt'):
        with open(Path(f'{f.parent}/{f.name}'), 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            row_data = namedtuple('result', next(reader), rename=True)
            for row in reader:
                year = f.name[:4]
                results_data = row_data(*row)  # results_data is a tuple
                finish = row_data(*row)
                # results_data.BONUS = f.name[:4] # put the year in the bonus field
                final_data = cooked(driver=results_data.DRIVER,
                                    finish=int(results_data.POS),
                                    year=year,
                                    )
                data.append(final_data)
    return data

# r = get_data()
# for x in r:
#     print(x)