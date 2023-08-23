# Machine Learning Fundamentals

## 1. Python Virtual Env Setup

```shell
python3 -m venv venv
source venv/bin/activate
deactivate
```

Install Dependency
```shell
pip install --upgrade pip
pip freeze > requirements.txt
pip install -r requirements.txt
```

```shell
jupyter notebook
```

## 2. Supervised Learning
Learn from data _labeled_ with the **right answers**.

### 2.1. Regression Algorithms
Predict a _number infinitely_ many possible outputs. for e.g. Housing price prediction

#### 2.1.2. Linear Regression Model
(Training Set - {x: features, y: targets})
                 +
(Supervised Learning Algorithms)
                 =
[f] {function / model}

x - feature / input

ŷ (y-hat) - prediction

x ~> [f] ~> ŷ

**Model**
```math
f_{w,b}(x) = wx + b
```

So each model prediction can be written as
```math
ŷ^{(i)} == f_{w,b}(x^{(i)})
```

#### Notation
| General Notation     |           Description           |   Python variable |
|:---------------------|:-------------------------------:|------------------:|
| **x** (vector)       | Training example feature values |         `x_train` |
| **y** (vector)       |    Training example targets     |         `y_train` |
| $`x^{(i)}, y^{(i)}`$ |   $`i^{th}`$ Training example   |      `x_i`, `y_i` |
| m (scalar)           |   Number of training examples   |               `m` |
| $`w`$ (scalar)       |        parameter: weight        |               `w` |
| $`b`$ (scalar)       |         parameter: bias         |               `b` |

#### Cost Function
The cost function will tell us how well the model is doing.

Error is (Prediction - Actual Target) i.e. $`ŷ^{(i)} - y^{(i)}`$

```math
J(w,b) = \left(1 \over 2m \right) \sum_{i=1}^m (ŷ^{(i)} - y^{(i)})^2
```
or
```math
J(w,b) = \left(1 \over 2m \right) \sum_{i=1}^m (f_{w,b}(x^{(i)}) - y^{(i)})^2
```
or
```math
J(w,b) = \left(1 \over 2m \right) \sum_{i=1}^m ((w * x^{(i)} + b) - y^{(i)})^2
```
The cost function is denoted as $`J(w,b)`$ also known squared error cost function.

Find $`w, b`$: $`ŷ^{(i)}`$ is close to $`y^{(i)}`$ for all ($`x^{(i)}, y^{(i)}`$)

Goal is to minimize the cost i.e. $`J(w,b)`$


#### 2.1.2. Polynomial Regression Model



### 2.2. Classification Algorithms
Predict _categories small number_ of possible outputs. for e.g. Cancer detection - Yes / No

#### 2.2.1 Logistic Regression
#### 2.2.2. Decision Tree
#### 2.2.3. Random Forest
#### 2.2.4. Support Vector Machine (SVM)
#### 2.2.5. K-Nearest Neighbour (KNN)
#### 2.2.6. Naive Bayes

## 3. Unsupervised Learning
Find something interesting from _unlabeled_ data. 

### 3.1. Clustering Algorithms
Take _unlabeled_ data and group similar data points together.

### 3.2. Anomaly detection
Find unusual data points.

### 3.3. Dimensionality reduction
Compress data using fewer numbers.

## 4. Recommender System

## 5. Reinforcement Learning