import numpy as np

from Iterate.firstRound import *
from DTreeFunction import *
from dataPreProcess.preprocess import IrisPreprocess
from irisData.getData import Iris

iris_instance = Iris()
preprocess_instance = IrisPreprocess(iris_instance.completeData)
data_normalized = preprocess_instance.normalize()
#     รอบแรก
#     self.columnNames = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
classes = np.zeros(3)
InD = 0
firstIterated(classes, InD, data_normalized)
