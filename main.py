from calc import std, std_of_means, mean, confidence_error, read_data

path = input('Write path to CSV file: ')
values = read_data(path)

print(f"Mean: {mean(values):.4f}\nStd: {std(values):.4f}\nStd of means: {std_of_means(values):.4f}\nConfidence error: {confidence_error(values):.4f}")