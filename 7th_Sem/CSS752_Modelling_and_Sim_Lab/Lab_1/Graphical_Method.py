from shapely.geometry import LineString
from matplotlib import pyplot as plt 
import numpy as np 

# Plot lines
x = [0, 250]
y = [500, 0]

plt.plot(x, y)

x = [150, 150]
y = [0, 500]

plt.plot(x, y)

x = [0, 500]
y = [250, 250]

plt.plot(x, y)

x = [0, 500]
y = [0, 0]

plt.plot(x, y)

x = [0, 0]
y = [0, 500]

plt.plot(x, y)

# Labels
plt.legend(["2x+y <= 500", "x <= 150", "y <= 250", "y = 0", "x = 0"])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Prob 2')

# define lines calculate inersection points
l1 = LineString([(250, 0), (0, 500)])
l2 = LineString([(150, 0), (150, 500)])
l3 = LineString([(0, 250), (500, 250)])
i1 = l1.intersection(l2)
i2 = l2.intersection(l3)
i3 = l3.intersection(l1)

# plot and print intersection points
plt.plot(*i1.xy, 'o')
plt.plot(*i2.xy, 'o')
plt.plot(*i3.xy, 'o')
plt.plot(0, 250, 'o')
plt.plot(150, 0, 'o')

prn = f"Intersection points are: \nA({i1.xy[0][0]}, {i1.xy[1][0]}) \nB({i2.xy[0][0]}, {i2.xy[1][0]}) \nC({i3.xy[0][0]}, {i3.xy[1][0]}) \nD(0, 250) \nE(150, 0)"
print(prn)


# shade solution region
x = [0, i3.xy[0][0], i1.xy[0][0], 150]
y = [250, i3.xy[1][0], i1.xy[1][0], 0]
plt.fill_between(x, y, color='blue', alpha=0.2)


# Show result
plt.show()