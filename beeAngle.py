#USE : python beeAngle.py (t) (angle) (csvfile) (outputfile-optional)



#imports

import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import sys

#function
## Look at events prior and classify based on y displacement


def beeCleanAngle(bee):

    ids = []
    new_event = []
    datetime = []
    first_detection = 0
    
    enter_min = 180 + angle
    enter_max = 360 - angle
    exit_min = angle
    exit_max = 180 - angle
        
    for i in range(len(break_indexes)):

        ids.append(vdf['track_tagid'].iloc[break_indexes[i]])
        datetime.append(vdf['track_endtime'].iloc[break_indexes[i]])
        
        detections = vdf.iloc[first_detection:break_indexes[i]+1]
    
        coordinates = detections[['track_endy','track_starty','track_startx','track_endx']]
        coordinates.reset_index(drop=True, inplace=True)

        dy = (coordinates['track_endy'] - coordinates['track_starty']).to_numpy()
        dx = (coordinates['track_endx'] - coordinates['track_startx']).to_numpy()

        angle_rad = np.arctan2(dy, dx)
        unit_dx = np.cos(angle_rad)
        unit_dy = np.sin(angle_rad)
        avg_x = np.average(unit_dx)
        avg_y = np.average(unit_dy)
        if avg_x == 0 and avg_y == 0:
                    deg = 0
        elif avg_x == 0 and avg_y != 0:
            if avg_y > 0:
                deg = 270
            elif avg_y < 0:
                deg = 90
        else:
            # determine direction angle using arctan
            deg = np.rad2deg(np.arctan(avg_y/avg_x))
                    
            # since arctan limits are (-90,90), use coordinate directions to 
            # correct the angle to be within standard [0,360) range
            if avg_x > 0 and avg_y >= 0:
                deg = deg
            elif avg_x < 0 and avg_y >= 0:
                deg = 180 + deg
            elif avg_x < 0 and avg_y < 0:
                deg = deg + 180
            elif avg_x > 0 and avg_y < 0:
                deg = 360 + deg

        if deg >= exit_min and deg <= exit_max:
            new_event.append('exiting')
        elif deg >= enter_min and deg <= enter_max:
            new_event.append('entering')
        else:
            new_event.append('unknown')
        first_detection = break_indexes[i]+1
                    
    datadict ={'tagID':ids,'datetime':datetime,'event':new_event}
    return pd.DataFrame.from_dict(datadict)
    

#obtain parameters from prompt

t = int(sys.argv[1])
angle = int(sys.argv[2])
csvname = sys.argv[3]
if len(sys.argv) > 4:
    outputfile = sys.argv[4]
else:
    outputfile = "bee_angle.csv"
    
vdf = pd.read_csv(csvname)
vdf['track_endtime'] = vdf['track_endtime'].apply(lambda x: pd.to_datetime(x))
vdf['track_starttime'] = vdf['track_starttime'].apply(lambda x: pd.to_datetime(x))
vdf['track_tagid'] = vdf['track_tagid'].apply(lambda x: str(x))
vdf = vdf.sort_values(by=['track_tagid','track_starttime']).reset_index()
vdf['next_t'] = vdf['track_starttime'].shift(periods=-1)
vdf['timedelta'] = (vdf['next_t'] - vdf['track_endtime']).apply(lambda x: x.total_seconds())

#iterate over all bees in dataset and save to full dataframe

summed = beeCleanAngle(vdf)
summed.to_csv(outputfile, index=False)
print(f"Saved to {outputfile}")