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
    results: list[Result] = field(default_factory=list)

    # def __str__(self):
    #     return f'{self.track} {self.driver} {self.results}'

    def __str__(self):
        res = []
        for r in self.results:
            value =  f"DATE={r.race_date} FINISH={r.finish:>2}"
            res.append(value)
        return f'{self.track.upper()} - {self.driver:<20} - {res}'

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
