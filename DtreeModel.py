import unittest


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
    test_data = [
        ['sepal_length_M', 'sepal_width_H', 'petal_length_L', 'petal_width_L', 'Iris-setosa'],
        ['sepal_length_L', 'sepal_width_H', 'petal_length_L', 'petal_width_L', 'Iris-setosa'],
        ['sepal_length_H', 'sepal_width_M', 'petal_length_M', 'petal_width_M', 'Iris-versicolor'],
        ['sepal_length_M', 'sepal_width_M', 'petal_length_M', 'petal_width_M', 'Iris-versicolor'],
        ['sepal_length_H', 'sepal_width_M', 'petal_length_M', 'petal_width_M', 'Iris-versicolor'],
        ['sepal_length_M', 'sepal_width_L', 'petal_length_M', 'petal_width_M', 'Iris-versicolor'],
        ['sepal_length_M', 'sepal_width_M', 'petal_length_M', 'petal_width_M', 'Iris-versicolor'],
        ['sepal_length_M', 'sepal_width_L', 'petal_length_M', 'petal_width_M', 'Iris-versicolor'],
        ['sepal_length_M', 'sepal_width_M', 'petal_length_M', 'petal_width_M', 'Iris-versicolor'],
        ['sepal_length_M', 'sepal_width_M', 'petal_length_H', 'petal_width_H', 'Iris-virginica'],
        ['sepal_length_M', 'sepal_width_M', 'petal_length_M', 'petal_width_M', 'Iris-virginica'],
        ['sepal_length_H', 'sepal_width_M', 'petal_length_H', 'petal_width_H', 'Iris-virginica'],
        ['sepal_length_M', 'sepal_width_M', 'petal_length_H', 'petal_width_M', 'Iris'],
        ['sepal_length_M', 'sepal_width_M', 'petal_length_M', 'petal_width_H', 'Iris-virginica'],
        ['sepal_length_M', 'sepal_width_M', 'petal_length_M', 'petal_width_H', 'Iris-virginica'],
        ['sepal_length_M', 'sepal_width_M', 'petal_length_M', 'petal_width_M', 'Iris-virginica']
    ]
    count = 0
    correct = 0
    for row in test_data:
        count += 1
        if row[4] == IrisDTreeModel(row[0], row[1], row[2], row[3]):
            correct += 1
    print('Correct:', correct, 'Total:', count)
    print('Accuracy:', correct / count)


if __name__ == '__main__':
    TestDTreeModel()
