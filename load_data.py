"""
Functions to load the dataset.
"""

import numpy as np

def read_data(file_name):
    """This function is taken from:
    https://github.com/benhamner/BioResponse/blob/master/Benchmarks/csv_io.py
    """
    f = open(file_name)
    #ignore header
    f.readline()
    samples = []
    target = []
    for line in f:
        line = line.strip().split(",")
        sample = [float(x) for x in line]
        samples.append(sample)
    return samples

def load():
    """Conveninence function to load all data as numpy arrays.
    """
    print "Loading data..."
    filename_train = 'train.csv'
    filename_test = 'test.csv'

    train = read_data("train.csv")
    y_train = np.array([x[0] for x in train])
    X_train = np.array([x[1:] for x in train])
    X_test = np.array(read_data("test.csv"))
    return X_train, y_train, X_test

if __name__ == '__main__':

    X_train, y_train, X_test = load()

