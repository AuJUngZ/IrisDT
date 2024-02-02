import numpy as np

from DTreeFunction import *


# วน loop เพื่อนับข้อมูล แยกตามรายละเอียด attb และ class
def fillTable(data_normalized, sepal_length, sepal_width, petal_length, petal_width, sepal_length_ci, sepal_width_ci,
              petal_length_ci, petal_width_ci, classes):
    for row in data_normalized:
        for i in range(len(row) - 1):
            if i == 0:
                if row[i] == 'A':
                    sepal_length[0] += 1
                elif row[i] == 'B':
                    sepal_length[1] += 1
                if row[i] == 'A' and row[4] == 'Iris-setosa':
                    sepal_length_ci[0][0] += 1
                elif row[i] == 'A' and row[4] == 'Iris-versicolor':
                    sepal_length_ci[0][1] += 1
                elif row[i] == 'A' and row[4] == 'Iris-virginica':
                    sepal_length_ci[0][2] += 1
                elif row[i] == 'B' and row[4] == 'Iris-setosa':
                    sepal_length_ci[1][0] += 1
                elif row[i] == 'B' and row[4] == 'Iris-versicolor':
                    sepal_length_ci[1][1] += 1
                elif row[i] == 'B' and row[4] == 'Iris-virginica':
                    sepal_length_ci[1][2] += 1
            elif i == 1:
                if row[i] == 'C':
                    sepal_width[0] += 1
                elif row[i] == 'D':
                    sepal_width[1] += 1
                if row[i] == 'C' and row[4] == 'Iris-setosa':
                    sepal_width_ci[0][0] += 1
                elif row[i] == 'C' and row[4] == 'Iris-versicolor':
                    sepal_width_ci[0][1] += 1
                elif row[i] == 'C' and row[4] == 'Iris-virginica':
                    sepal_width_ci[0][2] += 1
                elif row[i] == 'D' and row[4] == 'Iris-setosa':
                    sepal_width_ci[1][0] += 1
                elif row[i] == 'D' and row[4] == 'Iris-versicolor':
                    sepal_width_ci[1][1] += 1
                elif row[i] == 'D' and row[4] == 'Iris-virginica':
                    sepal_width_ci[1][2] += 1
            elif i == 2:
                if row[i] == 'E':
                    petal_length[0] += 1
                elif row[i] == 'F':
                    petal_length[1] += 1
                if row[i] == 'E' and row[4] == 'Iris-setosa':
                    petal_length_ci[0][0] += 1
                elif row[i] == 'E' and row[4] == 'Iris-versicolor':
                    petal_length_ci[0][1] += 1
                elif row[i] == 'E' and row[4] == 'Iris-virginica':
                    petal_length_ci[0][2] += 1
                elif row[i] == 'F' and row[4] == 'Iris-setosa':
                    petal_length_ci[1][0] += 1
                elif row[i] == 'F' and row[4] == 'Iris-versicolor':
                    petal_length_ci[1][1] += 1
                elif row[i] == 'F' and row[4] == 'Iris-virginica':
                    petal_length_ci[1][2] += 1
            elif i == 3:
                if row[i] == 'G':
                    petal_width[0] += 1
                elif row[i] == 'H':
                    petal_width[1] += 1
                if row[i] == 'G' and row[4] == 'Iris-setosa':
                    petal_width_ci[0][0] += 1
                elif row[i] == 'G' and row[4] == 'Iris-versicolor':
                    petal_width_ci[0][1] += 1
                elif row[i] == 'G' and row[4] == 'Iris-virginica':
                    petal_width_ci[0][2] += 1
                elif row[i] == 'H' and row[4] == 'Iris-setosa':
                    petal_width_ci[1][0] += 1
                elif row[i] == 'H' and row[4] == 'Iris-versicolor':
                    petal_width_ci[1][1] += 1
                elif row[i] == 'H' and row[4] == 'Iris-virginica':
                    petal_width_ci[1][2] += 1

    # นับจำนวนพันธุ์ดอกแต่ละชนิด
    for row in data_normalized:
        if row[4] == 'Iris-setosa':
            classes[0] += 1
        elif row[4] == 'Iris-versicolor':
            classes[1] += 1
        elif row[4] == 'Iris-virginica':
            classes[2] += 1


def firstIterated(classes, InD, data_normalized):
    sepal_length_ci = [[0 for i in range(4)] for i in range(2)]  # 2*4
    sepal_width_ci = [[0 for i in range(4)] for i in range(2)]  # 2*4
    petal_length_ci = [[0 for i in range(4)] for i in range(2)]  # 2*4
    petal_width_ci = [[0 for i in range(4)] for i in range(2)]  # 2*4

    sepal_length = np.zeros(2)  # มี 2 class
    sepal_width = np.zeros(2)
    petal_length = np.zeros(2)
    petal_width = np.zeros(2)

    fillTable(data_normalized, sepal_length, sepal_width, petal_length, petal_width, sepal_length_ci,
              sepal_width_ci, petal_length_ci, petal_width_ci, classes)
    # calculate information gain of dataset and attb
    InD = entropy(classes[0], classes[1], classes[2])

    #     คำนวณ entropy ของแต่ละ CI row
    sepal_length_ci[0][3] = entropy(sepal_length_ci[0][0], sepal_length_ci[0][1], sepal_length_ci[0][2])
    sepal_length_ci[1][3] = entropy(sepal_length_ci[1][0], sepal_length_ci[1][1], sepal_length_ci[1][2])

    sepal_width_ci[0][3] = entropy(sepal_width_ci[0][0], sepal_width_ci[0][1], sepal_width_ci[0][2])
    sepal_width_ci[1][3] = entropy(sepal_width_ci[1][0], sepal_width_ci[1][1], sepal_width_ci[1][2])

    petal_length_ci[0][3] = entropy(petal_length_ci[0][0], petal_length_ci[0][1], petal_length_ci[0][2])
    petal_length_ci[1][3] = entropy(petal_length_ci[1][0], petal_length_ci[1][1], petal_length_ci[1][2])

    petal_width_ci[0][3] = entropy(petal_width_ci[0][0], petal_width_ci[0][1], petal_width_ci[0][2])
    petal_width_ci[1][3] = entropy(petal_width_ci[1][0], petal_width_ci[1][1], petal_width_ci[1][2])

    #   หาค่า gain
    Info_sepalLength = inforD(sepal_length, [sepal_length_ci[0][3], sepal_length_ci[1][3]])
    Info_sepalWidth = inforD(sepal_width, [sepal_width_ci[0][3], sepal_width_ci[1][3]])
    Info_petalLength = inforD(petal_length, [petal_length_ci[0][3], petal_length_ci[1][3]])
    Info_petalWidth = inforD(petal_width, [petal_width_ci[0][3], petal_width_ci[1][3]])

    print("\n***Gain results of all dataset 1st round***")
    # print("Gain (age) is %5.3f"% gainAge)
    print("Gain (sepal_length) is %5.3f" % (InD - Info_sepalLength))
    print("Gain (sepal_width) is %5.3f" % (InD - Info_sepalWidth))
    print("Gain (petal_length) is %5.3f" % (InD - Info_petalLength))
    print("Gain (petal_width) is %5.3f" % (InD - Info_petalWidth))
