# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from scipy import stats
import random
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

class k_means(object):

# function to predict the classes based on input value of k
  def fit(self, x_train, k = 2, epochs = 1000):
    x=np.array(x_train)
    self.x_train = x
    self.k=k
    m=x.shape[0]
    n=x.shape[1]
    X = np.zeros((m,n))
  # normalisation
    for a in range(n):
      X[:,a]=(x[:,a]-np.mean(x[:,a]))/(np.std(x[:,a])+1e-09)
  # randomly initialising k centroids
    idx = random.sample(range(m),self.k)
    mean = np.zeros((self.k,n))
    for a in range(self.k):
      mean[a:a+1,:] = X[idx[a]:idx[a]+1,:] 
    for i in range(epochs):     
      cost_func = 0   
    # counting the no. of points in each cluster
      count = np.zeros((self.k,1))
      c = np.zeros((m,1))
    # finding distances and assigning each point to a cluster
      for a in range(m):     
        dist = np.sum((X[a:a+1,:]-mean)**2,axis=1)
        c[a] = np.argmin(dist)
      mean = np.zeros((self.k,n))
    # updating the centroid of each cluster
      for a in range(m):
        mean[int(c[a]):int(c[a])+1,:] += X[a:a+1,:]
        count[int(c[a])]+=1
      for a in range(self.k):
        mean[a:a+1,:]/=count[a]
    # finding the cost function
      for a in range(m):
        cost_func +=np.sum((X[a:a+1,:] - mean[int(c[a]):int(c[a])+1,:])**2)
      cost_func /= m
    return c

  def accuracy(self,y_true,y_pred):
    m=len(y_pred)
    acc=0
    for a in range(m):
      if y_true[a] == y_pred[a]:
        acc+=1
    return (acc*100)/m
  
  def visualize(self, x, c):
      pca = PCA(n_components = 2)
      pca.fit(self.x_train)
      x1 = pca.transform(x)[:,0]
      x2 = pca.transform(x)[:,1]
      x1_min, x1_max = x1.min() - 0.1, x1.max() + 0.1
      x2_min, x2_max = x2.min() - 0.1, x2.max() + 0.1
      plt.scatter(x1, x2, c = c)
      plt.show()
