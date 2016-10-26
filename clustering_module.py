import csv,operator,fnmatch,os
import numpy as np
#import matplotlib.pyplot as plt
from dateutil import parser
import datetime
import kmeans

def griding(latitude,longitude,rept,dxn,s,date,vehicle_id,outputfile):
	count1=0
	count=0
	#outputfile='iitb_clustered_real.csv'
	maxi= (float)(max(latitude))+0.002
	mini=((float)(min(latitude)))-0.002
	maxz= ((float)(max(longitude)))+0.002
	minz=((float)(min(longitude)))-0.002

	print "here#############################", maxi,maxz

	grid_lat=[]   ##List of Latitude equidistant at 0.001 for grids
	grid_long=[]  ##List of Longitude equidistant at 0.001 for grids

	###GRIDING
	while(mini<=maxi):
	    grid_lat.append(mini)
	    count=count+1
	    mini=(float)(mini+0.001)  ##0.001=10mts



	while(minz<=maxz):

	    grid_long.append(minz)
	    count1=count1+1
	    minz = (float)(minz + 0.001)




	grid_scat=[] ## list to store all the grids
	potholes_grid=[]   ## list of list all the potholes in all the grids [potholes_grid[0]=Number of pothole reports in grid 0]
	grid_speed=[]     ## list of list all the speed in all the grids
	vehicle1=[]      ## list of list all the vehicle_id in all the grids
	time_date=[]      ## list of list all the timestamps in all the grids
	counter=0
	grid_intensity=[]
	direction=[]## list of list all the intensity in all the grids

	##DIVIDING INTO GRIDS
	for n in range(count-1) :
	    for m in range(count1-1):
	        potholes_data1=[]
	        vehicle2=[]
	        speed1=[]
	        time1=[]

	        potholes_data=[] ## List of all the potholes in a particular grid
	        vehicle=[]
	        direction2=[]
	        direction1=[]## List of all the vehicle id in a particular grid
	        #intense=[]   ## List of all the intensities in a particular grid
	        time=[]   ## List of all the times in a particular grid
	        speed=[]   ## List of all the speed in a particular grid
	        #######CONDITION TO CHECK WHETHER A POTHOLE LIES IN A PARTICULAR GRID#####
	        if(counter!=len(rept)):
	            for k in range(len(rept)):
	                if (float)(rept[k][0]) >= (float)(grid_long[m]) and (float)(rept[k][0]) <= (float)(grid_long[m+1]) and (float)(rept[k][1])>= (float)(grid_lat[n]) and (float)(rept[k][1]) <= (float)(grid_lat[n+1]):

	                    if(dxn[k]==1):
	                        potholes_data.append(([rept[k][0],rept[k][1]]))
	                        counter=counter+1
	                        direction1.append(dxn[k])
	                        vehicle.append(vehicle_id[k])
	                        #p = parser.parse(date[k][0])
	             #           intense.append([intensity[k]])
	                        speed.append([s[k]])
	                        time.append([date[k][0],date[k][1]])

	                    if(dxn[k]==2):
	                        potholes_data1.append(([rept[k][0], rept[k][1]]))
	                        counter = counter + 1
	                        direction2.append(dxn[k])
	                        vehicle2.append(vehicle_id[k])
	                        # p = parser.parse(date[k][0])
	                        #           intense.append([intensity[k]])
	                        speed1.append([s[k]])
	                        time1.append([date[k][0], date[k][1]])

	            if(len(potholes_data)!= 0):
	                potholes_grid.append(potholes_data)
	                vehicle1.append(vehicle)
	                time_date.append((time))
	                grid_speed.append((speed))
	                direction.append(direction1)

	            if (len(potholes_data1) != 0):
	                potholes_grid.append(potholes_data1)
	                vehicle1.append(vehicle2)
	                time_date.append((time1))
	                grid_speed.append((speed1))
	                direction.append(direction2)

	                #      grid_intensity.append((intense))

	        grid_scat.append((grid_long[m],grid_lat[n]))   ## list to store latitude and longitudes of every grid

	for i in range(len(potholes_grid)):
	    print potholes_grid[i]
	    print len(potholes_grid)

	for j in range(len(time_date)):
	    sorted(time_date[j])  ##SORT ALL THE TIMESTAMPS According to Grids




	####FINDING THE VALUE OF K#########
	for i in range(len(potholes_grid)):
	    id=(np.unique(vehicle1[i]))   ##id stores the number of unique ids in each the grids
	    directions=[]
	    trip = [] ## number of trips of each id

	    number_reports_each_id = []
	    ## CALCULATION OF NUMBER OF TRIPS IN EACH GRID BY EACH VEHICLE##

	    for k in range(len(id)):
	            count_trip = 1
	            timestamp = [] ## ALL the timsestamps of a particular id in a given grid

	            for l in range(len(time_date[i])):  ## Check all the timsetamps in a agiven grid


	                if(id[k]==time_date[i][l][1]):

	                    timestamp.append(time_date[i][l][0]) ###Append all the timsetamps corresponding to a id that matches

	            timestamp.sort(reverse=True)

	            sum=0
	            length=len(timestamp)
	            for j in range(len(timestamp)-1):
	                diff=(parser.parse(timestamp[j])-parser.parse(timestamp[j+1])).seconds
	                print "difference in ",i, "grid is",diff
	                if(diff>=60 or sum>=60): ## if difference between consecutive timsetamps is more tha 60 seconds it will be a different trip
	                    count_trip=count_trip+1
	                    if(sum>=60):
	                        sum=0
	                else:
	                    sum=sum+diff
	                if(diff<=2):
	                    length=length-1
	            trip.append(count_trip) ## number of trips of each id in aa grid
	            number_reports_each_id.append(length)  ## NUmber of reports of each id in a grid

	    final_k=0
	    for m in range(len(number_reports_each_id)):

	        ## CALCULATE THE VALUE OF K (CLUSTER PARAMETER)#######
	        print "number of reports of each id...", number_reports_each_id[m]
	        print "number of trips", trip[m]

	        final_k=final_k+((int)(number_reports_each_id[m])/(int)(trip[m]))

	    #print "number of id's are", (np.unique(vehicle1[i]))
	    param=round((float)(final_k) / (float)(len(np.unique(vehicle1[i]))))

	    cluster_parameter = (int)(param)
	   ## calling k means#### algorithm
	#    print "data is:    ",potholes_grid[i]
	    print "DIRECTION IS",direction

	    centroid,final_speed,data_instances=(kmeans.value(potholes_grid[i],grid_speed[i],cluster_parameter))
	    print data_instances
	    if(cluster_parameter==1):
	        directions.append((np.unique(direction[i])))
	       # print  "hEEYYYYYYYYYYYYYYYYYYY#########",directions,direction[i]
	    else:
	        while(cluster_parameter!=0):
	            directions.append((np.unique(direction[i])))
	            cluster_parameter=cluster_parameter-1
	   
	    with open(outputfile, 'a') as csvoutput:
	        writer = csv.writer(csvoutput)
	        for i in range(len(centroid)):
	            if(data_instances[i][0]>0):
	            	#count = count + 1
	            	new_row = [centroid[i][0], centroid[i][1],final_speed[i][0],data_instances[i][0],(float)(directions[i])]
	                writer.writerow(new_row)
	                # z=((float)(data_intensity[i][0]))/((float)(final_speed[i][0])
	    id=0
