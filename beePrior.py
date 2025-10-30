#USE : python beePrior.py (t) (t2) (csvfile) (outputfile-optional)



#imports

import pandas as pd
from datetime import datetime, timedelta
import sys

#function
## Look at events prior and classify based on y displacement


def beeCleanPrior(bee):

    new_event = []
    datetime = []
    ids = []
    first_detection = 0
    for i in range(len(break_indexes)):

        ids.append(vdf['track_tagid'].iloc[break_indexes[i]])
        datetime.append(vdf['track_endtime'].iloc[break_indexes[i]])
        
        detections = vdf.iloc[first_detection:break_indexes[i]+1]
    
        coordinates = detections[['track_endy','track_starty']]
        coordinates.reset_index(drop=True, inplace=True)
        
        final = coordinates['track_endy'].iloc[-1]
        
        for k in range(len(coordinates)):
            prev = coordinates['track_starty'].iloc[len(coordinates)-k-1]
            dif = final - prev
            if abs(dif) >= t2:
                if dif > 0:
                    new_event.append('exiting')
                elif dif < 0:
                    new_event.append('entering')
                else:
                    new_event.append('unknown')
                break
            elif k == len(coordinates) - 1:
                if dif > 0:
                    new_event.append('exiting')
                elif dif < 0:
                    new_event.append('entering')
                else:
                    new_event.append('unknown')
        first_detection = break_indexes[i]+1
        

    datadict ={'tagID':ids,'datetime':datetime,'event':new_event}
    return pd.DataFrame.from_dict(datadict)
            
        
 
    

#obtain parameters from prompt

t = int(sys.argv[1])
t2 = int(sys.argv[2])
csvname = sys.argv[3]
if len(sys.argv) > 4:
    outputfile = sys.argv[4]
else:
    outputfile = "bee_prior.csv"
    
vdf = pd.read_csv(csvname)
vdf['track_endtime'] = vdf['track_endtime'].apply(lambda x: pd.to_datetime(x))
vdf['track_starttime'] = vdf['track_starttime'].apply(lambda x: pd.to_datetime(x))
vdf['track_tagid'] = vdf['track_tagid'].apply(lambda x: str(x))
vdf = vdf.sort_values(by=['track_tagid','track_starttime']).reset_index()
vdf['next_t'] = vdf['track_starttime'].shift(periods=-1)
vdf['timedelta'] = (vdf['next_t'] - vdf['track_endtime']).apply(lambda x: x.total_seconds())
#iterate over all bees in dataset and save to full dataframe

prior = beeCleanPrior(vdf)
prior.to_csv(outputfile, index=False)
print(f"Saved to {outputfile}")