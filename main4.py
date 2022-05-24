import glob

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
__project__ = 'pythonRaceTracks'

import csv
import os
from collections import namedtuple
from pathlib import Path

from models import RaceBet, DriverRaceResults

import csv
from collections import namedtuple
from datetime import date
from pathlib import Path

from models import RaceBet

file_path = Path.cwd() / 'data'


def read_the_race_data_file(bet: RaceBet) -> None:
    """
    Gets all data for a track from the data/track name directory
    driver, car, manufacturer,laps,start,led,pts,bonus, penalty
    :param bet:
    :param track_name:
    :return: update the finishing position in the bet for Bob and Greg
    """
    # txt = glob.glob(str(bet.data_file_name))
    if not os.path.isdir(bet.data_file_name.parent):
        os.mkdir(bet.data_file_name.parent)
    if not os.path.exists(bet.data_file_name):
        return None
    with open(str(bet.data_file_name), 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        row_data = namedtuple('result', next(reader), rename=True)
        for row in reader:
            results_data = row_data(*row)  # results_data is a tuple
            race_results = DriverRaceResults()
            (
                race_results.pos,
                race_results.driver,
                race_results.car,
                race_results.manufacturer,
                _,
                _,
                _,
                _,
                _,
                _,
            ) = row_data(*row)
            race_results.race_track = bet.race_track
            if race_results.driver in bet.bob_selected:
                bet.bob_finish = race_results.pos

            if race_results.driver in bet.greg_selected:
                bet.greg_finish = race_results.pos



class Bets:

    def __init__(self):
        self.data: [RaceBet] = list()

    def read_the_bets_data_file(self, file_name: str = 'bets.txt') -> [RaceBet]:
        """
        Gets all data for a track from the data/track name directory
        driver, car, manufacturer,laps,start,led,pts,bonus, penalty
        :param track_name:
        :return: list of DriverRaceResults
        """
        with open(Path(f'{file_path}/{file_name}'), 'r') as file:
            reader = csv.reader(file, delimiter=',')
            row_data = namedtuple('bet', next(reader), rename=True)
            names = list(row_data._fields)
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
                    _, _, Greg, Bob = row_data(*row)
                    l = list()
                    for x in range(2, 4):
                        d = dict()
                        d1 = dict()
                        d1['DRIVER'] = row[x]
                        d1['POS'] = -1
                        d['NAME'] = names[x]
                        d['PICKS'] = d1
                        l.append(d)
                    bet.picks = l
                    self.data.append(bet)
                except:
                    pass
                    # print(f'****{data}')


bets = Bets()
bets.read_the_bets_data_file()  # get the bets from the csv file

for bet in bets.data:
    d = read_the_race_data_file(bet)  # hydrate (score) the bet results

for bet in bets.data:
    print(bet)
