# Lab 2: Support Vector Machine (SVM) Implementation in AMPL

## Overview

This project is part of Lab 2 for the **Optimization and Data Mining (OTDM)** course at UPC Barcelona. The objective is to implement a Support Vector Machine (SVM) in **AMPL** (A Mathematical Programming Language) to classify data effectively. The project covers the mathematical foundations of SVM, its implementation in AMPL, and its evaluation on various datasets.

### Authors
- **Emilien L'Haridon** - [emilien.l.haridon@estudiantat.upc.edu](mailto:emilien.l.haridon@estudiantat.upc.edu)  
- **Gatien Dupont** - [gatien.dupont@estudiantat.upc.edu](mailto:gatien.dupont@estudiantat.upc.edu)

---

## Mathematical Background

Support Vector Machines (SVMs) are supervised learning models used for classification and regression tasks. The goal is to identify the hyperplane that best separates data into distinct classes. This project implements the SVM using two formulations:

### 1. Primal Formulation

The **primal formulation** minimizes a trade-off between the margin size and classification error:

$$
\min_{w, \gamma, s} \frac{1}{2} \|w\|^2 + \nu \sum_{i=1}^{m} s_i
$$

subject to:

$$
y_i (w^T x_i + \gamma) \geq 1 - s_i, \quad s_i \geq 0, \quad \forall i.
$$

### 2. Dual Formulation

The **dual formulation** maximizes a function of the Lagrange multipliers subject to constraints on their values:

$$
\max_{\lambda} \sum_{i=1}^{m} \lambda_i - \frac{1}{2} \sum_{i=1}^{m} \sum_{j=1}^{m} \lambda_i \lambda_j y_i y_j (x_i^T x_j)
$$

subject to:

$$
\sum_{i=1}^{m} \lambda_i y_i = 0, \quad 0 \leq \lambda_i \leq \nu, \quad \forall i.
$$

---

## Implementation

### Model Files

The implementation is split into the following AMPL model files:

- **`svm_primal.mod`**: Contains the primal formulation of the SVM.
- **`svm_dual.mod`**: Contains the dual formulation of the SVM.

### Training and Testing

The `svm_train_test.run` file automates the training and testing of the SVM on provided datasets. The results are exported as `.txt` files for further analysis.

A Python script, `result.py`, consolidates these results into a single file, `combined_results{dataset}.txt`, for easier interpretation.

---

## Datasets

### 1. Generated Data

A synthetic dataset is generated using the **`gensvmdat`** executable provided by the course instructor.

### 2. Universal Bank Data

A real-world dataset, **`raw_data/UniversalBank.csv`**, is used to test the SVM implementation under practical conditions. This dataset was taken from [SVM Classification - Kaggle](https://www.kaggle.com/datasets/vinod00725/svm-classification?resource=download&select=UniversalBank.csv).

---

## Data Processing

The following Python scripts are used to preprocess the datasets and convert them for use in AMPL:

- **`convert-dataset.py`**: Converts raw data files into the required AMPL input format.
- **`convert-csv-ampl.py`**: Processes the Universal Bank CSV file:
  - Normalizes the features.
  - Splits the data into training and testing sets.
  - Converts the data into an AMPL-readable format.

---

## Results

### Synthetic dataset : 100 samples.
On the synthetic dataset, using only 100 elements for training and testing, the SVM achieved an accuracy of 0.9.

```
Primal results:
w [*] :=
1  2.64397
2  1.76834
3  2.40685
4  2.27584
;

gamma = -4.44252

Dual results:
Computed w:
w [*] :=
1  2.64402
2  1.76838
3  2.40688
4  2.27584
;

Computed gamma:
gamma = -4.44257

Misclassifications:
misclassifications = 10

Accuracy:
accuracy = 0.9
```

### Synthetic dataset : 2000 samples.
Using more samples to train, the SVM improves and reach an accuracy of 0.93.

```
Primal results:
w [*] :=
1  3.60723
2  3.92288
3  3.58943
4  4.06435
;

gamma = -7.63824

Dual results:
Computed w:
w [*] :=
1  3.60723
2  3.92288
3  3.58943
4  4.06435
;

Computed gamma:
gamma = -7.63824

Misclassifications:
misclassifications = 70

Accuracy:
accuracy = 0.93
```



### "Real-world" dataset : Universal Bank data.
On the "real-world" example, the SVM also improves, thanks to the quantity of data and the number of features, to reach an accuracy of 0.9428.

```
Primal results:
w [*] :=
 1   0.00156131
 2   0.0753785
 3   2.65135
 4   0.0461437
 5   0.33201
 6   0.628581
 7   1.04429
 8   0.143253
 9  -0.347506
10   1.32312
11  -0.117587
12  -0.209396
;

gamma = -3.18631

Dual results:
Computed w:
w [*] :=
 1   0.0015612
 2   0.0753784
 3   2.65135
 4   0.0461437
 5   0.33201
 6   0.628581
 7   1.04429
 8   0.143253
 9  -0.347506
10   1.32312
11  -0.117587
12  -0.209396
;

Computed gamma:
gamma = -3.18631

Misclassifications:
misclassifications = 143

Accuracy:
accuracy = 0.9428
```





