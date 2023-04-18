import numpy as np
import matplotlib.pyplot as plt

# Constants
rho = 1060.0 # Blood density
mu_0 = 0.0035 # Reference viscosity
tau_0 = 0.015 # Yield stress
k_0 = 0.1 # Power-law index: low shear rates
k_inf = 0.01 # Power-law index: high shear rates
g_c = 100 # Characteristic shear rate
p = 1.0 # Power-law e
g = 9.81 # g
r_0 = 0.005 # Reference vessel radius
Q_0 = 0.00001 # Reference flow rate

# Grid and Time
L = 0.02 # Domain
N = 100 # POints
dx = L/N # Spacing
dt = 0.0001 # Time step

# Velocity and Pressure Arrays
u = np.zeros(N+1)
p = np.zeros(N+1)

# BOundry Conditions
u[0] = 0.0 # Inlet velocity
u[N] = 0.0 # Outlet velocity
p[0] = 0.0 # Inlet pressure
p[N] = 0.0 # Outlet pressure

# Main Loop
for n in range(10000):
    # Calc viscosity and shear rate
    r = r_0*(1+(k_0-1)*(np.abs(u)/tau_0)**(k_0-1))**(1/(k_0-1) + 1e-12)
    gamma = (u[1:] - u[:-1])/dx

    # Calc DelP, Fg, and flow rate
    dpdx = (p[1:] - p[:-1])/dx
    f_gravity = rho * g
    Q = Q_0*(r/r_0)**4 + 1e-12 
    k = k_inf + (k_0 - k_inf)/(1 + (gamma/g_c)**p) # Cross Model
    mu = mu_0*(r_0/r)**4*(gamma/100)**(k-1) # Carreau-Yasuda Model

    # Calc vel and P over time
    u[1:-1] += dt*(-1/rho*(dpdx + 2*mu*gamma/Q) + f_gravity/rho)
    p[1:-1] += dt*(-rho*gamma*u[1:-1])

    # Apply BC
    u[0] = 0.0
    u[N] = 0.0
    p[0] = 0.0
    p[N] = 0.0

    # Shear Stress Calc
    tau = mu*gamma

# Plot results
x = np.linspace(0, L, N+1)
plt.plot(x, u)
plt.xlabel('Position (m)')
plt.ylabel('Velocity (m/s)')
plt.show()





