__author__ = 'Robert W. Curtiss'
__project__ = 'Python Basics'

import csv
from collections import namedtuple
from datetime import date
from pathlib import Path
import read_data_file

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


class RaceBet:
    """
    racetrack, race date, bob, greg,
    """

    race_track: str
    _date_of_race: date
    bob_selected: str
    greg_selected: str
    bob_finish: int = -1
    greg_finish: int = -1
    _data_file_name: str   # name of the data file

    @property
    def date_of_race(self):
        """Race year"""
        return self._date_of_race

    @property
    def data_file_name(self) -> Path:
        self._data_file_name = self._date_of_race.strftime('%Y%m%d')

        the_path = (
            Path.cwd()
            / 'data'
            / f'{self.race_track}'
            / f'{self._data_file_name}.txt'
        )
        return the_path

    @date_of_race.setter
    def date_of_race(self, d):
        """Expected format: month/day/year"""
        month, day, year = d.split('/')
        self._date_of_race = date(int(year), int(month), int(day))

    def __repr__(self):
        return (
            f'{self.race_track.upper():<12} {self.date_of_race.strftime("%m/%d/%Y"):<10}'
            f' BOB: {self.bob_finish:<2} {self.bob_selected.capitalize():16}'
            f' GREG: {self.greg_finish:<2} {self.greg_selected.capitalize():16}'
            f' fname={self.data_file_name}'
        )


def get_data(file_name: str = 'bets.txt') -> [RaceBet]:
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
            (
                bet.race_track,
                bet.date_of_race,
                bet.greg_selected,
                bet.bob_selected,
            ) = row_data(*row)
            data.append(bet)
    return data


r = get_data()
for x in r:
    d = read_data_file.read_the_data_file(data_file_name=x.data_file_name)
    for i in d:
        print(i)
