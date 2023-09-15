from shapely.geometry import LineString
from matplotlib import pyplot as plt 
import numpy as np 

x1 = [0, 450]
y1 = [450, 0]

plt.plot(x1, y1)

x2 = [0, 300]
y2 = [600, 0]

plt.plot(x2, y2)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Prob 1')

l1 = LineString([(450, 0), (0, 450)])
l2 = LineString([(300, 0), (0, 600)])
intersec = l2.intersection(l1)

plt.plot(*intersec.xy, 'ro')
p, q = intersec.xy
print(p, q)

x = [0, p[0], 300]
y = [450, q[0], 0]

plt.fill_between(x, y, color='blue', alpha=0.2)
plt.show()