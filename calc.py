import csv


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
    return (res/(len(xs)-1))**0.5

print(std(read_data('data/example.csv')))