# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from math import e

class linear_regression(object):

  # training the model using default values of no. of iterations,learning rate,without regularisation
    def fit(self, x_train, y_train, epochs = 1000, alpha = 0.001, lamda = 0.0001):                                              
        x = np.array(x_train)
        self.x_train = x
        m = np.size(x,axis = 0)
        n = np.size(x,axis = 1)
        X = np.zeros((m,n))
      # normalising the data
        for a in range(n):                                                      
            X[:,a] = (x[:,a]-np.mean(x[:,a]))/(np.std(x[:,a])+1e-09)
        X = np.hstack((np.ones((m,1)),X))
        y = np.array(y_train).reshape(m,1)   
      # initialsing theta matrix 
        self.theta = np.zeros((n+1,1))                                          
      # computing the hypothesis function
        hypothesis = np.dot(X,self.theta)                                       
      # defining the cost function
        cost_func = (((hypothesis-y)**2).sum()+np.sum(self.theta[1:]**2)*lamda)/(m*2)                         
      # setting a default learning rate of 0.0001
        epoch = 0
        self.l=[]
        self.p=[]
      # performing gradient descent step for a default value of 7000 iterations
        while epoch < epochs:   
            theta1 = np.zeros((n+1,1))
            theta1[1:] = self.theta[1:]                                           
            hypothesis = np.dot(X,self.theta)
            cost_func = (((hypothesis-y)**2).sum()+np.sum(self.theta[1:]**2)*lamda)/(m*2)
            # updating the values of the theta matrix
            self.theta = self.theta - (alpha/m)*(np.dot(X.T,(hypothesis-y))-lamda*theta1)   
            self.l.append(cost_func)
            self.p.append(epoch)
            epoch+=1

  # returns the weights(theta)
    def get_params(self):                                                       
        return self.theta

  # predicting the value of y using the trained model
    def predict(self, x_test):                                                   
        x = np.array(x_test)
        m = np.size(x,axis = 0)
        n = np.size(x,axis = 1)
        X = np.zeros((m,n))
      # normalising the data
        for a in range(n):                                                      
            X[:,a] = (x[:,a]-np.mean(x[:,a]))/(np.std(x[:,a])+1e-09)   
        X = np.hstack((np.ones((m,1)),X))
      # predicting the output using the theta matrix
        prediction = np.dot(X, self.theta)                                       
        return prediction

  # calculating the score of the prediction made by the model
    def score(self, y_pred, y_test):                                              
        self.y_test = np.array(y_test)
        u = ((self.y_test.reshape((y_test.shape[0],1))-y_pred**2)).sum()        
        v = np.sum((y_test-self.y_test.mean())**2)
        return 1-u/v

  # splits the data into training set and testing set based on input split fraction
    def split_train_test(self, X, y, split):                                       
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
        plt.show()

  # plots 
    def visualize(self, x, y):
        plt.scatter(x, y, color = 'blue')
        plt.plot(self.x_train, self.predict(self.x_train), color = 'red')
        plt.show()
