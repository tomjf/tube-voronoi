import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from numpy import genfromtxt

my_data = genfromtxt('stations.csv', delimiter=',', skip_header =1, usecols= (3,4))
# print my_data
vor = Voronoi(my_data)
voronoi_plot_2d(vor)
plt.xlim(51.4, 51.6)
plt.ylim(-0.2, 0.0)
plt.show()
