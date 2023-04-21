
import numpy as np
import matplotlib.pyplot as plt
import math

#Constants

# m constant for blood as a power law fluid (Pa*s^n / m^2)
# "Rheological properties of blood" by D.A. Fedosov and G.E. Karniadakis, published in Annual Review of Fluid Mechanics in 2014
m = 0.04 

# n constant for blood as a power law fluid (no unit)
# "Rheological properties of blood" by D.A. Fedosov and G.E. Karniadakis, published in Annual Review of Fluid Mechanics in 2014
n = .5

# density of blood in kg/m^3
# Cutnell, John & Johnson, Kenneth. Physics, Fourth Edition. Wiley, 1998: 308.
rho = 1060

# Pressure (Pa)
# "Cardiovascular Physiology Concepts" by Richard E. Klabunde,"
p = 16000

# Viscocity (Pa)
# "Reference Values for Dynamic Viscosity and Density of Human Blood Plasma" by Hans-Ulrich Neue, published in Clinical Chemistry and Laboratory Medicine in 2000. This study reported an average viscosity of 3.5 mPa.s at a shear rate 
mu = .0035 

# Radius of aorta (m)
# "Aortic Anatomy Revisited: A Pictorial Essay" by Mahmoud Ahmed and Frank Corl, published in Current Problems in Diagnostic Radiology in 2018,
r = .025

# Sin of angle for vessel
# "Anatomy of the Aorta" by R. Shane Tubbs, Marios Loukas, and Mohammadali M. Shoja, published in the Journal of Cardiovascular Disease Research in 2013.
sintheta = math.sin(math.radians(45))

#length of aorta (m)
# "Atlas of Human Anatomy" by Frank H. Netter
l = .3

#Variables
# acceleration due to gravity (m/s^2)
g_start =0
g_step =.01
g_stop = 10

g=np.arange(g_start, g_stop, g_step)

#Shear Stress
tau = m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2 * mu)) ** n

#Plotting
fig, ax = plt.subplots()

ax.plot(g, tau, linewidth=2.0)

plt.show()