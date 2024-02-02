class IrisPreprocess:

    def __init__(self, data):
        self.data = data

    def minMax4EachColumn(self):
        min_max = list()
        for i in range(len(self.data[0])):
            col_values = [row[i] for row in self.data]
            value_min = min(col_values)
            value_max = max(col_values)
            min_max.append([value_min, value_max])
        return min_max

    def normalize(self):
        # tuple 0 is sepal_length, tuple 1 is sepal_width, tuple 2 is petal_length, tuple 3 is petal_width
        # tuple 0 : A [4.3,6.1] B [6.1,7.9]
        # tuple 1 : C [2.0,3.2] D [3.2,4.4]
        # tuple 2 : E [1.0,3.95] F [3.95,6.9]
        # tuple 3 : G [0.1,1.3] H [1.3,2.5]

        for row in self.data:
            for i in range(len(row) - 1):
                if i == 0:
                    if 4.3 <= row[i] <= 6.1:
                        row[i] = 'A'
                    elif 6.1 <= row[i] <= 7.9:
                        row[i] = 'B'
                elif i == 1:
                    if 2.0 <= row[i] <= 3.2:
                        row[i] = 'C'
                    elif 3.2 <= row[i] <= 4.4:
                        row[i] = 'D'
                elif i == 2:
                    if 1.0 <= row[i] <= 3.95:
                        row[i] = 'E'
                    elif 3.95 <= row[i] <= 6.9:
                        row[i] = 'F'
                elif i == 3:
                    if 0.1 <= row[i] <= 1.3:
                        row[i] = 'G'
                    elif 1.3 <= row[i] <= 2.5:
                        row[i] = 'H'
        return self.data
