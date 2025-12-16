## Classification algorithms for bees at the entrance to the hive to predict their trajectory.

### FILES

worker05.txt -> Example dataset from BeeCam-AprilTag

BeeCam-AprilTag.ipynb -> Graphs BeeCam-AprilTag example data y-position over time

beecam-graphs -> Folder containing BeeCam-AprilTag graphs

month_data/BeeClassify.ipynb -> Converts multiple csv files subset into one csv file and graphs the y movement across frames

month_data/cheatsheet.csv -> Manually corroborated event classification results for BeeClassify.ipynb

month_data/Rules.ipynb -> Implementing all methods for event classification on subset of month data. Contains recall, precision, f1-score, accuracy and class distribution

month_data/Rules-Full.ipynb -> Implementing compound event for all 289 csv in dataset

month_data/graphs -> Tracking bee movements from subset of month-long data

month_data/*.png -> Generated visualizations from Rules.ipynb and Rules-Full.ipynb

month_data/bees -> All 289 csv data with text files containing their names to combine them

month_data/beeActivity.csv -> 4 csv files combined and separated by event id, for use in Rules.ipynb

### USER-DEFINED VALUES

t2 -> Distance that must be covered to classify an event for DISP_START and DISP_END.

angle -> Angle threshold (in degrees) for verifying the classification for an event.

### GRAPH FORMAT

x-axis -> Frames of event in order

y-axis -> Y position of bee at event index

### CREDITS

Summed vector angle function and worker05.txt was taken from BeeCam-AprilTag https://github.com/AERS-Lab/BeeCam-AprilTag
