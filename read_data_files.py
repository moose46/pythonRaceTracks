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


class DriverRaceResults:
    """
    pos = finish position
    driver = diver name
    manufacturer = car manufacturer
    """
    def __init__(self, year: str = ''):
        self._year: str = year

    pos: int
    driver: str
    manufacturer: str
    car: int

    @property
    def year(self):
        """ Race year """
        return self._year


def get_data(track_name: str = 'kansas') -> [DriverRaceResults]:
    """
    Gets all data for a track from the data/track name directory
    driver, car, manufacturer,laps,start,led,pts,bonus, penalty
    :param track_name:
    :return: list of DriverRaceResults
    """
    data: [DriverRaceResults] = list()
    for f in file_path.glob(f'{track_name}/*.txt'):
        with open(Path(f'{f.parent}/{f.name}'), 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            row_data = namedtuple('result', next(reader), rename=True)
            year = f.name[:4]
            for row in reader:
                results_data = row_data(*row)  # results_data is a tuple
                fc = DriverRaceResults(year=year)
                (
                    fc.pos,
                    fc.driver,
                    fc.car,
                    fc.manufacturer,
                    _,
                    _,
                    _,
                    _,
                    _,
                    _,
                ) = row_data(*row)
                # results_data.BONUS = f.name[:4] # put the year in the bonus field
                data.append(fc)
    return data


# r = get_data()
# for x in r:
#     print(x)
