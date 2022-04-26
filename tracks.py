__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# tracks.py was created on April 25 2022 @ 10:40 AM
# Project: pythonRaceTracks
# https://www.nascar.com/tracks/

from operator import itemgetter
INTERMEDIATE = 'Intermediate'
SUPERSPEEDWAY = 'Superspeedway'
SHORTTRACK = 'Short Track'
ROADCOURSE = 'Road Course'
SPEEDWAY = 'Speedway'

OVAL = 'Oval'
ROVAL = 'Roval'


tuple_track_data = [
    ('Atlanta Motor Speedway',1.540,INTERMEDIATE),
    ('Auto Club Speedway',2, SUPERSPEEDWAY),
    ('Bristol Motor Speedway',.533,SHORTTRACK),
    ('Bristol Motor Speedway Dirt',.533,SHORTTRACK),
    ('Charlotte Motor Speedway',1.5,INTERMEDIATE),
    ('Charlotte Motor Speedway Road Course',2.32, ROADCOURSE),
    ('Chicagoland Speedway',1.5, INTERMEDIATE),
    ('Circuit of The Americas',3.4,ROADCOURSE),
    ('Daytona Road Course',3.61,ROADCOURSE),
    ('Darlington Raceway',1.3,INTERMEDIATE),
    ('Daytona International Speedway',2.5,SUPERSPEEDWAY),
    ('Dover Motor Speedway',1,INTERMEDIATE),
    ('Eldora Speedway',.5,SHORTTRACK),
    ('Homestead-Miami Speedway',1.5,INTERMEDIATE),
    ('Indianapolis Motor Speedway',2.5,SPEEDWAY),
    ('Indianapolis Motor Speedway Road Course',2.439,ROADCOURSE),
    ('Iowa Speedway',.875,SHORTTRACK),
    ('Kansas Speedway',1.5,INTERMEDIATE),
    ('Kentucky Speedway',1.5,INTERMEDIATE),
    ('Knoxville Raceway',.5,SHORTTRACK),
    ('Las Vegas Motor Speedway',1.5,INTERMEDIATE),
    ('Los Angeles Memorial Coliseum', .25,SHORTTRACK),
    ('Martinsville Speedway', .526,SHORTTRACK),
    ('Michigan International Speedway', 2,INTERMEDIATE),
    ('Mid-Ohio Sports Car Course', 2.258,ROADCOURSE),
    ('Nashville Superspeedway', 1.333,INTERMEDIATE),
    ('New Hampshire Motor Speedway', 1.058,INTERMEDIATE),
    ('Phoenix Raceway', 1.0,INTERMEDIATE),
    ('Pocono Raceway', 2.5,SUPERSPEEDWAY),
    ('Richmond Raceway', .750,SHORTTRACK),
    ('Road America', 4.048, ROADCOURSE),
    ('Sonoma Raceway', 1.990,ROADCOURSE),
    ('Talladega Superspeedway', 2.660,SUPERSPEEDWAY),
    ('Texas Motor Speedway', 1.5,INTERMEDIATE),
    ('Watkins Glen International', 2.450,ROADCOURSE),
]

def get_tracks(ptrackType = INTERMEDIATE):
    """

    :param ptrackType: INTERMEDIATE, ROADCOURSE, SUPERSPEEDWAY
    :return: list of tracks of trakType
    """
    return [dict(track=x[0],length=x[1],trackType=x[2]) for x in tuple_track_data if x[2] == ptrackType]


tuple_tracks = [dict(track=x[0],length=x[1],trackType=x[2]) for x in tuple_track_data]
# print(tuple_tracks)
sorted_tuple_tracks = sorted(tuple_tracks,key=lambda item:item.get("length"))
f = itemgetter('length')
sorted_tuple_tracks1 = sorted(tuple_tracks,key=f)

print(get_tracks(ptrackType=INTERMEDIATE))
dict_track_data = {'Atlanta Motor Speedway': 1.540,
              'Auto Club Speedway': 2,
              'Bristol Motor Speedway': .533,
              'Bristol Motor Speedway Dirt': .533,
              'Charlotte Motor Speedway': 1.5,
              'Charlotte Motor Speedway Road Course': 2.32,
              'Chicagoland Speedway': 1.5,
              'Circuit of The Americas': 3.4,
              'Daytona Road Course': 3.61,
              'Darlington Raceway': 1.366,
              'Daytona International Speedway': 2.5,
              'Dover Motor Speedway': 1,
              'Eldora Speedway': .5,
              'Homestead-Miami Speedway': 1.5,
              'Indianapolis Motor Speedway': 2.5,
              'Indianapolis Motor Speedway Road Course': 2.439,
              'Iowa Speedway': .875,
              'Kansas Speedway': 1.5,
              'Kentucky Speedway': 1.5,
              'Knoxville Raceway': .5,
              'Las Vegas Motor Speedway': 1.5,
              'Los Angeles Memorial Coliseum': .25,
              'Martinsville Speedway': .526,
              'Michigan International Speedway': 2,
              'Mid-Ohio Sports Car Course': 2.258,
              'Nashville Superspeedway': 1.333,
              'New Hampshire Motor Speedway': 1.058,
              'Phoenix Raceway': 1.0,
              'Pocono Raceway': 2.5,
              'Richmond Raceway': .750,
              'Road America': 4.048,
              'Sonoma Raceway': 1.990,
              'Talladega Superspeedway': 2.660,
              'Texas Motor Speedway': 1.5,
              'Watkins Glen International': 2.450,
              }

tuple_sorted_tracks = {k:v for k,v in sorted(dict_track_data.items(),key=lambda item:item[1])}

# tracks = {length: track for track, length in track_data}
#


fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))
celsius_dict = dict(zip(fahrenheit.keys(), celsius))

l1 = []
d1 = dict(k=2,y=3)
l1.append(d1)
d1 = dict(Track="Bristol",Length=.533)

print(d1.keys())