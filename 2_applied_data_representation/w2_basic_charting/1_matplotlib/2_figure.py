#!/usr/bin/python
# -*- coding:utf-8 -*-

# First let's set the backend without using mpl.use() from the scripting layer
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# 例子 1:
# create a new figure
fig = Figure()
# associate fig with the backend
canvas = FigureCanvasAgg(fig)
# add a subplot to the fig
ax = fig.add_subplot(111)
# plot the point (3,2)
ax.plot(3, 2, '.')
# save the figure to test.png
# you can see this figure in your Jupyter workspace afterwards by going to
# https://hub.coursera-notebooks.org/
# 在本地保存了该文件
canvas.print_png('2_figure.png')


def example2():
    # create a new figure
    plt.figure()
    # plot the point (3,2) using the circle marker
    plt.plot(3, 2, 'o')
    # get the current axes
    ax = plt.gca()
    # Set axis properties [xmin, xmax, ymin, ymax]
    ax.axis([0, 6, 0, 10])
    # get current axes
    ax = plt.gca()
    # get all the child objects the axes contains
    print(ax.get_children())
    plt.show()


def example3():
    # create a new figure
    plt.figure()

    # plot the point (1.5, 1.5) using the circle marker
    plt.plot(1.5, 1.5, 'o')
    # plot the point (2, 2) using the circle marker
    plt.plot(2, 2, 'o')
    # plot the point (2.5, 2.5) using the circle marker
    plt.plot(2.5, 2.5, 'o')
    plt.show()


example2()
example3()
