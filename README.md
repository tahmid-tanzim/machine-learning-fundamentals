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

**Linear Regression Model**
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
J(w,b) = \left(1 \over 2m \right) \sum_{i=0}^{m-1} (ŷ^{(i)} - y^{(i)})^2
```
or
```math
J(w,b) = \left(1 \over 2m \right) \sum_{i=0}^{m-1} (f_{w,b}(x^{(i)}) - y^{(i)})^2
```
or
```math
J(w,b) = \left(1 \over 2m \right) \sum_{i=0}^{m-1} ((w * x^{(i)} + b) - y^{(i)})^2
```
The cost function is denoted as $`J(w,b)`$ also known squared error cost function.

Find $`w, b`$: $`ŷ^{(i)}`$ is close to $`y^{(i)}`$ for all ($`x^{(i)}, y^{(i)}`$)


##### Gradient Descent
Goal is to minimize the cost i.e. $`min_{w,b} J(w,b)`$

Start with some $`w,b`$ keep changing $`w,b`$ to reduce $`J(w,b)`$ until we settle at or near a minimum.

##### Gradient Descent Algorithms
Repeat until convergence

$`\alpha`$ is Learning Rate

$`\partial`$ is derivatives

So far we have developed a linear model that predicts $`f_{w,b}(x^{(i)})`$:
```math
f_{w,b}(x^{(i)}) = wx^{(i)} + b \tag{1}
```
In linear regression, we utilize input training data to fit the parameters $`w`$,$`b`$ by minimizing a measure of the error between our predictions $`f_{w,b}(x^{(i)})`$ and the actual data $`y^{(i)}`$. The measure is called the $`cost`$, $`J(w,b)`$. In training we measure the cost over all of our training samples $`x^{(i)},y^{(i)}`$
```math
J(w,b) = \frac{1}{2m} \sum\limits_{i = 0}^{m-1} (f_{w,b}(x^{(i)}) - y^{(i)})^2\tag{2}
``` 

```math
\begin{align*} \text{repeat}&\text{ until convergence:} \; \lbrace \newline
\;  w &= w -  \alpha \frac{\partial J(w,b)}{\partial w} \tag{3}  \; \newline 
 b &= b -  \alpha \frac{\partial J(w,b)}{\partial b}  \newline \rbrace
\end{align*}
```

where, parameters $`w`$, $`b`$ are updated simultaneously.  
The gradient is defined as:
```math
\begin{align}
\frac{\partial J(w,b)}{\partial w}  &= \frac{1}{m} \sum\limits_{i = 0}^{m-1} (f_{w,b}(x^{(i)}) - y^{(i)})x^{(i)} \tag{4}\\
  \frac{\partial J(w,b)}{\partial b}  &= \frac{1}{m} \sum\limits_{i = 0}^{m-1} (f_{w,b}(x^{(i)}) - y^{(i)}) \tag{5}\\
\end{align}
```

Here *simultaneously* means that you calculate the partial derivatives for all the parameters before updating any of the parameters.

#### Multiple Linear Regression
* $`\vec x`$ = [$`x_1, x_2, x_3 ..... x_n`$]
* $`\vec x_j`$ = $`j^{th}`$ feature
* $`n`$ = number of features 
* $`\vec x^{(i)}`$ = features of $`i^{th}`$ training example
* $`\vec x_j^{(i)}`$ = the value of features $`j`$ in $`i^{th}`$ training example

### Model Prediction With Multiple Variables


```math
f_{\vec w,b}(\vec x) = \vec w . \vec x + b
```

Here
```math
\vec w . \vec x = w_1 * x_1 + w_2 * x_2 + w_3 * x_3 .... w_n * x_n
```

#### Vectorization
```math
f = np.dot(w, x) + b
```

#### Compute Cost With Multiple Variables
The equation for the cost function with multiple variables $J(\mathbf{w},b)$ is:
$$J(\mathbf{w},b) = \frac{1}{2m} \sum\limits_{i = 0}^{m-1} (f_{\mathbf{w},b}(\mathbf{x}^{(i)}) - y^{(i)})^2$$ 

where:
$$f_{\mathbf{w},b}(\mathbf{x}^{(i)}) = \mathbf{w} \cdot \mathbf{x}^{(i)} + b$$ 


In contrast to previous labs, $\mathbf{w}$ and $\mathbf{x}^{(i)}$ are vectors rather than scalars supporting multiple features.

#### Gradient Descent With Multiple Variables
Gradient descent for multiple variables:

$$\begin{align*} \text{repeat}&\text{ until convergence:} \; \lbrace \newline\;
& w_j = w_j -  \alpha \frac{\partial J(\mathbf{w},b)}{\partial w_j}  \; & \text{for j = 0..n-1}\newline
&b\ \ = b -  \alpha \frac{\partial J(\mathbf{w},b)}{\partial b}  \newline \rbrace
\end{align*}$$

where, n is the number of features, parameters $w_j$,  $b$, are updated simultaneously and where  

$$
\begin{align}
\frac{\partial J(\mathbf{w},b)}{\partial w_j}  &= \frac{1}{m} \sum\limits_{i = 0}^{m-1} (f_{\mathbf{w},b}(\mathbf{x}^{(i)}) - y^{(i)})x_{j}^{(i)}  \\
\frac{\partial J(\mathbf{w},b)}{\partial b}  &= \frac{1}{m} \sum\limits_{i = 0}^{m-1} (f_{\mathbf{w},b}(\mathbf{x}^{(i)}) - y^{(i)})
\end{align}
$$
* m is the number of training examples in the data set

    
*  $f_{\mathbf{w},b}(\mathbf{x}^{(i)})$ is the model's prediction, while $y^{(i)}$ is the target value



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