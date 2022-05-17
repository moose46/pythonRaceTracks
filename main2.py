__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# main1.py was created on May 03 2022 @ 3:44 PM
# Project: pythonRaceTracks
# uses DriverResults from driver_results2.py
import collections
import csv
from collections import namedtuple
from operator import itemgetter
from collections import OrderedDict
from pathlib import Path
from driver_result2 import DriverResults, Result
file_path = Path.cwd() / "data"

top_finishers = []

top_finishers_all = collections.Counter
top_finishers_dict = collections.Counter
data_dict = []
startingPos = OrderedDict()
name = []
TOP_FINISH = 3
MOST_COMMON = 10
race_results = OrderedDict()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(name,file_path)
    for f in file_path.glob(f"{name}/*.txt"):
        with open(Path(f'{f.parent}/{f.name}'), 'r') as file:
            reader = csv.DictReader(file, delimiter='\t')
            for row in reader:
                if int(row['POS']) > 15: # only interested in the top 5 finishes
                    continue
                del row['LAPS']
                del row['LED']
                del row['BONUS']
                del row['PENALTY']
                del row['MANUFACTURER']
                del row['PTS']
                race_data = Result(f.name[:4],int(row['START']),int(row['POS']))
                driver = DriverResults(row['DRIVER'],row['CAR'],track=name)
                try: # add to the list
                    data = race_results[row['DRIVER']]
                    data.results.append(race_data)
                    pass
                except KeyError:  # init the list
                    driver.results.append(race_data)
                    race_results[row['DRIVER']] = driver
                    # print('~')

print_hi('darlington')

for r in sorted(race_results):
    x = race_results[r]
    if len(x.results) > 1:
        print(x)

def match_pos():
    results = []
    for result in race_results:
        r = race_results[result]
        match r:
            case DriverResults(driver='Erik Jones', track='darlington'):
                results.append(result)

        return results

print(match_pos())
#     # https://fedingo.com/how-to-search-item-in-list-of-dictionaries-in-python/
#     res = next((sub for sub in x.results if sub['DATE'] == '2021' or sub['DATE'] == '2020' or sub['DATE'] == '2019'), None)
#     res1 = [x for x in x.results]
#     if res:
#         print(f'{x.driver} {x.track} {res}')
#
# most_common = top_finishers_dict(race_results).most_common(10)
# print("-",most_common)