# import numpy as np
import matplotlib.pyplot as plt


def draw_plot_chart(items):
    plt.style.use('fast')
    fig, ax = plt.subplots()
    ax.set_xlabel(items['x_label'], fontsize=14)
    ax.set_ylabel(items['y_label'], fontsize=14)

    ax.set_title(items['chart_title'], fontdict={'fontsize': 22, 'color': '#424242'})
    plt.plot(items['x_train'], items['y_train'], 'o')
    plt.plot(items['x_train'], items['y_hat'])
    plt.show()


# def f(x, w, b):
#     return w * x + b


# if __name__ == "__main__":
#     x_train = np.array([1.0, 1.7, 2.0, 2.5, 3.0, 3.2])
#     y_train = np.array([250, 300, 480, 430, 630, 730])
#     w = 200
#     b = -100
#     y_hat = f(x_train, w, b)
#     draw_plot_chart(
#         {
#             'chart_title': "Housing Prices",
#             'x_label': "Size in 1000 square feet",
#             'y_label': "Price in 1000s of dollars",
#             'x_train': x_train,
#             'y_train': y_train,
#             'y_hat': y_hat
#         }
#     )
