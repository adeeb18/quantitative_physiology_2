import numpy as np
import matplotlib.pyplot as plt
import math
from labellines import labelLine, labelLines

#Constants

# m constant for blood as a power law fluid (Pa*s^n / m^2)
m = 0.01615

# n constant for blood as a power law fluid (no unit)
n = .708

# density of blood in kg/m^3
# Cutnell, John & Johnson, Kenneth. Physics, Fourth Edition. Wiley, 1998: 308.
rho = 1060

# Pressure (Pa)
# "Cardiovascular Physiology Concepts" by Richard E. Klabunde,"
p = 16000

# Viscocity (Pa)
# "Reference Values for Dynamic Viscosity and Density of Human Blood Plasma" by Hans-Ulrich Neue, published in Clinical Chemistry and Laboratory Medicine in 2000. This study reported an average viscosity of 3.5 mPa.s at a shear rate 
mu = .0035 

# Radius of coronary arteries (m)
r = .0015

# Sin of angle for vessel
# "Anatomy of the Aorta" by R. Shane Tubbs, Marios Loukas, and Mohammadali M. Shoja, published in the Journal of Cardiovascular Disease Research in 2013.
sintheta = math.sin(math.radians(-45))

# length of coronary arteries (m)
l = .03

#Yield Stress (Pa)
# "Determination of the blood viscosity and yield stress with a pressure-scanning capillary hemorheometer using constitutive models" 
ys = 0.0144

#Variables

# acceleration due to Gravity (m/s^2)
g_start =0
g_step =.01
g_stop = 9.8*4.5
g=np.arange(g_start, g_stop, g_step)


plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 16})



'''
M constant Sensitivity Analysis
'''
m1 = m * 1.75
m2 = m * 2.5
m3 = m * 3.25
m4 = m * 0.25


print("m constant power law: ")
print("m: " + str(m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))
print("m1: " + str(m1 * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))
print("m2: " + str(m2 * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))
print("m3: " + str(m3 * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))
print("m4: " + str(m4 * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))

taum = (m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n)
taum1 = (m1 * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n)
taum2 = (m2 * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n)
taum3 = (m3 * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n)
taum4 = (m4 * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n)


fig, ax = plt.subplots()

plt.xlabel("Acceleration due to Gravity (m/s^2)")
plt.ylabel("Shear Stress (Pa)")
plt.title("One-way Sensitivity Analysis, constant m")
ax.plot(g, taum, linewidth=2.0, color='k', label='mₒ')
ax.plot(g, taum1, linewidth=2.0, color='k', label='1.75mₒ')
ax.plot(g, taum2, linewidth=2.0, color='k', label='2.25mₒ')
ax.plot(g, taum3, linewidth=2.0, color='k', label='3.25mₒ')
ax.plot(g, taum4, linewidth=2.0, color='k', label='0.25mₒ')

labelLines(ax.get_lines(), zorder=2.5)

plt.show()

'''
N constant Sensitivity Analysis
'''
#N constant
n1 = n * 1.75
n2 = n * 2.5
n3 = n * 3.25
n4 = n * 0.25


print("n constant power law: ")
print("n: " + str(m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))
print("n1: " + str(m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n1))
print("n2: " + str(m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n2))
print("n3: " + str(m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n3))
print("n4: " + str(m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n4))


taun = (m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n)
taun1 = (m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n1)
taun2 = (m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n2)
taun3 = (m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n3)
taun4 = (m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n4)


fig, ax = plt.subplots()

plt.xlabel("Acceleration due to Gravity (m/s^2)")
plt.ylabel("Shear Stress (Pa)")
plt.title("One-way Sensitivity Analysis, constant n")
ax.plot(g, taun, linewidth=2.0, color='k', label='nₒ')
ax.plot(g, taun1, linewidth=2.0, color='k', label='1.75nₒ')
ax.plot(g, taun2, linewidth=2.0, color='k', label='2.25nₒ')
ax.plot(g, taun3, linewidth=2.0, color='k', label='3.25nₒ')
ax.plot(g, taun4, linewidth=2.0, color='k', label='0.25nₒ')

labelLines(ax.get_lines(), zorder=2.5)

plt.show()


'''
Density constant Sensitivity Analysis
'''

#Density
#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4590883/#:~:text=Existing%20data%20are%20conflicting%20and,%2FmL)%20%5B10%5D.
rho1 = rho * 1.75
rho2 = rho * 2.5
rho3 = rho * 3.25
rho4 = rho * 0.25


print("rho constant power law: ")
print("rho: " + str(m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))
print("rho1: " + str(m * np.abs(((p/l) - np.multiply(np.multiply(g,rho1), sintheta)) * (r / 2)) ** n))
print("rho2: " + str(m * np.abs(((p/l) - np.multiply(np.multiply(g,rho2), sintheta)) * (r / 2)) ** n))
print("rho3: " + str(m * np.abs(((p/l) - np.multiply(np.multiply(g,rho3), sintheta)) * (r / 2)) ** n))
print("rho4: " + str(m * np.abs(((p/l) - np.multiply(np.multiply(g,rho4), sintheta)) * (r / 2)) ** n))



'''
Change in P constant Sensitivity Analysis
'''

#Pressure
p1 = p * 1.75
p2 = p * 2.5
p3 = p * 3.25
p4 = p * 0.25


print("pressure power law: ")
print("p: " + str(m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))
print("p1: " + str(m * np.abs(((p1/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))
print("p2: " + str(m * np.abs(((p2/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))
print("p3: " + str(m * np.abs(((p3/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))
print("p4: " + str(m * np.abs(((p4/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))


taup = (m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n)
taup1 = (m * np.abs(((p1/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n)
taup2 = (m * np.abs(((p2/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n)
taup3 = (m * np.abs(((p3/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n)
taup4 = (m * np.abs(((p4/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n)


fig, ax = plt.subplots()

plt.xlabel("Acceleration due to Gravity (m/s^2)")
plt.ylabel("Shear Stress (Pa)")
plt.title("One-way Sensitivity Analysis, Change in Presssure (\u0394P)")
ax.plot(g, taup, linewidth=2.0, color='k', label='\u0394Pₒ')
ax.plot(g, taup1, linewidth=2.0, color='k', label='1.75\u0394Pₒ')
ax.plot(g, taup2, linewidth=2.0, color='k', label='2.25\u0394Pₒ')
ax.plot(g, taup3, linewidth=2.0, color='k', label='3.25\u0394Pₒ')
ax.plot(g, taup4, linewidth=2.0, color='k', label='0.25\u0394Pₒ')

labelLines(ax.get_lines(), zorder=2.5)

plt.show()

'''
L constant Sensitivity Analysis
'''

#Length
l1 = l * 1.75
l2 = l * 2.5
l3 = l * 3.25
l4 = l * 0.25


print("length power law: ")
print("l: " + str(m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))
print("l1: " + str(m * np.abs(((p/l1) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))
print("l2: " + str(m * np.abs(((p/l2) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))
print("l3: " + str(m * np.abs(((p/l3) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))
print("l4: " + str(m * np.abs(((p/l4) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n))



taul = (m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n)
taul1 = (m * np.abs(((p/l1) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n)
taul2 = (m * np.abs(((p/l2) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n)
taul3 = (m * np.abs(((p/l3) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n)
taul4 = (m * np.abs(((p/l4) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n)


fig, ax = plt.subplots()

plt.xlabel("Acceleration due to Gravity (m/s^2)")
plt.ylabel("Shear Stress (Pa)")
plt.title("One-way Sensitivity Analysis, Length (l)")
ax.plot(g, taul, linewidth=2.0, color='k', label='lₒ')
ax.plot(g, taul1, linewidth=2.0, color='k', label='1.75lₒ')
ax.plot(g, taul2, linewidth=2.0, color='k', label='2.25lₒ')
ax.plot(g, taul3, linewidth=2.0, color='k', label='3.25lₒ')
ax.plot(g, taul4, linewidth=2.0, color='k', label='0.25lₒ')

labelLines(ax.get_lines(), zorder=2.5)

plt.show()



#Viscocity
mu1 = mu * 1.75
mu2 = mu * 2.5
mu3 = mu * 3.25
mu4 = mu * 0.25


print("viscocity power law: ")


#yield stress
ys1 = ys * 1.75
ys2 = ys * 2.5
ys3 = ys * 3.25
ys4 = ys * 0.25


print("Yield Stress Bingham: ")
print("ys: " + str((np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)))/500 + ys ))
print("ys1: " + str((np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)))/500 + ys1 ))
print("ys2: " + str((np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)))/500 + ys2 ))
print("ys3: " + str((np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)))/500 + ys3 ))
print("ys4: " + str((np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)))/500 + ys4 ))



# tau_PL = (m * np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)) ** n) # Power Law Shear Stress
# tau_NW = (np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)))/500 # Newtonian Shear Stress
# tau_BP = (np.abs(((p/l) - np.multiply(np.multiply(g,rho), sintheta)) * (r / 2)))/500 + ys # Bingham Plastic Shear Stress
