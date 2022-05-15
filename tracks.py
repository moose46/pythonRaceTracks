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
ROAD_COURSE = 'Road Course'
SPEEDWAY = 'Speedway'

CONCRETE_OVAL = 'Concrete Oval'
CONCRETE_TRI_OVAL = 'Concrete Tri Oval'
STADIUM_OVAL = 'Stadium Oval'
CLASSIC_OVAL = 'Classic Oval'
PAPER_CLIP_OVAL = 'Paper Clip Oval'
DOG_LEG_OVAL = 'Dog Leg Oval'
TRI_OVAL = 'Tri Oval'
DIRT_OVAL = 'Dirt Oval'
ROVAL = 'Roval'
QUAD_OVAL = 'Quad Oval'
D_SHAPED_OVAL = 'D-Shaped Oval'
EGG_SHAPED_OVAL = 'Egg Shaped Oval'
TRIANGULAR_SHAPED_OVAL = 'Triangular Shaped Oval'
tuple_track_data = [
    ('Atlanta Motor Speedway',1.540,INTERMEDIATE,QUAD_OVAL),
    ('Auto Club Speedway',2, SUPERSPEEDWAY,D_SHAPED_OVAL),
    ('Bristol Motor Speedway',.533,SHORTTRACK,CONCRETE_OVAL),
    ('Bristol Motor Speedway Dirt',.533,SHORTTRACK,DIRT_OVAL),
    ('Charlotte Motor Speedway',1.5,INTERMEDIATE,QUAD_OVAL),
    ('Charlotte Motor Speedway Road Course',2.32, ROAD_COURSE,ROAD_COURSE),
    ('Chicagoland Speedway',1.5, INTERMEDIATE,TRI_OVAL),
    ('Circuit of The Americas',3.4,ROAD_COURSE,ROAD_COURSE),
    ('Daytona Road Course',3.61,ROAD_COURSE,ROAD_COURSE),
    ('Darlington Raceway',1.3,INTERMEDIATE,EGG_SHAPED_OVAL),
    ('Daytona International Speedway',2.5,SUPERSPEEDWAY,TRI_OVAL),
    ('Dover Motor Speedway',1,INTERMEDIATE,CONCRETE_OVAL),
    ('Eldora Speedway',.5,SHORTTRACK,SHORTTRACK),
    ('Homestead-Miami Speedway',1.5,INTERMEDIATE,CLASSIC_OVAL),
    ('Indianapolis Motor Speedway',2.5,SPEEDWAY,PAPER_CLIP_OVAL),
    ('Indianapolis Motor Speedway Road Course',2.439,ROAD_COURSE,ROAD_COURSE),
    ('Iowa Speedway',.875,SHORTTRACK,CLASSIC_OVAL),
    ('Kansas Speedway',1.5,INTERMEDIATE,TRI_OVAL),
    ('Kentucky Speedway',1.5,INTERMEDIATE,TRI_OVAL),
    ('Las Vegas Motor Speedway',1.5,INTERMEDIATE,TRI_OVAL),
    ('Los Angeles Memorial Coliseum', .25,SHORTTRACK,STADIUM_OVAL),
    ('Martinsville Speedway', .526,SHORTTRACK,PAPER_CLIP_OVAL),
    ('Michigan International Speedway', 2,INTERMEDIATE,D_SHAPED_OVAL),
    ('Mid-Ohio Sports Car Course', 2.258,ROAD_COURSE,ROAD_COURSE),
    ('Nashville Superspeedway', 1.333,INTERMEDIATE,CONCRETE_TRI_OVAL),
    ('New Hampshire Motor Speedway', 1.058,INTERMEDIATE,PAPER_CLIP_OVAL),
    ('Phoenix Raceway', 1.0,INTERMEDIATE,DOG_LEG_OVAL),
    ('Pocono Raceway', 2.5,SUPERSPEEDWAY,TRIANGULAR_SHAPED_OVAL),
    ('Richmond Raceway', .750,SHORTTRACK,D_SHAPED_OVAL),
    ('Road America', 4.048, ROAD_COURSE,ROAD_COURSE),
    ('Sonoma Raceway', 1.990,ROAD_COURSE,ROAD_COURSE),
    ('Talladega Superspeedway', 2.660,SUPERSPEEDWAY,TRI_OVAL),
    ('Texas Motor Speedway', 1.5,INTERMEDIATE,QUAD_OVAL),
    ('Watkins Glen International', 2.450,ROAD_COURSE,ROAD_COURSE),
]

def get_tracks(ptrackType = INTERMEDIATE):
    """

    :param ptrackType: INTERMEDIATE, ROADCOURSE, SUPERSPEEDWAY
    :return: list of tracks of trakType
    """
    # sorted_tuple_tracks = sorted(tuple_tracks, key=lambda item: item.get("length"))
    return [dict(track=x[0],miles=x[1],trackType=x[2],configuration=x[3]) for x in tuple_track_data if x[2] == ptrackType]


# tuple_tracks = [dict(track=x[0],length=x[1],trackType=x[2]) for x in tuple_track_data]
print(get_tracks())
# f = itemgetter('length')
# sorted_tuple_tracks1 = sorted(tuple_tracks,key=f)

