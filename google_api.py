import webbrowser
import urllib
import json
import  csv
import urllib2
import time
#time.sleep(5)
#inputfile='iitb_parsed_real.csv'
#outputFileName="iitb_snapped_real.csv"

def process_data(point):



    #   webbrowser.open("https://roads.googleapis.com/v1/snapToRoads?path=" + point + "&key=AIzaSyBP1gpcoREd88Er-o2oDyxlAgzwpYGjwpg")
    f = urllib.urlopen(
        "https://roads.googleapis.com/v1/snapToRoads?path=" +point + "&key=AIzaSyBcLFHwsNhGQzXh82Jt1_ng3wqBygf4O2Y")

    response = urllib2.urlopen(f.geturl())
    data1 = json.load(response)

    with open('data.json', 'w') as outfile:
        json.dump(data1, outfile)
    

    with open('data.json') as data_file:
        data = (json.load(data_file))
        for i in range(len(data["snappedPoints"])):
            latitude=(str)(data["snappedPoints"][i]["location"]["latitude"])
            longitude=(str)(data["snappedPoints"][i]["location"]["longitude"])

        '''

    with open(outputFileName, 'a') as csvoutput:
        writer = csv.writer(csvoutput)

#print "length is:", len(data["snappedPoints"])
        for i in range(len(data["snappedPoints"])):
            new_row = [(str)(data["snappedPoints"][i]["location"]["latitude"]),
                       (str)(data["snappedPoints"][i]["location"]["longitude"]),

                       ]
            writer.writerow(new_row
    '''
    print latitude,longitude
    return latitude,longitude

'''
def form_point(lat,long,count):
        
        print count
        if(count<360):
            a = (str)(lat) + ',' + (str)(long)
            print a
            latitude,longitude= process_data(a)

        else:
            time.sleep(5)
            count=0
        return latitude,longitude,count
        
       # count = count + 1
       '''
