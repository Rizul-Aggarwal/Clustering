
import numpy as np
#import parse_data
import script
import csv
import time
import webbrowser
from dateutil import parser
import urllib
import json
import urllib2
import datetime
def get_direction(x,y):
    dxn=0

    if(len(x)>2 and len(y)>2):

                best_fit_line = np.poly1d(np.polyfit(y, x, 1))(y)
                angle = np.rad2deg(np.arctan2(y[-1] - y[0], x[-1] - x[0]))
                if angle<0:
                    angle=angle+360
                #print angle
                if(angle>0 and angle<180):
                    dxn=1
                
                else:
                    dxn=2
    return dxn