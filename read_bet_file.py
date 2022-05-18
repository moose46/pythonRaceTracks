__author__ = 'Robert W. Curtiss'
__project__ = 'Python Basics'

import csv
from collections import namedtuple
from datetime import date
from pathlib import Path

import read_data_file
from models import RaceBet

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
        for row in reader:
            results_data = row_data(*row)  # results_data is a tuple
            bet = RaceBet()
            try:
                bet.race_track, bet.date_of_race, bet.greg_selected,  bet.bob_selected  = row_data(*row)
                data.append(bet)
            except:
                pass
                # print(f'****{data}')
    return data


bets = get_the_bets()
for bet in bets:
    d = read_data_file.read_the_race_data_file(bet)
    for i in d:
        print(i)
