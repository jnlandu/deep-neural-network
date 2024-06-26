# -*- coding: utf-8 -*-
"""jeremie_Neural_Networks_From_Scratch_updated.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A9ZIGO7SBUB3zG8q8L84xyqDF9LbWuSv
"""

import numpy as np
import matplotlib.pyplot as plt

# generate data
var = 0.2
n = 800
class_0_a = var * np.random.randn(n//4,2)
class_0_b =var * np.random.randn(n//4,2) + (2,2)

class_1_a = var* np.random.randn(n//4,2) + (0,2)
class_1_b = var * np.random.randn(n//4,2) +  (2,0)

X = np.concatenate([class_0_a, class_0_b,class_1_a,class_1_b], axis =0)
Y = np.concatenate([np.zeros((n//2,1)), np.ones((n//2,1))])
X.shape, Y.shape

# shuffle the data
rand_perm = np.random.permutation(n)

X = X[rand_perm, :]
Y = Y[rand_perm, :]

X = X.T
Y = Y.T
X.shape, Y.shape

# train test split
ratio = 0.8
X_train = X [:, :int (n*ratio)]
Y_train = Y [:, :int (n*ratio)]

X_test = X [:, int (n*ratio):]
Y_test = Y [:, int (n*ratio):]
X_train.shape

plt.scatter(X_train[0,:], X_train[1,:], c=Y_train[0,:])
plt.show()

## Fill this cell

def sigmoid(z):
  # Your code here
  return 1/(1+np.exp(-z))

def d_sigmoid(z):
  # Your code here
  return sigmoid(z)*(1-sigmoid(z))


def loss(y_pred,Y):
    ##### WRITE YOUR CODE HERE #####
    loss = (-1 / Y.shape[0]) * np.sum(Y * np.log(y_pred) + (1 - Y) * np.log(1 - y_pred))
    return loss

"""## Initialize parameters"""

h0, h1, h2 = 2, 10, 1

def init_params():
    # Your code here
  #xavier = np.sqrt(6/(X.shape[0]+ Y.shape[0])2
  W1 = np.random.randn(h1,h0)
  W2 = np.random.randn(h2,h1)  #(10,1)
  b1 = np.random.randn(h1, 1)  # (1,800)
  b2 = np.random.randn(h2, 1) ## (1, 800)
  # print(W2.shape)
  # print(W1.shape)
  # print(b2.shape)
  # print(b1.shape)
  return W1, W2, b1, b2

"""## Forward pass"""

def forward_pass(X, W1,W2, b1, b2):
  Z1 =  W1.dot(X) + b1 #W1.dot(X) + b1  ## W1.shape =(10,2), dim Z1 =b1.shape =(10,800)
  A1 = sigmoid(Z1)
  Z2 = W2.dot(A1) +b2 #.dot(A1) + b2 # dim Z2 = dim b2 = (1,10)
  A2 = sigmoid(Z2) # dim A2 = (1,800)
  #return A2.shape
  return A2, Z2, A1, Z1

"""## Backward pass"""

# def backward_pass(X,Y, A2, Z2, A1, Z1, W1, W2, b1, b2):

#   # Your code here
#    dW2 = (1/Y.shape[0])*A1 @(A2-Y).T #(A2-Y)@ A1 @(A2-Y).T
#    dW1 = (((A2-Y).T)@ W2.T)@ d_sigmoid(Z1)@X.T # @(1-A1)@X.T
#    db2 = A2-Y
#    db1 = (A2-Y).T @ W2.T@ d_sigmoid(Z1)#A1 @ (1-A1) #
#    return dW1, dW2, db1, db2

def backward_pass(X,Y, A2, Z2, A1, Z1, W1, W2, b1, b2):
  #L = loss(A2,Y)
  # Your code here
  dL_dA2 = (A2 - Y)/(A2 * (1-A2))
  dA2_dZ2 = d_sigmoid(Z2)
  dZ2_dW2 = A1.T

  dW2 = (dL_dA2 * dA2_dZ2) @ dZ2_dW2
  db2 = dL_dA2 @ dA2_dZ2.T

  dZ2_dA1 = W2
  dA1_dZ1 = d_sigmoid(Z1)
  dZ1_dW1 = X.T

  dW1 = (dZ2_dA1.T * (dL_dA2 * dA2_dZ2)* dA1_dZ1) @ dZ1_dW1
  db1 = ((dL_dA2 * dA2_dZ2)@(dZ2_dA1.T *dA1_dZ1).T).T


  return dW1, dW2, db1, db2

"""## Accuracy"""

def accuracy(y_pred, y):

  # Your code here
  pred = (y_pred >= 0.5).astype(int)
  acc = np.sum(pred == y)/y.shape[1]
  return acc

def predict(X,W1,W2, b1, b2):
  # Your code here
  Z1 = W1.dot(X) + b1
  A1 = sigmoid(Z1)
  Z2 = W2.dot(A1) + b2
  A2 = sigmoid(Z2)
  return A2

"""## Update parameters"""

def update(W1, W2, b1, b2,dW1, dW2, db1, db2, alpha ):

  # Your code here
  # dW1 = backward_pass(X,Y, A2, Z2, A1, Z1, W1, W2, b1, b2)[0]
  # dW2 = backward_pass(X,Y, A2, Z2, A1, Z1, W1, W2, b1, b2)[1]
  # db1 = backward_pass(X,Y, A2, Z2, A1, Z1, W1, W2, b1, b2)[2]
  # db2 = backward_pass(X,Y, A2, Z2, A1, Z1, W1, W2, b1, b2)[3]

  W1 = W1 - alpha*dW1
  W2 = W2 - alpha*dW2
  b1 = b1 - alpha*db1
  b2 = b2 - alpha*db2

  return W1, W2, b1, b2

"""## Plot decision boundary"""

def plot_decision_boundary(W1, W2, b1, b2):
  x = np.linspace(-0.5, 2.5,100 )
  y = np.linspace(-0.5, 2.5,100 )
  xv , yv = np.meshgrid(x,y)
  xv.shape , yv.shape
  X_ = np.stack([xv,yv],axis = 0)
  X_ = X_.reshape(2,-1)
  A2, Z2, A1, Z1 = forward_pass(X_, W1, W2, b1, b2)
  plt.figure()
  plt.scatter(X_[0,:], X_[1,:], c= A2)
  plt.show()

"""## Training loop"""

alpha = 0.001
W1, W2, b1, b2 = init_params()
n_epochs = 10000
train_loss = []
test_loss = []
for i in range(n_epochs):
  ## forward pass
  A2, Z2, A1, Z1 = forward_pass(X_train,W1,W2,b1,b2)
  ## backward pass
  dW1, dW2, db1, db2 = backward_pass(X_train,Y_train,A2,Z2,A1,Z1,W1,W2,b1,b2)
  ## update parameters
  W1, W2, b1, b2 = update(W1, W2, b1, b2,dW1, dW2, db1, db2, alpha )

  ## save the train loss
  train_loss.append(loss(A2, Y_train))
  ## compute test loss
  A2, Z2, A1, Z1 = forward_pass(X_test, W1, W2, b1, b2)
  test_loss.append(loss(A2, Y_test))

  ## plot boundary
  if i %1000 == 0:
    plot_decision_boundary(W1, W2, b1, b2)

## plot train et test losses
plt.plot(train_loss)
plt.plot(test_loss)

y_pred = predict(X_train, W1, W2, b1, b2)
train_accuracy = accuracy(y_pred, Y_train)
print ("train accuracy :", train_accuracy)

y_pred = predict(X_test, W1, W2, b1, b2)
test_accuracy = accuracy(y_pred, Y_test)
print ("test accuracy :", test_accuracy)



