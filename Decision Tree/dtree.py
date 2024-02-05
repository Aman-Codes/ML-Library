# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from collections import Counter

class node(object):
  def _init_(self,f,t,left,right):
    self.f = f
    self.t = t
    self.left = left
    self.right = right

class leaf(object):
  def _init_(self, label):
    self.label = label

class dtree(object):
# gini impurity for a group
  def gini_imp(self, label):
    a = np.unique(label,return_counts=True)[1]/float(len(label))
    g = 1-np.sum(a**2)
    return g
# split points based on best information gain
  def split(self, x, y, a):
    gini = 100000
    f = 0
    t = 0
    for i in range(x.shape[1]):
      for j in range(len(a[i])):
        c = np.array(((x[:,i]>=a[i][j])).astype(int))
        p = np.sum(c)/len(c)
        b = self.gini_imp(y[np.where(c==1)])*p + self.gini_imp(y[np.where(c==0)])*(1-p)
        if b<gini : 
          gini = b
          f = i
          t = a[i][j]
    return f,t
# recursive function to build decision terr
  def build(self, x, y, a):
    f,t = self.split(x,y,a)
    z = np.array((x[:,f]>t).astype(int))
    y_left = y[np.where(z==0)]
    y_right = y[np.where(z==1)]
    p = len(y_right)/len(y) 
    ig = self.gini_imp(y) - p*self.gini_imp(y_right) - (1-p)*self.gini_imp(y_left)
    if ig==0 :
      n = leaf()
      n.label = Counter(y).most_common(1)[0][0]
      return n
    else:
      n = node()
      n.f = f
      n.t = t
      x_left = x[np.argwhere(z-1).flatten(),:]
      x_right = x[np.argwhere(z).flatten(),:]
      n.right = self.build(x_right,y_right,a)
      n.left = self.build(x_left,y_left,a)
      return n

  def fit(self, x_train, y_train): 
    X = np.array(x_train)
    y = np.array(y_train)
    n = X.shape[1]
    m = X.shape[0]
    a = []
    for i in range(n):
      c = np.unique(X[:,i])
      a.append(c)
    self.tree = self.build(X,y,a)

  def accuracy(self, y_pred, y_true):                                             
      p = 0
      m = len(y_true)
      for a in range(m):                                                        
        if y_true[a]==y_pred[a]:                
          p+=1
      return (p*100)/m

  def predict(self, x):
      X = np.array(x)
      y_pred = np.zeros((X.shape[0],1))
      for i in range(X.shape[0]):
         a = self.tree
         while isinstance(a,leaf) != True:
           f = a.f
           t = a.t
           if X[i][f] >= t: a = a.right
           else : a = a.left
         y_pred[i] = a.label
      return y_pred
