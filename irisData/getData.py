from ucimlrepo import fetch_ucirepo
import pandas as pd


class Iris:
    def __init__(self):
        self.data = []
        self.label = []
        self.completeData = []
        self.columnNames = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
        self.readData()

    def readData(self):
        iris = fetch_ucirepo(id=53)
        self.data = iris.data.features
        self.label = iris.data.targets
        combined = pd.concat([self.data, self.label], axis=1)
        self.completeData = combined.values.tolist()
