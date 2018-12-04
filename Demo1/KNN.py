'''
Started on Sep 04.2018
KNN   K-Nearest Neighbour
@author:Azure1yu
1st year learning Python and ML ^^
'''


from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    lables = ['A','A','B','B']
    return group,lables


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape(0)
