"""
calculate the standard deviation of the collected measurements
"""

import pandas as pd

# ---

file_names = ['Graph1.txt', 'Graph2.txt']


def read_data():
    """
    """
    data = []

    for fname in file_names:
        single_data = pd.read_csv(fname, sep=",", header=None, skiprows=1)
        data.append(single_data)

    return data


def cal_std_deviation(data):
    """
    """
    for single_data in data:
        print(single_data.std(axis=0))

# ---

def start():
    """
    """
    data = read_data()
    cal_std_deviation(data)


if __name__ == "__main__":
    """
    """
    start()