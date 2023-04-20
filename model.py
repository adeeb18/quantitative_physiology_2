
import numpy as np
import matplotlib.pyplot as plt
import math

#Constants

# m constant for blood as a power law fluid
m = 1

# n constant for blood as a power law fluid
n = 1

# density of blood in kg/m^3
# Cutnell, John & Johnson, Kenneth. Physics, Fourth Edition. Wiley, 1998: 308.
rho = 1060

# Pressure
p = 1

# Sin of angle for vessel
sintheta = math.sin(45)

# acceleration due to gravity (m/s^2)
g_start =0
g_step =.01
g_stop = 10

g=np.arange(g_start, g_stop, g_step)


#Shear Stress
tau = m * np.abs(p - np.multiply(np.multiply(g,rho), sintheta)) ** n

#Plotting
fig, ax = plt.subplots()

ax.plot(g, tau, linewidth=2.0)

plt.show()