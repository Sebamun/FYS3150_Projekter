

import numpy as np
import matplotlib.pyplot as plt
infileVV = open('PlanetsVV_3.txt', 'r')
infileEU = open('PlanetsEU_2.txt', 'r')
lines = infileVV.readlines()
xVV = np.zeros(len(lines))
yVV = np.zeros(len(lines))
zVV = np.zeros(len(lines))
x1VV = np.zeros(len(lines))
y1VV = np.zeros(len(lines))
z1VV = np.zeros(len(lines))
for i in range(1,len(lines)):
    vals = lines[i].split()
    xVV[i] = float(vals[3])
    yVV[i] = float(vals[4])
    zVV[i] = float(vals[5])
    x1VV[i] = float(vals[6])
    y1VV[i] = float(vals[7])
    z1VV[i] = float(vals[8])


lines = infileEU.readlines()
xEU = np.zeros(len(lines))
yEU = np.zeros(len(lines))
zEU = np.zeros(len(lines))
x1EU = np.zeros(len(lines))
y1EU = np.zeros(len(lines))
z1EU = np.zeros(len(lines))
for i in range(1,len(lines)):
    vals = lines[i].split()
    xEU[i] = float(vals[3])
    yEU[i] = float(vals[4])
    zEU[i] = float(vals[5])
    x1EU[i] = float(vals[6])
    y1EU[i] = float(vals[7])
    z1EU[i] = float(vals[8])


#ax = plt.axes(projection='3d')
#ax.plot3D(x, y, z, 'gray')
#plt.show()
#plt.plot(xEU[1:], yEU[1:])
plt.axis('equal')
plt.tight_layout()
#plt.show()

plt.plot(xVV[1:], yVV[1:])
#plt.plot(x1,y1)
plt.axis('equal')
plt.tight_layout()
plt.show()
