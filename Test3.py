import numpy as np
import matplotlib.pyplot as plt

# Define the parameters of the model
radius = 0.01 
length = 0.1 
viscosity = 0.001 
gravity = 9.8 

# time
x = np.linspace(0, length, 1000)

# Models
def bingham_plastic(shear_rate, yield_stress):
    if shear_rate < yield_stress:
        return 0
    else:
        return yield_stress * shear_rate

def power_law(shear_rate, exponent):
    return shear_rate ** exponent

def newtonian(shear_rate):
    return shear_rate * viscosity

# NS
def navier_stokes(radius, length, viscosity, gravity, shear_stress_function):

    # Vel
    u = np.zeros(len(x))
    for i in range(len(x) - 1):
        u[i + 1] = u[i] + (shear_stress_function(u[i], x[i]) * (x[i + 1] - x[i])) / (2 * viscosity)

    # P
    p = np.zeros(len(x))
    for i in range(len(x) - 1):
        p[i + 1] = p[i] + (gravity * radius * (u[i + 1] + u[i]) / 2) - (viscosity * (u[i + 1] - u[i]) ** 2) / (2 * radius)

    return u, p

# SR
shear_stress_functions = [bingham_plastic, power_law, newtonian]
for shear_stress_function in shear_stress_functions:
    for radius in [0.005, 0.01, 0.015]:
        for gravity in [9.8, 10, 11]:
            u, p = navier_stokes(radius, length, viscosity, gravity, shear_stress_function)
            """
            plt.plot(x, u)
            plt.xlabel("Radius (m)")
            plt.ylabel("Velocity (m/s)")
            plt.title("Velocity vs. radius for gravity = {} and shear stress function = {}".format(gravity, shear_stress_function.__name__))
            plt.show()
            """
            # Plot the shear stress and pressure over time
            time = np.linspace(0, 1, 100)
            shear_stress = np.zeros(len(time))
            pressure = np.zeros(len(time))
            for i in range(len(time) - 1):
                shear_stress[i + 1] = shear_stress_function(u[i], x[i])
                pressure[i + 1] = p[i]
            plt.plot(time, shear_stress)
            plt.xlabel("Time (s)")
            plt.ylabel("Shear stress (Pa)")
            plt.title("Shear stress over time for gravity = {} and shear stress function = {}".format(gravity, shear_stress_function.__name__))
            plt.show()

            plt.plot(time, pressure)
            plt.xlabel("Time (s)")
            plt.ylabel("Pressure (Pa)")
            plt.title("Pressure over time for gravity = {} and shear stress function = {}".format(gravity, shear_stress_function.__name__))
            plt.show()

