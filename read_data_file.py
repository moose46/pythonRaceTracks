__author__ = 'Robert W. Curtiss'
__project__ = 'Python RaceTrack'

import csv
import os
from collections import namedtuple
from pathlib import Path

"""
====================================================
Author: Robert W. Curtiss
    Project: 
    File: read_data_file
    Created: May, 15, 2022
    
    Description:
        returns a list of named tuples for all the race dates
        for a track    
===================================================
"""


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
    race_track: str
    @property
    def year(self):
        """Race year"""
        return self._year

    def __repr__(self):
        return f'{self.race_track:12} - {self.driver} {self.pos}'


def read_the_race_data_file(data_file_name: Path, race_track: str) -> [DriverRaceResults]:
    """
    Gets all data for a track from the data/track name directory
    driver, car, manufacturer,laps,start,led,pts,bonus, penalty
    :param track_name:
    :return: list of DriverRaceResults
    """
    data: [DriverRaceResults] = list()
    if not os.path.isdir(data_file_name.parent):
        os.mkdir(data_file_name.parent)
    if not os.path.exists(data_file_name):
        return data
    with open(str(data_file_name), 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        row_data = namedtuple('result', next(reader), rename=True)
        for row in reader:
            results_data = row_data(*row)  # results_data is a tuple
            fc = DriverRaceResults()
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
            fc.race_track = race_track
            # results_data.BONUS = f.name[:4] # put the year in the bonus field
            data.append(fc)
    return data


# r = get_data()
# for x in r:
#     print(x)
