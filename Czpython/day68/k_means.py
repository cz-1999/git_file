print(__doc__)

#Author: Phil Roth <mr.phil.roth@gmail.com>
#License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

plt.figure(figsize=(12,12))

n_samples = 1500
random_state = 170
x,y = make_blobs(n_samples=n_samples,random_state=random_state)

#Incorrect number of clusters
y_pred = KMeans(n_clusters=2,random_state=random_state).fit_predict(x)

plt.subplot(221)
plt.scatter(x[:,0],x[:,1],c=y_pred)
plt.title("Incorrect Number of Blobs")

#Anisotropicly distributed data
transformation = [[0.60834549,-0.63667341],[-0.40887718,0.85253229]]
x_aniso = np.dot(x,transformation)
y_pred = KMeans(n_clusters=3,random_state = random_state).fit_predict(x_aniso)

plt.subplot(222)
plt.scatter(x_aniso[:,0],x_aniso[:,1],c=y_pred)
plt.title("Anisotropicly Distributed Blobs ")

#Different variance
x_varied,y_varied = make_blobs(n_samples=n_samples,cluster_std=[1.0,2.5,0.5],random_state=random_state)
y_pred = KMeans(n_clusters = 3,random_state=random_state).fit_predict(x_varied)

plt.subplot(223)
plt.scatter(x_varied[:,0],x_varied[:,1],c=y_pred)
plt.title("Unequal Variance")

#Uneven sized blobs
x_filtered = np.vstack((x[y==0][:500],x[y==1][:100],x[y==2][:10]))
y_pred = KMeans(n_clusters = 3,random_state=random_state).fit_predict(x_varied)

plt.subplot(224)
plt.scatter(x_varied[:,0],x_varied[:,1],c=y_pred)
plt.title("Unequal Variance")

#Unevenly sized blobs
x_filtered = np.vstack((x[y==0][:500],x[y==1][:100],x[y==1][:100],x[y==2][:10]))
y_pred = KMeans(n_clusters = 3,random_state=random_state).fit_predict(x_filtered)

plt.subplot(224)
plt.scatter(x_filtered[:,0],x_filtered[:,1],c=y_pred)
plt.title("Unevenly Sized Blobs")
plt.savefig("D:/python/czpython/save_kmeans")
plt.show()