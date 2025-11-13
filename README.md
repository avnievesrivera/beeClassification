## Classification algorithms for bees at the entrance to the hive to predict their trajectory.

### FILES

BeeClassify.ipynb -> Initial algorithms on which we worked with

beeActivity.csv -> File of all detections in original data

month_data/BeeClassify.ipynb -> Converts multiple csv files subset into one csv file

month_data/cheatsheet.csv -> Manually corroborated event classification results

month_data/cheatsheetroundabout.csv -> Manually corroborated u-turn events as single movement classification

month_data/cheatsheetboth.csv -> Manually corroborated compound events

month_data/Rules.ipynb -> Implementing all methods for event classification on subset of month data. Contains directional complementarity and accuracy checks

month_data/Rules-Full.ipynb -> Implementing compound event for all data in dataset

graphs folder -> Tracking bee movements from beeActivity.csv

month_data/graphs -> tracking bee movements from subset of month-long data

month_data folder -> Same experiment with monthlong extracted data.

### USER-DEFINED VALUES

t -> User-defined seconds threshold to divide and combine detections into events.

t2 -> Distance that must be covered to classify an event.

angle -> Angle threshold (in degrees) for verifying the classification for an event.

### GRAPH FORMAT

x-axis -> frames of event in order

y-axis -> y position of bee at event index

### CREDITS

Summed vector angle function was taken from BeeCam-AprilTag https://github.com/AERS-Lab/BeeCam-AprilTag
