__author__ = 'Robert W. Curtiss'
__project__ = 'Python Basics'

import glob

"""
====================================================
Author: Robert W. Curtiss
    Project: 
    File: main4
    Created: May, 18, 2022
    
    Description:
    
===================================================
"""

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
__author__ = 'Robert W. Curtiss'
__project__ = 'Python Basics'

import csv
from collections import namedtuple
from datetime import date
from pathlib import Path

from models import RaceBet

file_path = Path.cwd() / 'data'


def read_the_race_data_file(bet: RaceBet) -> [DriverRaceResults]:
    """
    Gets all data for a track from the data/track name directory
    driver, car, manufacturer,laps,start,led,pts,bonus, penalty
    :param track_name:
    :return: list of DriverRaceResults
    """
    data: [DriverRaceResults] = list()
    # txt = glob.glob(str(bet.data_file_name))
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
            if fc.driver in bet.bob_selected:
                bet.bob_finish = fc.pos
            if fc.driver in bet.greg_selected:
                bet.greg_finish = fc.pos

    return data


def get_the_bets(file_name: str = 'bets.txt') -> [RaceBet]:
    """
    Gets all data for a track from the data/track name directory
    driver, car, manufacturer,laps,start,led,pts,bonus, penalty
    :param track_name:
    :return: list of DriverRaceResults
    """
    data: [RaceBet] = list()
    with open(Path(f'{file_path}/{file_name}'), 'r') as file:
        reader = csv.reader(file, delimiter=',')
        row_data = namedtuple('bet', next(reader), rename=True)
        names = list(row_data._fields)
        # print(names)
        # picks = list()
        # for x in names:
        #     d = dict()
        #     d[x] = ''
        #     d['DRIVER'] = 'Ricky Rudd'
        #     picks.append(d)
        # print(picks)
        # exit()
        for row in reader:
            results_data = row_data(*row)  # results_data is a tuple
            bet = RaceBet()
            try:
                (
                    bet.race_track,
                    bet.date_of_race,
                    bet.greg_selected,
                    bet.bob_selected,
                ) = row_data(*row)
                _,_,Greg,Bob = row_data(*row)
                l = list()
                for x in range(2,4):
                    d = dict()
                    d1 = dict()
                    d1['DRIVER'] = row[x]
                    d1['POS'] = -1
                    d['NAME'] = names[x]
                    d['PICKS'] = d1
                    l.append(d)
                bet.picks = l
                data.append(bet)
            except:
                pass
                # print(f'****{data}')
    return data


bets = get_the_bets()
for bet in bets:
    d = read_the_race_data_file(bet)
for bet in bets:
    print(bet)
