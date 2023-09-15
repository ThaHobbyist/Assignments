from shapely.geometry import LineString
from matplotlib import pyplot as plt 
import numpy as np 

# Plot lines
x = [0, 2]
y = [10, 0]

plt.plot(x, y)

x = [0, 6]
y = [6, 0]

plt.plot(x, y)

x = [0, 12]
y = [3, 0]

plt.plot(x, y)

x = [0, 13]
y = [0, 0]

plt.plot(x, y)

x = [0, 0]
y = [0, 13]

plt.plot(x, y)

# Labels
plt.legend(["5x+y=10", "x+y=6", "x+4y=12", "y=0", "x=0"])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Prob 1')

# define lines calculate inersection points
l1 = LineString([(2, 0), (0, 10)])
l2 = LineString([(6, 0), (0, 6)])
l3 = LineString([(12, 0), (0, 3)])
i1 = l1.intersection(l2)
i2 = l2.intersection(l3)

# plot and print intersection points
plt.plot(*i1.xy, 'o')
plt.plot(*i2.xy, 'o')
plt.plot(0, 10, 'o')
plt.plot(12, 0, 'o')

prn = f"Intersection points are: \nA({i1.xy[0][0]}, {i1.xy[1][0]}) \nB({i2.xy[0][0]}, {i2.xy[1][0]}) \nC(0, 10) \nD(12, 0)"
print(prn)

'''
# shade solution region
x = [0, p[0], 300]
y = [450, q[0], 0]
plt.fill_between(x, y, color='blue', alpha=0.2)
'''

# Show result
plt.show()