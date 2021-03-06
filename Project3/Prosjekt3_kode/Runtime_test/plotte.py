import numpy as np
import matplotlib.pyplot as plt
infile_EU = open('posisjonEU.txt', 'r')
lines_EU = infile_EU.readlines()
x_EU = np.zeros(len(lines_EU))
y_EU = np.zeros(len(lines_EU))
infile_VV = open('posisjonVV.txt', 'r')
lines_VV = infile_VV.readlines()
x_VV = np.zeros(len(lines_VV))
y_VV = np.zeros(len(lines_VV))
for i in range(1,len(lines_EU)):
    vals_VV = lines_VV[i].split()
    x_VV[i] = float(vals_VV[0])
    y_VV[i] = float(vals_VV[1])
    vals_EU = lines_EU[i].split()
    x_EU[i] = float(vals_EU[0])
    y_EU[i] = float(vals_EU[1])
# PLotting:
fig, axes = plt.subplots(2,1)
axes[0].plot(x_VV, y_VV)
axes[0].set_xlabel('x[AU]')
axes[0].set_ylabel('y[AU]')
axes[0].set_title('Velocity Verlet')
axes[1].plot(x_EU, y_EU)
axes[1].set_xlabel('x[AU]')
axes[1].set_ylabel('y[AU]')
axes[1].set_title('Euler')
fig.tight_layout()
plt.show()
