# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import collections
import csv
from collections import namedtuple
from operator import itemgetter
from collections import OrderedDict
from pathlib import Path

file_path = Path.cwd() / "data"

top_finishers = []
data = ""
top_finishers_all = collections.Counter
top_finishers_dict = collections.Counter
data_dict = []
startingPos = OrderedDict()
name = []
TOP_FINISH = 3
MOST_COMMON = 10
TRACK = 'darlington'
race_results = []
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(name)
    for f in file_path.glob(f"{name}/*.txt"):
        with open(Path(f'{f.parent}/{f.name}'), 'r') as file:
            reader = csv.reader(file,delimiter='\t')
            data = namedtuple("result", next(reader), rename=True)
            for row in reader :

                driver_race_results = data(*row) # driver_race_results is a tuple
                race_results.append(driver_race_results)
                # data_dict.append(dict(name=driver_race_results[1]))
                if int(driver_race_results.POS) <= TOP_FINISH:
                    top_finishers.append(driver_race_results.DRIVER)
                # top_finishers_start.append(driver_race_results[5])
                if startingPos.get(driver_race_results.DRIVER) == None:
                    # create an entry for results
                    startingPos[driver_race_results.DRIVER] = [{'date': f.name[:4],'Started':int(driver_race_results.START), 'Finished': int(driver_race_results.POS)}]  # 1st entry
                else:
                    #  append and entry for this driver to the list of results
                    startingPos[driver_race_results.DRIVER].append({'date': f.name[:4],'Started':int(driver_race_results.START), 'Finished': int(driver_race_results.POS)})# make a list of starting positions
                    # sorted_list = [i for i in sorted(startingPos[driver_race_results.DRIVER],key='Finished')]
                    pass
                # if int(driver_race_results[0]) >= 10: # just get the top ten
                #     break
                pass

    for x in race_results:
        r = x._asdict()
        print(r['DRIVER'])
    # sortedTop10 = top_finishers  # sort list by names
    #  get most common drivers and finish position in a list of tuples
    most_common = top_finishers_all(top_finishers).most_common(MOST_COMMON)  # returns tuples
    sortedStartingPos = dict(sorted(startingPos.items(),key=lambda item: item[0])) # sort by names {'name' : {...}}
    # sortedStartingPos = startingPos # sort by names {'name' : {...}}
    for x in most_common:  # list of tuples
        total = 0
        zz = sorted(sortedStartingPos.get(x[0]), key=lambda x: x['Finished'])
        for results in zz:
            total += results['Finished'] / len(zz)
        t = x + (total,)
        print(f'{x[0]:16} Avg Finish={total:.2f}',end=None)  # print driver name
        for y in zz:
            print(f'{y["date"]:>8} Start={y["Started"]:>4} Finished={y["Finished"]:>4}')
# print(top_finishers_dict( ('Bob','start' , 2, 'pos' , 3)))
print_hi('darlington')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
