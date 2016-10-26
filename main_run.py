
import numpy as np
#import parse_data
import sys
import script
import csv
import time
import webbrowser
from dateutil import parser
import urllib
import json
import urllib2
import datetime
import direction
import google_api
import clustering_module

latitude=[]   ##List of Latitude of the reports
longitude=[]  ##List of Longitude of the reports
rept=[]        ## Latitude and Longitude of reported Potholes
vehicle_id=[]  ## All the vehicle_id in database
date=[]
dxn=[]    ##All intensities of reported potholes
s=[]    ##speed of vehicles while reporting potholes
def get_data(filename,outputfile):
    
    count=0
    count1=0
    with open(filename) as csvfile:
        reader=csv.reader(csvfile, delimiter=',')
        for row in reader:

            x, y = script.parse_string(row[1])
            dxn1 = direction.get_direction(x, y)

            if(count<360):
            	a = (str)(row[7]) + ',' + (str)(row[8])
                count = count + 1
            	lat,long= google_api.process_data(a)
            else:
            	time.sleep(5)
            	count=0

            #lat,long,count=google_api.form_point(row[7],row[8],count) # snap_to_road

            with open(outputfile, 'a') as csvoutput:
                writer = csv.writer(csvoutput)
                new_row=[long,lat,row[6],row[4],dxn1,row[12]]
                writer.writerow(new_row)

def run_clustering(filename,outputfile):
    with open(filename) as csvfile:
        reader=csv.reader(csvfile, delimiter=',')
        
        for row in reader:
            rept.append(((float)(row[0]),(float)(row[1])))
            dxn.append((float)(row[4]))
            s.append((float)(row[5]))
            latitude.append((float)(row[1]))
            longitude.append((float)(row[0]))
            vehicle_id.append((float)(row[3]))

                ##Appending date and vehicle_id in a list
            p = parser.parse(row[2])  ##Parsing to perform computations on timestamp
            d = datetime.datetime.strftime(p, "%Y-%m-%d %H:%M:%S") ## Converting to a aspecific format
            date.append((d, (float)(row[3])))

                ##Appending date and vehicle_id in a list
    clustering_module.griding(latitude,longitude,rept,dxn,s,date,vehicle_id,outputfile)
    
inputfile = sys.argv[1]
snapped_file = sys.argv[2]
outputfile = sys.argv[3]

get_data(inputfile,snapped_file)
run_clustering(snapped_file,outputfile)
