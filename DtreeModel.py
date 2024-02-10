import pandas as pd
from dataPreProcess.preprocess import IrisPreprocess


def IrisDTreeModel(sepal_length, sepal_width, petal_length, petal_width):
    if petal_length == 'petal_length_L':
        return 'Iris-setosa'
    elif petal_length == 'petal_length_M':
        if petal_width == 'petal_width_L':
            return 'Unknown'
        elif petal_width == 'petal_width_M':
            if petal_length == 'petal_length_L':
                return 'Iris-versicolor'
            elif petal_length == 'petal_length_M':
                if sepal_width == 'sepal_width_L':
                    return 'Iris-versicolor'
                elif sepal_width == 'sepal_width_M':
                    return 'Iris-versicolor'
                elif sepal_width == 'sepal_width_H':
                    return 'Unknown'
            else:
                return 'Iris-versicolor'
        else:
            return 'Iris-virginica'
    else:
        return 'Iris-virginica'


def TestDTreeModel():
    training_data = IrisPreprocess(pd.read_csv('dataset/iris.csv').values.tolist()).transformation()
    count = 0
    correct = 0
    for row in training_data:
        count += 1
        if row[4] == IrisDTreeModel(row[0], row[1], row[2], row[3]):
            correct += 1
    print('Test with training data:' + '\n' + '-' * 50)
    print('Correct:', correct, 'Total:', count)
    print('Accuracy:', correct / count)

    unseen_data = IrisPreprocess(pd.read_csv('testDataset.csv').values.tolist()).transformation()
    count = 0
    correct = 0
    for row in unseen_data:
        count += 1
        if row[4] == IrisDTreeModel(row[0], row[1], row[2], row[3]):
            correct += 1
    print('\nTest with unseen data:' + '\n' + '-' * 50)
    print('Correct:', correct, 'Total:', count)
    print('Accuracy:', correct / count)


if __name__ == '__main__':
    TestDTreeModel()
