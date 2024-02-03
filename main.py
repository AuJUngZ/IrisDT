import Iterate.firstRound
import Iterate.secondRound
import Iterate.thirdRound
from DtreeModel import TestDTreeModel
from dataPreProcess.preprocess import IrisPreprocess
from irisData.getData import Iris

iris_instance = Iris()
preprocess_instance = IrisPreprocess(iris_instance.completeData)
data_firstRound = preprocess_instance.transformation()
#     รอบแรก
#     self.columnNames = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
Iterate.firstRound.firstIterated(data_firstRound)  # result show that petal_length is root node

# แยกออกได้เป็น 3 กลุ่ม คือ L M H แต่ L กับ H สามารถทำนายได้เลย ดังนั้นจะแยกทำต่อเฉพาะ M

dataset_PetalLength_M = list()
for row in data_firstRound:
    if row[2] == 'petal_length_M':
        # drop petal_length column
        row.pop(2)
        dataset_PetalLength_M.append(row)

Iterate.secondRound.secondIterated(dataset_PetalLength_M)  # result show that petal_width has the most information gain

# แยกออกได้เป็น 3 กลุ่ม คือ L M H แต่ H สามารถทำนายได้เลย ดังนั้นจะแยกทำต่อเฉพาะ L M และเนื่องจาก L ไม่ปรากฏใน petal_width จึงเลือกทำต่อเฉพาะ M
dataset_PetalWidth_M = list()
for row in dataset_PetalLength_M:
    if row[2] == 'petal_width_M':
        # drop petal_width column
        row.pop(2)
        dataset_PetalWidth_M.append(row)

Iterate.thirdRound.thirdIterated(dataset_PetalWidth_M)  # result show that sepal_length has the most information gain
