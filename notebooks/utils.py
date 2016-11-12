#!/usr/bin/python
# coding: utf-8

import matplotlib.pyplot as plt
from matplotlib import offsetbox
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def plot_embedding(embedded_set, original_set, title=None):
    x_min, x_max = np.min(embedded_set, 0), np.max(embedded_set, 0)
    embedded_set = (embedded_set - x_min) / (x_max - x_min)

    plt.figure()
    ax = plt.subplot(111)
    for i in range(embedded_set.shape[0]):
        plt.text(embedded_set[i, 0], embedded_set[i, 1], str(original_set.target[i]),
                 color=plt.cm.Set1(original_set.target[i] / 10.),
                 fontdict={'weight': 'bold', 'size': 9})

    if hasattr(offsetbox, 'AnnotationBbox'):
        # only print thumbnails with matplotlib > 1.0
        shown_images = np.array([[1., 1.]])  # just something big
        for i in range(embedded_set.shape[0]):
            dist = np.sum((embedded_set[i] - shown_images) ** 2, 1)
            if np.min(dist) < 4e-3:
                # don't show points that are too close
                continue
            shown_images = np.r_[shown_images, [embedded_set[i]]]
            imagebox = offsetbox.AnnotationBbox(
                offsetbox.OffsetImage(original_set.images[i], cmap=plt.cm.gray_r),
                embedded_set[i])
            ax.add_artist(imagebox)
    plt.xticks([]), plt.yticks([])
    if title is not None:
        plt.title(title)


def plot_3D(X, color):
    fig = plt.figure()
    try:
        # compatibility matplotlib < 1.0
        ax = fig.add_subplot(211, projection='3d')
        ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)
    except:
        ax = fig.add_subplot(211)
        ax.scatter(X[:, 0], X[:, 2], c=color, cmap=plt.cm.Spectral)

    plt.show()


def plot_2D(X, color):
    fig = plt.figure()
    ax = fig.add_subplot(212)
    ax.scatter(X[:, 0], X[:, 1], c=color, cmap=plt.cm.Spectral)
    plt.axis('tight')
    plt.xticks([]), plt.yticks([])
    plt.show()


def show_digits(digits, rows=20, cols=20):
    img = np.zeros((10 * rows, 10 * cols))
    for i in range(rows):
        ix = 10 * i + 1
        for j in range(cols):
            iy = 10 * j + 1
            img[ix:ix + 8, iy:iy + 8] = digits.data[i * cols + j].reshape((8, 8))

    plt.imshow(img, cmap=plt.cm.binary)
    plt.show()
