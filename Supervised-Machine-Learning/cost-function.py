import numpy as np
from chart import draw_plot_chart


def compute_cost(x, y, w, b):
    """
    Computes the cost function for linear regression.

    Args:
      x (ndarray (m,)): Data, m examples
      y (ndarray (m,)): target values
      w,b (scalar)    : model parameters

    Returns
        total_cost (float): The cost of using w,b as the parameters for linear regression
               to fit the data points in x and y
    """
    # number of training examples

    m = x.shape[0]

    cost_sum = 0
    for i in range(m):
        f_wb = w * x[i] + b
        cost = (f_wb - y[i]) ** 2
        cost_sum = cost_sum + cost
    total_cost = (1 / (2 * m)) * cost_sum

    return total_cost


def f(x, w, b):
    return w * x + b


def find_min_cost(x, y):
    w_low, w_high, w_step = 196, 226, 1
    b_low, b_high, b_step = -1.5, 5.1, 0.1

    min_cost = float('inf')
    weight, bias = w_low, b_low

    for w in range(w_low, w_high, w_step):
        for b in np.arange(b_low, b_high, b_step):
            cost = compute_cost(x, y, w, b)
            if min_cost > cost:
                min_cost = cost
                weight = w
                bias = b
                print('New Min Cost - ', min_cost, weight, bias)
    print('Cost - ', min_cost)
    print('Weight - ', weight)
    print('Bias - ', bias)


if __name__ == '__main__':
    x_train = np.array([1.0, 1.7, 2.0, 2.5, 3.0, 3.2])
    y_train = np.array([250, 300, 480, 430, 630, 730])
    # find_min_cost(x_train, y_train)
    w = 209
    b = 3.2
    y_hat = f(x_train, w, b)
    draw_plot_chart(
        {
            'chart_title': f"Housing Prices - Cost {round(compute_cost(x_train, y_train, w, b))}",
            'x_label': "Size in 1000 square feet",
            'y_label': "Price in 1000s of dollars",
            'x_train': x_train,
            'y_train': y_train,
            'y_hat': y_hat
        }
    )

