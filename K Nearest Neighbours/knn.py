# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

class knn(object):

# saving the training data set
  def fit(self, x_train, y_train, k = 1):  
  # k is the no. of nearest neighbours               
    self.k = k                                     
    self.X = np.array(x_train)
    self.y = np.array(y_train)

# predicting the class of test data 
  def predict(self, x_test):                       
    x = np.array(x_test)
    m = x.shape[0]
    y_pred = np.zeros((m,1))  
  # finding distances between a given point and the training data 
    for a in range(m):                              
      dist = np.sum((self.X-x[a,:])**2,axis=1)
      dist = np.vstack((dist,self.y))
    # arranging the distances in ascending order
      b = np.argsort(dist[0,:])                   
    # storing the indices of the k nearest points 
      l = b[0:self.k]                             
    # assigning the class which is most frequent to the test point
      y_pred[a] = stats.mode(dist[1,l]).mode        
    return y_pred

# splitting the data set into training and test sets based on the split fraction
  def split_train_test(self, X, y, split):            
        m = size()
        n = split*np.size(y,axis=0)
        x_train = X[0:n,:]
        x_test = X[n:,:]
        y_train = y[0:n]
        y_test = y[n:]
        return x_train,x_test,y_train,y_test  

# classifies a prediction as correct only if it is equal to the original class
  def accuracy(self, y_true, y_pred):               
    m = len(y_true)
    acc=0
    for a in range(m):
      if y_pred[a]==y_true[a]: acc+=1
    return (acc*100)/m

  def visualize(self, x, y, c = 0, grid_step = 10):
      pca = PCA(n_components = 2)
      pca.fit(self.X)
      x1 = pca.transform(x)[:,0]
      x2 = pca.transform(x)[:,1]
      x1_min, x1_max = x1.min() - 0.1, x1.max() + 0.1
      x2_min, x2_max = x2.min() - 0.1, x2.max() + 0.1
      xx, yy = np.meshgrid(np.arange(x1_min, x1_max, grid_step), np.arange(x2_min, x2_max, grid_step))
      pred = self.predict(pca.inverse_transform(np.c_[xx.ravel(), yy.ravel()]))
      plt.contour(xx, yy, (pred.reshape(xx.shape) == c))
      plt.scatter(x1, x2, c = (y == c))
      plt.show()
