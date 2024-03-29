# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from math import e
from math import log
from sklearn.decomposition import PCA

class logistic_regression(object):

# definition of the sigmoid function
  def sigmoid(self, X): 
      s = 1/(1+e**(-X))
    # returns the sigmoid(x)
      return s                                                                            

# training the model using default values of no. of iterations, learning rate
  def train(self, x_train, y_train, epochs = 3000, alpha = 0.1, lamda = 0.001, k = 2):                           
    # number of classes
      self.k = k
      x = np.array(x_train)
      self.x_train = x
      m = x.shape[0]
      n = x.shape[1]
      X = np.zeros((m,n))
      Y = np.zeros((m,self.k))
    # converting y into one Vs all type matrix
      for a in range(m):                                                          
        Y[a,y_train[a]]=1
    # normalising the data
      for a in range(n):                                                          
              X[:,a] = (x[:,a]-np.mean(x[:,a]))/(np.std(x[:,a])+1e-09)            
    # initialising theta matrix
      self.theta = np.zeros((self.k,n+1))                                         
      X = np.hstack((np.ones((m,1)),X))
      H = np.dot(X,self.theta.T)
    # hypothesis function
      G = self.sigmoid(H)                                                         
    # cost function considering regularisation
      cost_func = -np.sum(Y*np.log(G)+(1-Y)*np.log(1-G))/m + (lamda/(2*m))*np.sum(self.theta[:,1:]**2) 
      self.l = []
      self.p = []     
    # performing gradient descent over input given iterations
      for epoch in range(epochs):  
        self.p.append(epoch)                                                     
        H = np.dot(X,self.theta.T)
        G = self.sigmoid(H)
        cost_func = -np.sum(Y*np.log(G)+(1-Y)*np.log(1-G))/m + (lamda/(2*m))*np.sum(self.theta[:,1:]**2)
        theta1 = np.zeros((self.k,n+1))
        theta1[:,1:] = self.theta[:,1:]      
        self.l.append(cost_func)                                         
      #updating theta using gradient of theta and also regularistaion parameter
        self.theta = self.theta - (alpha/m)*(np.dot((G-Y).T,X) + lamda*theta1)    

  def get_params(self):
    # returns the weights(theta)                                                         
      return self.theta

# predicting the value of y using the trained model
  def predict(self,x_test):                                                     
      x = np.array(x_test)
      m = x.shape[0]
      n = x.shape[1]
      X = np.zeros((m,n))
    # normalising the data
      for a in range(n):                                                          
              X[:,a] = (x[:,a]-np.mean(x[:,a]))/(np.std(x[:,a])+1e-09)
      X = np.hstack((np.ones((m,1)),X))
      H = np.dot(X,self.theta.T)
    # hypothesis(G)
      G = self.sigmoid(H)       
    # predicting the value of y based on the maximum probable class                                                  
      prediction = G.argmax(axis = 1).reshape((m,1))                              
      return prediction

  def accuracy(self,y_pred,y_true):
      acc = np.mean(y_pred == y_true)                                             
      return acc

# splits the data into training set and testing set based on input split fraction
  def split_train_test(self,X,y,split):                                         
      m = size()
      n = split*np.size(y,axis=0)
      x_train = X[0:n,:]
      x_test = X[n:,:]
      y_train = y[0:n]
      y_test = y[n:]
      return x_train,x_test,y_train,y_test

# plots the cost function Vs the no. of iterations
  def plot_loss(self):                                                               
      plt.plot(self.p,self.l)

# plots 
  def visualize(self, x, y, c = 0, grid_step = 10):
      pca = PCA(n_components = 2)
      pca.fit(self.x_train)
      x1 = pca.transform(x)[:,0]
      x2 = pca.transform(x)[:,1]
      x1_min, x1_max = x1.min() - 0.1, x1.max() + 0.1
      x2_min, x2_max = x2.min() - 0.1, x2.max() + 0.1
      xx, yy = np.meshgrid(np.arange(x1_min, x1_max, grid_step), np.arange(x2_min, x2_max, grid_step))
      pred = self.predict(pca.inverse_transform(np.c_[xx.ravel(), yy.ravel()]))
      plt.contour(xx, yy, (pred.reshape(xx.shape) == c))
      plt.scatter(x1, x2, c = (y == c))
      plt.show()
