from shapely.geometry import LineString
from matplotlib import pyplot as plt 
import numpy as np 

y1 = [50/4, 0]
x1 = [0, 50/3]

plt.plot(x1, y1)

y2 = [10, 0]
x2 = [0, 120/7]

plt.plot(x2, y2)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Prob 2')

l1 = LineString([(0, 50/4), (50/3, 0)])
l2 = LineString([(0, 10), (120/7, 0)])
intersec = l1.intersection(l2)

plt.plot(*intersec.xy, 'ro')
p, q = intersec.xy
print(p, q)
x = [0, p[0], 120/7]
y = [50/4, q[0], 0]
plt.fill_between(x, y, max(y), color='blue', alpha=0.2)

plt.show()