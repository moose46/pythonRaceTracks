# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import collections
import csv
from collections import namedtuple
from operator import itemgetter
from pathlib import Path

file_path = Path.cwd() / "data"

top_10 = []
data = ""
top_10_all = collections.Counter
top_10_dict = collections.Counter
data_dict = []
startingPos = {}
name = []
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    for f in file_path.glob("dover/*.txt"):
        with open(Path(f'{f.parent}/{f.name}'), 'r') as file:
            reader = csv.reader(file,delimiter='\t')
            data = namedtuple("driver", next(reader), rename=True)
            for row in reader :
                driver = data(*row) # driver is a tuple
                # data_dict.append(dict(name=driver[1]))
                top_10.append(driver[1])
                # top_10_start.append(driver[5])
                if startingPos.get(driver[1]) == None:
                    startingPos[driver[1]] = [{'date': f.name[:4],'Started':driver[5], 'Finished': driver[0]}]  # 1st entry
                else:
                    name = startingPos[driver[1]].append({'date': f.name[:4],'Started':driver[5], 'Finished': driver[0]})# make a list of starting positions
                # if int(driver[0]) >= 10: # just get the top ten
                #     break
                pass
    most_common = top_10_all(top_10).most_common(5)
    for x in most_common:
        print(f'{x[0]:16} {startingPos.get(x[0])}')
    # print(top_10_dict( ('Bob','start' , 2, 'pos' , 3)))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
