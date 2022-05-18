__author__ = 'Robert W. Curtiss'
__project__ = 'Python RaceTrack'

import csv
import os
from collections import namedtuple
from pathlib import Path

from models import RaceBet, DriverRaceResults

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


def read_the_race_data_file(bet: RaceBet) -> [DriverRaceResults]:
    """
    Gets all data for a track from the data/track name directory
    driver, car, manufacturer,laps,start,led,pts,bonus, penalty
    :param track_name:
    :return: list of DriverRaceResults
    """
    data: [DriverRaceResults] = list()
    if not os.path.isdir(bet.data_file_name.parent):
        os.mkdir(bet.data_file_name.parent)
    if not os.path.exists(bet.data_file_name):
        return data
    with open(str(bet.data_file_name), 'r') as file:
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
            fc.race_track = bet.race_track
            # results_data.BONUS = f.name[:4] # put the year in the bonus field
            data.append(fc)
    return data


# r = get_data()
# for x in r:
#     print(x)
