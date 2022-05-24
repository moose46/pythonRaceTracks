__author__ = 'Robert W. Curtiss'
__project__ = 'Python Basics'

from datetime import date
from pathlib import Path

"""
====================================================
Author: Robert W. Curtiss
    Project: 
    File: race_bet
    Created: May, 18, 2022
    
    Description:
    
===================================================
"""


class Bet:
    name: str = ''  # better name
    driver: str = ''  # race car driver name
    pos: int  # finish position
    beers: int = (
        0  # number of beers won, 2 for first place, 1 for placing higher
    )


class RaceBet:
    """
    format = racetrack, race date, bob, greg
    """

    race_track: str
    _date_of_race: date
    bob_selected: str
    greg_selected: str
    _bob_finish: int = -1
    _greg_finish: int = -1
    _data_file_name: str  # name of the data file
    bob_beers = 0
    greg_beers = 0

    def __init__(self):
        self._picks: [] = list()

    @property
    def picks(self):
        return self._picks

    @picks.setter
    def picks(self, value):
        self._picks.append(value)

    @property
    def bob_finish(self):
        return self._bob_finish

    @bob_finish.setter
    def bob_finish(self, pos: int):
        self._bob_finish = int(pos)
        if not self._greg_finish == -1:
            self.score()

    @property
    def greg_finish(self):
        return self._greg_finish

    @greg_finish.setter
    def greg_finish(self, pos: int):
        self._greg_finish = int(pos)
        if not self._bob_finish == -1:
            self.score()

    @property
    def date_of_race(self):
        """Race year"""
        return self._date_of_race

    def score(self):
        if self._greg_finish < self._bob_finish:
            self.greg_beers += 1
        else:
            self.bob_beers += 1
        if self._bob_finish == 1:
            self.bob_beers += 1
        if self._greg_finish == 1:
            self.greg_beers += 1

    @property
    def data_file_name(self) -> Path:
        self._data_file_name = self.date_of_race.strftime('%Y%m%d')

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
            f' greg={self.greg_beers} bob={self.bob_beers}'
            f' {self.picks}'
        )


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
