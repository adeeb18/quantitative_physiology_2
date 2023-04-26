import numpy as np
import matplotlib.pyplot as plt
import math

# Constants
# yield stress of blood (Pa)
# "Rheological properties of blood" by D.A. Fedosov and G.E. Karniadakis, published in Annual Review of Fluid Mechanics in 2014
tau_yield = 6.31

# Bingham plastic viscosity of blood (Pa*s)
# "Rheological properties of blood" by D.A. Fedosov and G.E. Karniadakis, published in Annual Review of Fluid Mechanics in 2014
mu_bp = 0.01

# Power law constants
# "Rheological properties of blood" by D.A. Fedosov and G.E. Karniadakis, published in Annual Review of Fluid Mechanics in 2014
k = 3.64  # consistency index of blood (Pa*s^n)
n_pl = 0.36  # power law index of blood (no unit)

# Shear rate range (1/s)
gamma_start = 0.1
gamma_stop = 1000
gamma_num = 1000

# Blood properties
rho = 1060  # density of blood in kg/m^3
mu = 0.0035  # dynamic viscosity of blood in Pa*s
r = 0.025  # radius of aorta in meters
sintheta = math.sin(math.radians(45))  # sin of angle for vessel
l = 0.3  # length of aorta in meters
p = 16000
m = 0.04
n = 0.5

# Variables
g_start = 0  
g_stop = 10  
g_step = 0.01  
g = np.arange(g_start, g_stop, g_step)  # acceleration due to gravity array

gamma = np.logspace(np.log10(gamma_start), np.log10(gamma_stop), num=gamma_num)

# Newtonain Model
tau = m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2 * mu)) ** n

# Bingham plastic model
tau_bp = np.zeros((len(g), len(gamma)))

for i, gi in enumerate(g):
    for j in range(len(gamma)):
        if gamma[j] > tau_yield / mu_bp + gi * sintheta * r * rho / mu:
            tau_bp[i, j] = tau_yield + mu_bp * (gamma[j] - tau_yield / mu_bp) + gi * sintheta * r * rho
        else:
            tau_bp[i, j] = mu_bp * gamma[j] + gi * sintheta * r * rho

# Power law model
tau_pl = np.zeros((len(g), len(gamma)))

for i, gi in enumerate(g):
    for j in range(len(gamma)):
        tau_pl[i, j] = k * gamma[j] ** n_pl + gi * sintheta * r * rho / (2 * mu) * gamma[j] ** (n_pl + 1) * r ** 2 / l

# Effects of gravity on Newtonain, Bingham plastic, and power law models
fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(12, 8))

for i, gi in enumerate(g):
    ax[0, 0].plot(gamma, tau_bp[i, :], label=f'g={gi:.2f} m/s^2')
    ax[1, 0].plot(gamma, (tau_bp[i, :] - tau_bp[0, :]) / tau_bp[0, :] * 100, label=f'g={gi:.2f} m/s^2')

    ax[0, 1].plot(gamma, tau_pl[i, :], label=f'g={gi:.2f} m/s^2')
    ax[1, 1].plot(gamma, (tau_pl[i, :] - tau_pl[0, :]) / tau_pl[0, :] * 100, label=f'g={gi:.2f} m/s^2')

# ax[1].xlabel('Shear rate (1/s)')
# ax[1].ylabel('Shear stress (Pa)')
# ax[1].set_xscale('log')
# ax[1].set_yscale('log')
# ax[1].set_title('Power law model')
# ax[1].legend()

plt.show()


