from sklearn.cluster import KMeans 
import matplotlib.pyplot as grapher 
import numpy as np 
import pandas

# open CSV data file and convert into pandas dataframe 
inFile = open('ACM-Research-Coding-Challenge\ClusterPlot.csv')
data = pandas.read_csv(inFile, header = 0)

# create K-means models with K (number of clusters) ranging from 1 to 9 and calculate specific inertias for each
clusterNums = range(1,10)
clusterInertias = []
for k in clusterNums:
    kmeans_model = KMeans(n_clusters=k, random_state=1).fit(data.iloc[:,1:])
    # inertia is the sum of squared distances of points to the closest cluster center
    clusterInertias.append(kmeans_model.inertia_)

# Find out which cluster number's inertia is the farthest from the graph's average line 
maxDistance = 0.0 
optimalCluster = 0
x1, y1 = 1, clusterInertias[0]
x2, y2 = 9, clusterInertias[8]
slope = (y2 - y1) / (x2 - x1)

for k in clusterNums:
    yx = slope * (k - 1) + clusterInertias[0]
    distance = yx - clusterInertias[k - 1]

    if(distance > maxDistance):
        maxDistance = distance
        optimalCluster = k

# print calculated optimal number of clusters
print('Using K-means clustering with k=1-9, it can be seen that the amount of clusters in the data is', optimalCluster)

# using optimal number of clusters from graph and fitting data into desired amount of clusters
kmeans_model = KMeans(n_clusters=optimalCluster, random_state=1).fit(data.iloc[:,1:])
labels = kmeans_model.labels_

# create elbow graph to visualize optimal clusternum (at 'elbow' of graph)
grapher.plot(clusterNums, clusterInertias)
grapher.show()



