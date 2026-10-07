from calc import std, std_of_means, mean, confidence_error, read_data

path = input('Write path to CSV file: ')
values = read_data(path)

print(f"Mean: {mean(values)}\nStd: {std(values)}\nStd of means: {std_of_means(values)}\nConfidence error: {confidence_error(values)}")