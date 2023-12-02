#n = open("input").read().strip()
#print(n)

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(111, projection='3d')

ax.scatter(0,0,0) # plot the point (2,3,4) on the figure

plt.show()
