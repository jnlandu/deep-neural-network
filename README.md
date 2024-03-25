# Deep Neural Network from Scratch

In this project, we implement a single layer deep neural network from scratch using python and the basic libraries `numpy` and `matplotlib`. We implement a Python class to define, train,and evaluate the Deep Neural Network for  (binary) classification tasks. We use the Backpropagation algorithm in the class.  This version is a firsr attempt to the implementation of deep neural network. Although, it is worth mentioning that several aspects will be added to the current class to make it more general, notably:
- We will add a separate class `Layer`, that will implement the inputs and the outputs layer, in which we will implement for each layer the forward pass and associates weights, for example **ReLU**, **Leaky ReLU**, etc, instead of only sigmoid.
- etc.

References for neural network can be found in 

Detailed ddscription of the project along with with the results can be found [here](#project-description-and-results).



  ## Getting started

  The repository has actually two main files, one file implemnts the neural network without use of OPP and the other `jeremie_nn.py` does it  with OPP. For the later, there are still things to fixed since the expected outcome does not correspond to that of the first file. The details explained below are related to the file `jeremie_nn.py`.

  ### Prerequisites:

To run the codes in the file, in your local computer  the followinf need to be installed:
- numpy, go to https://numpy.org/install/ for broad details.
- matplotlib. For details about the installation, see https://matplotlib.org/stable/users/installing/index.html

If you have pip installed and working very good, they can be installed using:
 
     pip install numpy
     pip install matplotlib

Or if you have pip3, replace pip above with `pip3`.

An other alternative is to use [Google Colab](https://colab.research.google.com/) in a Web Browser without needing to install the mentioned packages.

### Usage:

The file `jeremie_nn.py` gives access to the method `fit` that one has to pass the `x_train`, `y_train`, and the corresponding test datasets. First of all, an `neuralNetwork` object must be instatiate, and this mus be done using, for example:

 
     nn = neuralNetwork(lr=0.1, n_epochs = 1000)
     nn.fit(x_train, y_train, x_test, y_test)


## Tools Used
* [NumPy](https://numpy.org/) : Used for storing and manipulating high dimensional arrays, and performing large scale mathematical computations on them.
* [Matplotlib](https://matplotlib.org/) : Used for plotting the Learning Curves.
* [Google Colab](https://colab.research.google.com/) : Used as the development environment for executing high-end computations on its backend GPUs/TPUs.

 

