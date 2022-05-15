__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'

#
# Author: Robert W. Curtiss
# driver_result.py was created on May 04 2022 @ 8:30 AM
# Project: pythonRaceTracks
#
from dataclasses import dataclass, field, fields
from datetime import date
from typing import NamedTuple

@dataclass
class Result:
    race_date: str
    start: int
    finish: int


@dataclass
class DriverResults():
    driver: str  # driver name
    car: int  # car number
    track: str  # track name
    manufacturer: str = ''
    best_year: str = ''
    best: int = 100
    results: list[Result] = field(default_factory=list)
    def best_finish(self):
        for r in self.results:
            if int(r.finish) < self.best:
                self.best = int(r.finish)
                self.best_year = r.race_date
        return self.best

    def __str__(self):
        res = []
        for r in self.results:
            value =  f"DATE={r.race_date} FINISH={r.finish:>2}"
            res.append(value)
        return f'{self.track.upper()} {self.best_year:<4} - {self.best:<2} - {self.driver:<20} - {self.manufacturer:<12} {res}'

    def __repr__(self):
        cls = self.__class__
        cls_name = cls.__name__
        indent = ' ' * 4
        res = [f'{cls_name}(']
        for f in fields(cls):
            value = getattr(self, f.name)
            res.append(f'{indent}{f.name}={value}')
        res.append(')')
        return '\n'.join(res)
