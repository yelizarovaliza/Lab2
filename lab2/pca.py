import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt

image_raw = imread("photo.jpg")
print(image_raw.shape)


image_sum = image_raw.sum(axis = 2)
print(image_sum.shape)
image_bw = image_sum/image_sum.max()
print(image_bw.max())
