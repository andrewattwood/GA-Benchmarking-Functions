import matplotlib.pyplot as plt
from gabenchmark import rastrigins, sphere, rosenbrock
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np


#initial arrays for Rastrigin's Function
x = np.linspace(-5.12,5.12,100)
y = np.linspace(-5.12,5.12,100)
z = np.zeros((100,100))


#initial arrays for rosenbrock Function
x = np.linspace(-5.12,5.12,100)
y = np.linspace(-5.12,5.12,100)



## compute rastrigins
##rastrigins(x,y,z)
##x, y = np.meshgrid(x,y)

## compute sphere
#sphere(x,y)

# compute rosenbrock
rosenbrock(x,y)

#plot rastrigins
#fig = plt.figure()
#ax = Axes3D(fig)
#ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='hot')
#plt.show()

#plot sphere
#plt.plot(y)
#plt.show()

#plot rosenbrock
plt.plot(y)
plt.show()
