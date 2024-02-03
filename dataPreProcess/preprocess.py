import pandas as pd


def assign_label(value, mean, sd, feature):
    if value < mean - sd:
        return f'{feature}_L'
    elif value > mean + sd:
        return f'{feature}_H'
    else:
        return f'{feature}_M'


class IrisPreprocess:

    def __init__(self, data):
        self.data = data

    def transformation(self):
        """
        Normalize the data
        Summary Statistics:
                           Min  Max   Mean    SD   Class Correlation
              sepal length: 4.3  7.9   5.84  0.83    0.7826
                sepal width: 2.0  4.4   3.05  0.43   -0.4194
                petal length: 1.0  6.9   3.76  1.76    0.9490  (high!)
                petal width: 0.1  2.5   1.20  0.76    0.9565  (high!)
        Idea : Spilt the data into 3 groups by middle group is Mean +- SD
        and the rest is less than Mean - SD and more than Mean + SD
        """

        summary_statistics = {
            'sepal_length': {'min': 4.3, 'max': 7.9, 'mean': 5.84, 'sd': 0.83},
            'sepal_width': {'min': 2.0, 'max': 4.4, 'mean': 3.05, 'sd': 0.43},
            'petal_length': {'min': 1.0, 'max': 6.9, 'mean': 3.76, 'sd': 1.76},
            'petal_width': {'min': 0.1, 'max': 2.5, 'mean': 1.20, 'sd': 0.76}
        }

        for i, feature in enumerate(['sepal_length', 'sepal_width', 'petal_length', 'petal_width']):
            mean = summary_statistics[feature]['mean']
            sd = summary_statistics[feature]['sd']

            for row in self.data:
                row[i] = assign_label(row[i], mean, sd, feature)

        # export csv
        with open('data.csv', 'w', newline='') as file:
            pd.DataFrame(self.data).to_csv(file, index=False,
                                           header=['sepal_length', 'sepal_width', 'petal_length', 'petal_width',
                                                   'class'])

        return self.data
