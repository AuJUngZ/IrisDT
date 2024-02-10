import numpy as np

from DTreeFunction import *


# วน loop เพื่อนับข้อมูล แยกตามรายละเอียด attb และ class
def fillTable(data, sepal_length, sepal_width, sepal_length_ci, sepal_width_ci, classes):
    for row in data:
        for i in range(len(row) - 1):
            if i == 0:
                if row[i] == 'sepal_length_L':
                    sepal_length[0] += 1
                    if row[2] == 'Iris-versicolor':
                        sepal_length_ci[0][0] += 1
                    elif row[2] == 'Iris-virginica':
                        sepal_length_ci[0][1] += 1
                elif row[i] == 'sepal_length_M':
                    sepal_length[1] += 1
                    if row[2] == 'Iris-versicolor':
                        sepal_length_ci[1][0] += 1
                    elif row[2] == 'Iris-virginica':
                        sepal_length_ci[1][1] += 1
                elif row[i] == 'sepal_length_H':
                    sepal_length[2] += 1
                    if row[2] == 'Iris-versicolor':
                        sepal_length_ci[2][0] += 1
                    elif row[2] == 'Iris-virginica':
                        sepal_length_ci[2][1] += 1

            elif i == 1:
                if row[i] == 'sepal_width_L':
                    sepal_width[0] += 1
                    if row[2] == 'Iris-versicolor':
                        sepal_width_ci[0][0] += 1
                    elif row[2] == 'Iris-virginica':
                        sepal_width_ci[0][1] += 1
                elif row[i] == 'sepal_width_M':
                    sepal_width[1] += 1
                    if row[2] == 'Iris-versicolor':
                        sepal_width_ci[1][0] += 1
                    elif row[2] == 'Iris-virginica':
                        sepal_width_ci[1][1] += 1
                elif row[i] == 'sepal_width_H':
                    sepal_width[2] += 1
                    if row[2] == 'Iris-versicolor':
                        sepal_width_ci[2][0] += 1
                    elif row[2] == 'Iris-virginica':
                        sepal_width_ci[2][1] += 1

    # นับจำนวนพันธุ์ดอกแต่ละชนิด
    for row in data:
        if row[2] == 'Iris-versicolor':
            classes[0] += 1
        elif row[2] == 'Iris-virginica':
            classes[1] += 1


def thirdIterated(data):
    classes = np.zeros(2)  # มี 3 class Iris-versicolor, Iris-virginica

    sepal_length_ci = [[0 for i in range(3)] for i in range(3)]  # 3*3
    sepal_width_ci = [[0 for i in range(3)] for i in range(3)]  # 3*3

    sepal_length = np.zeros(3)  # มี 2 class
    sepal_width = np.zeros(3)

    fillTable(data, sepal_length, sepal_width, sepal_length_ci,
              sepal_width_ci, classes)
    # calculate information gain of dataset and attb
    InD = entropy2([classes[0], classes[1]])

    #     คำนวณ entropy ของแต่ละ CI row
    sepal_length_ci[0][2] = entropy2([sepal_length_ci[0][0], sepal_length_ci[0][1]])
    sepal_length_ci[1][2] = entropy2([sepal_length_ci[1][0], sepal_length_ci[1][1]])

    sepal_width_ci[0][2] = entropy2([sepal_width_ci[0][0], sepal_width_ci[0][1]])
    sepal_width_ci[1][2] = entropy2([sepal_width_ci[1][0], sepal_width_ci[1][1]])



    #   หาค่า gain
    Info_sepalLength = inforD(sepal_length, [sepal_length_ci[0][2], sepal_length_ci[1][2], sepal_length_ci[2][2]])
    Info_sepalWidth = inforD(sepal_width, [sepal_width_ci[0][2], sepal_width_ci[1][2], sepal_width_ci[2][2]])

    print("\n***Gain results of all dataset 3st round***")
    print("Gain (sepal_length) is %5.3f" % (InD - Info_sepalLength))
    print("Gain (sepal_width) is %5.3f" % (InD - Info_sepalWidth))

    print("\n*** CI table***")
    print("sepal_length_ci", sepal_length_ci)
    print("sepal_width_ci", sepal_width_ci)