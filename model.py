import numpy as np
import matplotlib.pyplot as plt
import math

#Constants
plt.rcParams["font.family"] = "Times New Roman"

# m constant for blood as a power law fluid (Pa*s^n / m^2)
m = 0.01615

# n constant for blood as a power law fluid (no unit)
n = .708

# density of blood in kg/m^3
# Cutnell, John & Johnson, Kenneth. Physics, Fourth Edition. Wiley, 1998: 308.
rho = 1060

# Pressure (Pa)
# "Cardiovascular Physiology Concepts" by Richard E. Klabunde,"
p = 10000

# Viscocity (Pa)
# "Reference Values for Dynamic Viscosity and Density of Human Blood Plasma" by Hans-Ulrich Neue, published in Clinical Chemistry and Laboratory Medicine in 2000. This study reported an average viscosity of 3.5 mPa.s at a shear rate 
mu = .0035 

# Radius of coronary arteries (m)
r = .0015
r_min = 0.5
r_max = 3.5
r_step = 0.01
r_array = np.arange(r_min, r_max, r_step)

# Sin of angle for vessel
# "Anatomy of the Aorta" by R. Shane Tubbs, Marios Loukas, and Mohammadali M. Shoja, published in the Journal of Cardiovascular Disease Research in 2013.
sintheta = math.sin(math.radians(-45))

# length of coronary arteries (m)
l = .03

#Yield Stress (Pa)
# "Determination of the blood viscosity and yield stress with a pressure-scanning capillary hemorheometer using constitutive models" 
ys = 0.0144

#Variables

# acceleration due to gravity (m/s^2)
g_start =0
g_step =.01
g_stop = 9.8

g=np.arange(g_start, g_stop, g_step)

#Shear Stress
tau_PL = (m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n) # Power Law Shear Stress
tau_NW = (np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)))/280 # Newtonian Shear Stress
#tau_BP = (np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2))) + ys # Bingham Plastic Shear Stress

tau_nog =  m * np.abs(((p/l)) * (r / 2 * mu)) ** n
tau_nog = np.repeat(tau_nog, 4410)


#Plotting
fig, ax = plt.subplots()
plt.xlabel("Acceleration due to Gravity (m/s^2)")
plt.ylabel("Wall Shear Stress (Pa)")
plt.title("Gravity-Induced Changes in Wall Shear Stress in Generalized Coronary Artery")
ax.plot(g, tau_PL, linewidth=2.0, color='r', label='Power Law Fluid (Shear Thinning)')
ax.plot(g, tau_NW, linewidth=2.0, color='b', label='Newtonian Fluid')
ax.axhline(y = 0.60, color='k', linestyle='--')
ax.grid()
#ax.plot(g, tau_BP, linewidth=2.0, color='b', label='Bingham Plastic Fluid')
#ax.plot(g, tau_nog, linewidth=2.0, color='y')
ax.legend(loc='lower right')

plt.show()

# Coronary arteries length (m)
l = .030 

# Variable radius coronary arteries (m)
r_start = .001
r_step =.0001
r_stop = .003

r_variable=np.arange(r_start, r_stop, r_step)

# g values
g_earth = 9.8
g_takeoff = 9.8 * 4
g_space = 9.8/1000000

tau_earth = m * np.abs(((p/l) - np.multiply(np.multiply(g_earth,rho), sintheta)) * (r_variable / 2 * mu)) ** n
tau_takeoff = m * np.abs(((p/l) - np.multiply(np.multiply(g_takeoff,rho), sintheta)) * (r_variable / 2 * mu)) ** n
tau_space = m * np.abs(((p/l) - np.multiply(np.multiply(g_space,rho), sintheta)) * (r_variable / 2 * mu)) ** n

fig, ax = plt.subplots()
plt.xlabel("Vessel Radius (mm)")
plt.ylabel("Wall Shear Stress (Pa)")
plt.title("Gravity-Induced Changes in Wall Shear Stress along Vessel Radius in Shear-Thinning Blood Model")
    
gravity_comp = [9.8e-6, 3.3, 6.6, 9.8]
colors = ['r', 'b', 'g', 'y']
for i in range(4):
    grav_value = gravity_comp[i]
    grav_label = "g = " + str(grav_value) + " m/s^2"
    colu = colors[i]
    testPL = m * np.abs(((p/l) - np.multiply(np.multiply(grav_value,rho), sintheta)) * ((r_array /1000)/ 2)) ** n
    ax.plot(r_array, testPL, linewidth=2.0, color=colu, label=grav_label)

ax.axhline(y = 0.60, color='k', linestyle='--')
ax.grid()
#ax.set_xlim(2.3,2.5)
#ax.set_ylim(0.7,0.8)
ax.legend()
# ax.plot(r_variable, tau_earth, linewidth=2.0, color= 'r', label='earth, g=9.8')
# ax.plot(r_variable, tau_takeoff, linewidth=2.0, color='g', label='takeoff, g=9.8 * 4')
# ax.plot(r_variable, tau_space, linewidth=2.0, color='b', label='space, g=9.8/1000000')
# plt.legend()

plt.show()

# Variable angles coronary arteries (m)
theta_start = -90
theta_step = 1
theta_stop = 90

theta_variable=np.arange(theta_start, theta_stop, theta_step)

sintheta_variable = np.sin(theta_variable * np.pi/180.)


# tau_earth = m * np.abs(((p/l) - np.multiply(np.multiply(g_earth,rho), sintheta_variable)) * (r / 2 * mu)) ** n
# tau_takeoff = m * np.abs(((p/l) - np.multiply(np.multiply(g_takeoff,rho), sintheta_variable)) * (r / 2 * mu)) ** n
# tau_space = m * np.abs(((p/l) - np.multiply(np.multiply(g_space,rho), sintheta_variable)) * (r / 2 * mu)) ** n


fig, ax = plt.subplots()
plt.xlabel("Angle \u03F4 (Redians)")
plt.ylabel("Wall Shear Stress (Pa)")
plt.title("Gravity-Induced Changes in Wall Shear Stress at Different Angles in Shear-Thinning Blood Model")

gravity_comp = [9.8e-6, 3.3, 6.6, 9.8]
colors = ['r', 'b', 'g', 'y']
r_const = 0.0015
for i in range(4):
    grav_value = gravity_comp[i]
    grav_label = "g = " + str(grav_value) + " m/s^2"
    colu = colors[i]
    testPL = m * np.abs(((p/l) - np.multiply(np.multiply(grav_value,rho), sintheta_variable)) * (r_const/ 2)) ** n
    ax.plot(sintheta_variable, testPL, linewidth=2.0, color=colu, label=grav_label)

ax.axhline(y = 0.60, color='k', linestyle='--')
ax.grid()
# ax.plot(theta_variable, tau_earth, linewidth=2.0, color= 'r', label='earth, ge=9.8')
# ax.plot(theta_variable, tau_takeoff, linewidth=2.0, color='g', label='takeoff, g=4*ge')
# ax.plot(theta_variable, tau_space, linewidth=2.0, color='b', label='space, g=ge/100000')
plt.legend(loc = 'lower right')
plt.show()
