import matplotlib.pyplot as plt
import pylab as py
from formula.calculates import *
from formula.kinematics import *
from matplotlib import animation, rc

# initialization animation function: plot the background of each frame
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    ttl.set_text('')
    return (line1, line2, line3, ttl)

def mplot(fign, x, y, xl, yl, clr, lbl):
    py.figure(fign)
    py.xlabel(xl)
    py.ylabel(yl)
    return py.plot(x, y, clr, linewidth=1.0, label=lbl)


# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 09:51:10 2014

@author: Zaman
"""

m1 = 2e30  # Mass of Sun in kg
m2 = 6e24  # Mass of Earth in kg
m3 = 1.9e27  # Mass of Jupiter

G = 6.673e-11  # Gravitational Constant

RR = 1.496e11  # Normalizing distance in km (= 1 AU)
MM = 6e24  # Normalizing mass
TT = 365 * 24 * 60 * 60.0  # Normalizing time (1 year)

FF = (G * MM ** 2) / RR ** 2  # Unit force
EE = FF * RR  # Unit energy

GG = (MM * G * TT ** 2) / (RR ** 3)

Ms = m1 / MM  # Normalized mass of Sun
Me = m2 / MM  # Normalized mass of Earth
Mj = 500 * m3 / MM  # Normalized mass of Jupiter/Super Jupiter

ti = 0  # initial time = 0
tf = 120  # final time = 120 years

N = 100 * tf  # 100 points per year
t = np.linspace(ti, tf, N)  # time array from ti to tf with N points

h = t[2] - t[1]  # time step (uniform)

# Initialization

KE1 = np.zeros(N)  # Kinetic energy
KE2 = np.zeros(N)  # Kinetic energy
KE3 = np.zeros(N)  # Kinetic energy
PE1 = np.zeros(N)  # Potential energy
PE2 = np.zeros(N)  # Potential energy
PE3 = np.zeros(N)  # Potential energy
AM1 = np.zeros(N)  # Angular momentum
AM2 = np.zeros(N)  # Angular momentum
AM3 = np.zeros(N)  # Angular momentum
AreaVal1 = np.zeros(N)
AreaVal2 = np.zeros(N)
AreaVal3 = np.zeros(N)

r1 = np.zeros([N, 2])  # position vector of m1
v1 = np.zeros([N, 2])  # velocity vector of m1
r2 = np.zeros([N, 2])  # position vector of m2
v2 = np.zeros([N, 2])  # velocity vector of m2
r3 = np.zeros([N, 2])  # position vector of m3
v3 = np.zeros([N, 2])  # velocity vector of m3

r1i = [0, 0]
r2i = [1496e8 / RR, 0]  # initial position of earth
r3i = [5.2, 0]  # initial position of Jupiter

vv1 = 0
vv2 = np.sqrt(Ms * GG / r2i[0])  # Magnitude of Earth's initial velocity
vv3 = 13.06e3 * TT / RR  # Magnitude of Jupiter's initial velocity
v1i = [0, vv1 * 1.0]  # Initial velocity vector for Earth.Taken to be along y direction as ri is on x axis.
v2i = [0, vv2 * 1.0]  # Initial velocity vector for Jupiter
v3i = [0, vv3 * 1.0]  # Initial velocity vector for Jupiter

# Initializing the arrays with initial values.
t[0] = ti
r1[0, :] = r1i
v1[0, :] = v1i
r2[0, :] = r2i
v2[0, :] = v2i
r3[0, :] = r3i
v3[0, :] = v3i

"""
t1 = dr_dt(ti,ri,vi)
t2 = dv_dt(ti,ri,vi)
print t1
print t2
"""

KE1[0], KE2[0], KE3[0] = KineticEnergy(v1[0, :], v2[0, :], v3[0, :], m1, m2, m3)
PE1[0], PE2[0], PE3[0] = PotentialEnergy(m1, m2, m3, r1[0, :], r2[0, :], r3[0, :])
AM1[0] = AngMomentum(r1[0, :], v1[0, :], m1)
AM2[0] = AngMomentum(r2[0, :], v2[0, :], m2)
AM3[0] = AngMomentum(r3[0, :], v3[0, :], m3)
AreaVal1[0] = 0
AreaVal2[0] = 0
AreaVal3[0] = 0

for i in range(0, N - 1):
    [r1[i + 1, :], v1[i + 1, :]] = RK4Solver(m1, m2, m3, r1[i, :], v1[i, :], h, 1, r2[i, :], r3[i, :])
    [r2[i + 1, :], v2[i + 1, :]] = RK4Solver(m2, m1, m3, r2[i, :], v2[i, :], h, 2, r1[i, :], r3[i, :])
    [r3[i + 1, :], v3[i + 1, :]] = RK4Solver(m3, m1, m2, r3[i, :], v3[i, :], h, 3, r1[i, :], r2[i, :])

    KE1[i+1], KE2[i+1], KE3[i+1] = KineticEnergy(v1[i+1, :], v2[i+1, :], v3[i+1, :], m1, m2, m3)
    PE1[i+1], PE2[i+1], PE3[i+1] = PotentialEnergy(m1, m2, m3, r1[i+1, :], r2[i+1, :], r3[i+1, :])
    AM1[i+1] = AngMomentum(r1[i+1, :], v1[i+1, :], m1)
    # AM2[i+1] = AngMomentum(r2[i+1, :], v2[i+1, :], m2)
    # AM3[i+1] = AngMomentum(r3[i+1, :], v3[i+1, :], m3)
    AreaVal1[i + 1] = AreaVal1[i] + AreaCalc(r1[i, :], r1[i + 1, :])
    # AreaVal2[i + 1] = AreaVal2[i] + AreaCalc(r2[i, :], r2[i + 1, :])
    # AreaVal3[i + 1] = AreaVal3[i] + AreaCalc(r3[i, :], r3[i + 1, :])

lbl = 'orbit'
py.plot(0, 0, 'ro', linewidth=7)
mplot(1, r1[:, 0], r1[:, 1], r'$x$ position (AU)', r'$y$ position (AU)', 'blue', 'Earth')
mplot(1, r2[:, 0], r2[:, 1], r'$x$ position (AU)', r'$y$ position (AU)', 'green', 'Super Jupiter')
mplot(1, r3[:, 0], r3[:, 1], r'$x$ position (AU)', r'$y$ position (AU)', 'red', 'Sun')
py.ylim([-9, 9])

py.axis('equal')
mplot(2, t, KE1, r'Time, $t$ (years)', r'Kinetice Energy, $KE$ ($\times$' + str("%.*e" % (2, EE)) + ' Joule)', 'blue',
      'KE')
mplot(2, t, PE1, r'Time, $t$ (years)', r'Potential Energy, $KE$ ($\times$' + str("%.*e" % (2, EE)) + ' Joule)', 'red',
      'PE')
mplot(2, t, KE1 + PE1, r'Time, $t$ (years)', r'Total Energy, $KE$ ($\times$' + str("%.*e" % (2, EE)) + ' Joule)', 'black',
      'Total Energy')
q = py.legend(loc=0)
q.draw_frame(False)
py.ylim([-180, 180])

mplot(3, t, AM1, r'Time, $t$ (years)', r'Angular Momentum', 'black', lbl)
py.ylim([4, 8])

mplot(4, t, AreaVal1, r'Time, $t$ (years)', r'Sweeped Area ($AU^2$)', 'black', lbl)


# Animation function. Reads out the positon coordinates sequentially
def animate(i):
    trail1 = 40;
    trail2 = 200;
    trail3 = 200;
    tm_yr = 'Elapsed time = ' + str(round(t[i], 1)) + ' years'
    ttl.set_text(tm_yr)
    line1.set_data(r1[i:max(1, i - trail1):-1, 0], r1[i:max(1, i - trail1):-1, 1])
    line2.set_data(r2[i:max(1, i - trail2):-1, 0], r2[i:max(1, i - trail3):-1, 1])
    line3.set_data(r3[i:max(1, i - trail3):-1, 0], r3[i:max(1, i - trail3):-1, 1])

    return (line1, line2, line3)


# Function for setting up the animation

fig, ax = py.subplots()
ax.axis('square')
ax.set_xlim((-7.2, 7.2))
ax.set_ylim((-7.2, 7.2))
ax.get_xaxis().set_ticks([])  # enable this to hide x axis ticks
ax.get_yaxis().set_ticks([])  # enable this to hide y axis ticks

ax.plot(0, 0, 'o', markersize=9, markerfacecolor="#FDB813", markeredgecolor="#FD7813")
line1, = ax.plot([], [], 'o-', color='#d2eeff', markevery=10000, markerfacecolor='#0077BE', lw=2)  # line for m1
line2, = ax.plot([], [], 'o-', color='#e3dccb', markersize=8, markerfacecolor='#f66338', lw=2, markevery=10000)  # line for m2
line3, = ax.plot([], [], 'o-', color='#e3ddcb', markersize=8, markerfacecolor='#ff6338', lw=2, markevery=10000)  # line for m3

ax.plot([-6, -5], [6.5, 6.5], 'r-')
ax.text(-4.5, 6.3, r'1 AU = $1.496 \times 10^8$ km')

ax.plot(-6, -6.2, 'o', color='#d2eeff', markerfacecolor='#0077BE')
ax.text(-5.5, -6.4, 'Earth')

ax.plot(-3.3, -6.2, 'o', color='#e3dccb', markersize=8, markerfacecolor='#f66338')
ax.text(-2.9, -6.4, 'Super Jupiter (500x mass)')

ax.plot(5, -6.2, 'o', markersize=9, markerfacecolor="#FDB813", markeredgecolor="#FD7813")
ax.text(5.5, -6.4, 'Sun')
ttl = ax.text(0.24, 1.05, '', transform=ax.transAxes, va='center')
# plt.title('Elapsed time, T=%i years' %u)


# Call animation function

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=4000, interval=5, blit=True)
plt.show()