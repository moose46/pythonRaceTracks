# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import collections
import csv
import operator
from collections import namedtuple
from typing import NamedTuple
from operator import itemgetter
from collections import OrderedDict
from pathlib import Path
from typing import Any, Sequence

from driver_result_dataclasses import Result, DriverResults

file_path = Path.cwd() / 'data'

top_finishers = []
data = ''
top_finishers_all = collections.Counter
top_finishers_dict = collections.Counter
# data_dict = []
startingPos = OrderedDict()
name = [str]
TOP_FINISH = 3
MOST_COMMON = 10
TRACK = 'kansas'
race_results = []
# race_results = [DriverResults]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(name)
    for f in file_path.glob(f'{name}/*.txt'):
        with open(Path(f'{f.parent}/{f.name}'), 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            row_data = namedtuple('result', next(reader), rename=True)
            for row in reader:
                results_data = row_data(*row)   # results_data is a tuple
                data = DriverResults(
                    driver=results_data.DRIVER, car=results_data.CAR, track=name,manufacturer=results_data.MANUFACTURER
                )
                yup_nope = [x for x in race_results if x.driver == data.driver]
                if not len(
                    yup_nope
                ):   # add the driver and results to race_results if not found
                    data.results.append(
                        Result(
                            f.name[:4], results_data.START, results_data.POS
                        )
                    )
                    race_results.append(data)
                else:  # just add the results to the drivers data
                    x = yup_nope[0]
                    x.results.append(
                        Result(
                            f.name[:4], results_data.START, results_data.POS
                        )
                    )
                    data.best_finish()
                if int(results_data.POS) <= TOP_FINISH:
                    top_finishers.append(data.driver)
                # top_finishers_start.append(results_data[5])
                pass
    # for x in race_results:
    #     x.best_finish()
    xy = list(map(lambda x: x.best_finish(), race_results))
    print(type(race_results))
    for x in sorted(
        race_results, key=operator.attrgetter('best', 'best_year', 'driver', 'manufacturer')
    ):
        print(x)
    # sortedTop10 = top_finishers  # sort list by names
    #  get most common drivers and finish position in a list of tuples
    most_common = top_finishers_all(top_finishers).most_common(
        MOST_COMMON
    )  # returns tuples
    sortedStartingPos = dict(
        sorted(startingPos.items(), key=lambda item: item[0])
    )   # sort by names {'name' : {...}}
    # sortedStartingPos = startingPos # sort by names {'name' : {...}}
    # for x in most_common:  # list of tuples
    #     total = 0
    #     zz = sorted(sortedStartingPos.get(x[0]), key=lambda x: x['Finished'])
    #     for results in zz:
    #         total += results['Finished'] / len(zz)
    #     t = x + (total,)
    #     print(f'{x[0]:16} Avg Finish={total:.2f}',end=None)  # print driver name
    #     for y in zz:
    #         print(f'{y["date"]:>8} Start={y["Started"]:>4} Finished={y["Finished"]:>4}')


# print(top_finishers_dict( ('Bob','start' , 2, 'pos' , 3)))
print_hi(TRACK)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
