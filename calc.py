import csv
from math import *
from scipy import stats


def read_data(path):
    csv_values = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                csv_values.append(float(row[0].replace(',', '.')))

    return csv_values


def mean(xs):
    return sum(xs)/len(xs)


def std(xs):
    avg = mean(xs)
    res = 0
    for i in xs:
        res += (i - avg)**2
    return sqrt(res/(len(xs)-1))


def std_of_means(xs):
    return std(xs)/sqrt(len(xs))


def confidence_error(xs, p=0.95):
    q = (1+p)/2
    df = len(xs)-1
    return stats.t.ppf(q, df)*std_of_means(xs)
