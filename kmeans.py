import os
import numpy as np
import csv
#from haversine import haversine

# kmeans clustering algorithm
# data = set of data points
# k = number of clusters
# c = initial list of centroids (if provided)
#

def kmeans(data,speed, k, c= None):

    centroids = []
    del centroids[:]
   # intense = [[] for i in range(k)]
    final_speed=[[] for i in range(k)]
    centroids = randomize_centroids(data, centroids, k)

    old_centroids = [[] for i in range(k)]

    iterations = 0
    while not (has_converged(centroids, old_centroids, iterations)):
        iterations += 1

        clusters = [[] for i in range(k)]
       #intensity = [[] for i in range(k)]
        speed_clusters=[[] for i in range(k)]
        number_data_instances=[[] for i in range(k)]

        # assign data points to clusters
        clusters,speed_clusters = euclidean_dist(data,speed, centroids, clusters,speed_clusters)
        #outputFileName = outputpath + "SectoredLatLongs.csv"
       # with open(outputFileName, 'a') as csvoutput:
            #writer = csv.writer(csvoutput)

        # recalculate centroids
        count=0
        index = 0
        for cluster in clusters:


                old_centroids[index] = centroids[index]
                centroids[index] = np.median(cluster, axis=0).tolist()

                number_data_instances[index]=[len(cluster)]

                index += 1
        index=0
#        for intensi in intensity:
  #                  intense[index] = np.mean(intensi, axis=0).tolist()

   #                 index += 1
        index=0
        for speed1 in speed_clusters:
                    final_speed[index] = np.mean(speed1, axis=0).tolist()

                    index += 1
        index = 0

            #for i in range(len(centroids)):
             #   count=count+1

              #  new_row = [centroids[i][0],centroids[i][1]]
               # writer.writerow(new_row)
    #print "values written in iteration are:      ",count

    print("####################CLUSTER STARTS###########################")
    print "cluster",i
    print ("Data is:", data)
    print("The total number of data instances is: " + str(len(data)))
    print("The total number of iterations necessary is: " + str(iterations))
    print "VALUE OF K IS",k
    print("The medians of each cluster are: " + str(centroids))
    print "length of centroids",len(centroids)
    print("The clusters are as follows:")
    for cluster in clusters:

        print("Cluster with a size of " + str(len(cluster)) + " starts here:")

        print(np.array(cluster).tolist())
        print("Cluster ends here.")

    print("#######################CLUSTER ENDS#############################")
    print "   "
    print "   "
    return centroids,final_speed,number_data_instances

# Calculates euclidean distance between
# a data point and all the available cluster
# centroids.


#outputpath = "F:\\PythonStuff"
def euclidean_dist(data,speed,centroids, clusters,speed_clusters):
    mu_index=[]
    for instance in data:
        # Find which centroid is the closest
        # to the given data point.
        mu_index = min([(i[0], np.linalg.norm(instance-centroids[i[0]])) \
                            for i in enumerate(centroids)], key=lambda t:t[1])[0]
        #mu_index.append(haversine(data,centroids, miles=True))

        try:
            clusters[mu_index].append(instance)
            #intensity[mu_index].append(b[mu_index])
            speed_clusters[mu_index].append(speed[mu_index])
        except KeyError:
            clusters[mu_index] = [instance]

    # If any cluster is empty then assign one point
    # from data set randomly so as to not have empty
    # clusters and 0 means.
    for cluster in clusters:
        if not cluster:
            cluster.append(data[np.random.randint(0, len(data), size=1)].flatten().tolist())
   # for intense in intensity:
    #    if not intense:
     #       intense.append(b[np.random.randint(0, len(b), size=1)].flatten().tolist())

    for speed2 in speed_clusters:
        if not speed2:
            speed2.append(speed[np.random.randint(0, len(speed), size=1)].flatten().tolist())

    return clusters,speed_clusters


# randomize initial centroids
def randomize_centroids(data, centroids, k):
    for cluster in range(0, k):
        centroids.append(data[np.random.randint(0, len(data), size=1)].flatten().tolist())
    return centroids


# check if clusters have converged
def has_converged(centroids, old_centroids, iterations):
    MAX_ITERATIONS = 1000
    if iterations > MAX_ITERATIONS:
        return True
    return old_centroids == centroids

#a=np.genfromtxt('lat-longdata-iitb.csv',delimiter=';').astype(np.float)

#a=np.array(list(csv.reader(open("lat-longdata-iitb.csv","rb"),delimiter=','))).astype('float')

def value(data,speed,k_value):

    a = np.array(data)
    #b=np.array(intensity)
    speed1=np.array(speed)
    centroid=kmeans(a,speed1,k_value,c=None)
    return centroid

