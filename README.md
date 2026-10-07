# lab-calc

A small Python tool for processing repeated measurements from lab work: it computes the mean, standard deviation and confidence error of a series of values.

## Features

- Reads measurements from a CSV file (one column of numbers)
- Mean value
- Sample standard deviation (n - 1)
- Standard deviation of the mean
- Confidence error using Student's t-distribution (default confidence level: 0.95)

## Requirements

- Python 3.10+
- scipy

```
pip install -r requirements.txt
```

## Usage

```
python main.py
```

Enter the path to your CSV file when prompted, for example `data/example.csv`.

Example output:

```
Mean: 3.0
Std: 1.5811388300841898
Std of means: 0.7071067811865476
Confidence error: 1.9632431614775572
```

## Input format

A CSV file with one column of numbers, one measurement per row. Use a dot as the decimal separator:

```
1
2
3
4
5
```

## Formulas

- Mean: `x̄ = Σxᵢ / n`
- Standard deviation: `s = sqrt(Σ(xᵢ - x̄)² / (n - 1))`
- Standard deviation of the mean: `s / sqrt(n)`
- Confidence error: `t(p, n - 1) · s / sqrt(n)`, where `t` is the Student coefficient

## Tests

```
python test_calc.py
```

## Roadmap

- Indirect measurements (error propagation for an arbitrary formula)
- Plots with error bars and least-squares fit
- Export results to a report