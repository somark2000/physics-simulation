# imports
import tkinter as tk

import matplotlib.pyplot as plt
import pylab as py
from matplotlib import animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from formula.calculates import *
from formula.kinematics import *
from IPython.display import HTML
import ffmpeg

# verification flags
f_plot = False

# positions
ti = 0  # initial time = 0
tf = 120  # final time = 120 years
N = 100 * tf  # 100 points per year
r1 = np.zeros([N, 2])  # position vector of m1
v1 = np.zeros([N, 2])  # velocity vector of m1
r2 = np.zeros([N, 2])  # position vector of m2
v2 = np.zeros([N, 2])  # velocity vector of m2
t = np.linspace(ti, tf, N)  # time array from ti to tf with N points

# mass options
options = [1e22, 1e23, 1e24, 1e25, 1e26, 1e27, 1e28, 1e29, 1e30, 1e31]


# functions to read the input data
def get_data():
    data = []
    MM = 6e24  # Normalizing mass
    data.append(m1_scale.get() * float(clicked1.get()) / MM)
    data.append(m2_scale.get() * float(clicked2.get()) / MM)
    data.append(m3_scale.get() * float(clicked3.get()) / MM)
    data.append(v1_scale.get())
    data.append(v2_scale.get())
    data.append(r1_scale.get())
    data.append(r2_scale.get())
    data.append(phi1_scale.get())
    data.append(phi2_scale.get())
    return data


# initialization animation function: plot the background of each frame
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    ttl.set_text('')
    return line1, line2, ttl


# Animation function. Reads out the position coordinates sequentially
def animate(i):
    trail1 = 2000
    trail2 = 2000
    tm_yr = 'Elapsed time = ' + str(round(t[i], 1)) + ' years'
    ttl.set_text(tm_yr)
    line1.set_data(r1[i:max(1, i - trail1):-1, 0], r1[i:max(1, i - trail1):-1, 1])
    line2.set_data(r2[i:max(1, i - trail2):-1, 0], r2[i:max(1, i - trail2):-1, 1])
    return line1, line2,


def mplot(fign, x, y, xl, yl, clr, lbl,alpha=1.0):
    py.figure(fign)
    py.xlabel(xl)
    py.ylabel(yl)
    return py.plot(x, y, clr, linewidth=1.0, label=lbl, alpha=alpha)


def prepare():
    # resetting the figures
    py.close(1)
    py.close(2)
    py.close(3)
    py.close(4)
    canvas.flush_events()
    global line1,line2,ttl
    line1, line2, ttl = init()
    try:
        canvas.get_tk_widget().grid_forget()
    except AttributeError:
        pass

    # retrieving data from UI
    data = get_data()
    m1, m2, m3, vv1, vv2, rr1, rr2, phi1, phi2 = data
    ti = 0  # initial time = 0
    tf = 120  # final time = 120 years
    N = 100 * tf  # 100 points per year
    h = t[2] - t[1]  # time step (uniform)
    RR = 1.496e11  # Normalizing distance in km (= 1 AU)
    MM = 6e24  # Normalizing mass
    TT = 365 * 24 * 60 * 60.0  # Normalizing time (1 year)
    G = 6.673e-11  # Gravitational Constant
    GG = (MM * G * TT ** 2) / (RR ** 3)

    KE1 = np.zeros(N)  # Kinetic energy
    KE2 = np.zeros(N)  # Kinetic energy
    PE1 = np.zeros(N)  # Potential energy
    PE2 = np.zeros(N)  # Potential energy
    AM1 = np.zeros(N)  # Angular momentum
    AM2 = np.zeros(N)  # Angular momentum
    AreaVal1 = np.zeros(N)
    AreaVal2 = np.zeros(N)

    r1i = [rr1 * math.cos(np.deg2rad(phi1)), rr1 * math.sin(np.deg2rad(phi1))]  # initial position of m1
    r2i = [rr2 * math.cos(np.deg2rad(phi1)), rr2 * math.sin(np.deg2rad(phi2))]  # initial position of m2

    vv1 = np.sqrt(m3 * GG / 1) * vv1 / 30  # Magnitude of Earth's initial velocity
    vv2 = np.sqrt(m3 * GG / 4.9) * vv2 / 13  # Magnitude of Jupiter's initial velocity

    v1i = [vv1 * math.cos(np.pi / 2 + np.deg2rad(phi1)),
           vv1 * math.sin(np.pi / 2 + np.deg2rad(phi1))]  # initial # velocity of m1
    v2i = [vv2 * math.cos(np.pi / 2 + np.deg2rad(phi2)),
           vv2 * math.sin(np.pi / 2 + np.deg2rad(phi2))]  # initial velocity of m2

    # Initializing the arrays with initial values.
    t[0] = ti
    r1[0, :] = r1i
    v1[0, :] = v1i
    r2[0, :] = r2i
    v2[0, :] = v2i

    KE1[0] = KineticEnergy(v1[0, :], m1)
    KE2[0] = KineticEnergy(v2[0, :], m2)
    PE1[0], PE2[0] = PotentialEnergy(r1[0, :], m1, r2[0, :], m2, m3)
    AM1[0] = AngMomentum(r1[0, :], v1[0, :], m1)
    AM2[0] = AngMomentum(r2[0, :], v2[0, :], m2)
    AreaVal1[0] = 0
    AreaVal2[0] = 0

    for i in range(0, N - 1):
        [r1[i + 1, :], v1[i + 1, :]] = RK4Solver(r1[i, :], r2[i, :], m1, m2, m3, v1[i, :], v2[i, :], h, 1)
        [r2[i + 1, :], v2[i + 1, :]] = RK4Solver(r1[i, :], r2[i, :], m1, m2, m3, v1[i, :], v2[i, :], h, 2)

        KE1[i + 1] = KineticEnergy(v1[i + 1, :], m1)
        KE2[i + 1] = KineticEnergy(v2[i + 1, :], m2)
        PE1[i + 1], PE2[i + 1] = PotentialEnergy(r1[i + 1, :], m1, r2[i + 1, :], m2, m3)
        AM1[i + 1] = AngMomentum(r1[i + 1, :], v1[i + 1, :], m1)
        AM2[i + 1] = AngMomentum(r2[i + 1, :], v2[i + 1, :], m2)
        AreaVal1[i + 1] = AreaVal1[i] + AreaCalc(r1[i, :], r1[i + 1, :])
        AreaVal2[i + 1] = AreaVal2[i] + AreaCalc(r2[i, :], r2[i + 1, :])
    do_plot(KE1,PE1,AM1,AreaVal1)


def do_plot(KE1,PE1,AM1,AreaVal1):
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=4000, interval=5, blit=True)
    canvas.flush_events()
    canvas.get_tk_widget().grid(row=0, column=4, rowspan=10)
    canvas.draw()

    G = 6.673e-11  # Gravitational Constant
    RR = 1.496e11  # Normalizing distance in km (= 1 AU)
    MM = 6e24  # Normalizing mass
    FF = (G * MM ** 2) / RR ** 2  # Unit force
    EE = FF * RR  # Unit energy

    lbl = 'orbit'
    py.plot(0, 0, 'ro', linewidth=7)
    mplot(1, r1[:, 0], r1[:, 1], r'$x$ position (AU)', r'$y$ position (AU)', 'blue', 'M1',0.1)
    mplot(1, r2[:, 0], r2[:, 1], r'$x$ position (AU)', r'$y$ position (AU)', 'green', 'M2',0.1)
    py.ylim([-9, 9])

    py.axis('equal')
    mplot(2, t, KE1, r'Time, $t$ (years)', r'Kinetice Energy, $KE$ ($\times$' + str("%.*e" % (2, EE)) + ' Joule)', 'blue', 'KE')
    mplot(2, t, PE1, r'Time, $t$ (years)', r'Potential Energy, $KE$ ($\times$' + str("%.*e" % (2, EE)) + ' Joule)', 'red', 'PE')
    mplot(2, t, KE1 + PE1, r'Time, $t$ (years)', r'Total Energy, $KE$ ($\times$' + str("%.*e" % (2, EE)) + ' Joule)', 'black', 'Total Energy')
    q = py.legend(loc=0)
    q.draw_frame(False)
    py.ylim([-180, 180])

    mplot(3, t, AM1, r'Time, $t$ (years)', r'Angular Momentum', 'black', lbl)
    py.ylim([4, 8])

    mplot(4, t, AreaVal1, r'Time, $t$ (years)', r'Sweeped Area ($AU^2$)', 'black', lbl)
    plt.show()


# setup for the UI window
window = tk.Tk()
window.title("Three Body Problem")

fig, ax = py.subplots()
ax.axis('square')
ax.set_xlim((-10, 10))
ax.set_ylim((-10, 10))
ax.get_xaxis().set_ticks([])  # enable this to hide x-axis ticks
ax.get_yaxis().set_ticks([])  # enable this to hide y-axis ticks
canvas = FigureCanvasTkAgg(fig, master=window)

ax.plot(0, 0, 'o', markersize=9, markerfacecolor="#FDB813", markeredgecolor="#FD7813")
line1, = ax.plot([], [], 'o-', color='blue', markevery=10000, markerfacecolor='#0077BE', lw=2)  # line for m1
line2, = ax.plot([], [], 'o-', color='orange', markevery=10000, markerfacecolor='#f66338', lw=2)  # line for m2
ttl = ax.text(0.24, 1.05, '', transform=ax.transAxes, va='center')

# datatype of menu text
clicked1 = tk.StringVar()
clicked1.set("1e24")
clicked2 = tk.StringVar()
clicked2.set("1e24")
clicked3 = tk.StringVar()
clicked3.set("1e24")

m1_label = tk.Label(window, text="M1")
m1_scale = tk.Scale(window, from_=0, to=100, length=600, tickinterval=20, orient=tk.HORIZONTAL, resolution=0.1)
m1_unit = tk.Label(window, text="M Earth")
m1_selector = tk.OptionMenu(window, clicked1, *options)
m2_label = tk.Label(window, text="M2")
m2_scale = tk.Scale(window, from_=0, to=100, length=600, tickinterval=20, orient=tk.HORIZONTAL, resolution=0.1)
m2_unit = tk.Label(window, text="M Earth")
m2_selector = tk.OptionMenu(window, clicked2, *options)
m3_label = tk.Label(window, text="M3")
m3_scale = tk.Scale(window, from_=0, to=100, length=600, tickinterval=20, orient=tk.HORIZONTAL, resolution=0.1)
m3_unit = tk.Label(window, text="M Earth")
m3_selector = tk.OptionMenu(window, clicked3, *options)
v1_label = tk.Label(window, text="V1")
v1_scale = tk.Scale(window, from_=0, to=60, length=600, tickinterval=5, orient=tk.HORIZONTAL, resolution=0.1)
v1_unit = tk.Label(window, text="km/s")
v2_label = tk.Label(window, text="V2")
v2_scale = tk.Scale(window, from_=0, to=60, length=600, tickinterval=5, orient=tk.HORIZONTAL, resolution=0.1)
v2_unit = tk.Label(window, text="km/s")
r1_label = tk.Label(window, text="R1")
r1_scale = tk.Scale(window, from_=0, to=90, length=600, tickinterval=5, orient=tk.HORIZONTAL, resolution=0.1)
r1_unit = tk.Label(window, text="AU")
r2_label = tk.Label(window, text="R2")
r2_scale = tk.Scale(window, from_=0, to=90, length=600, tickinterval=5, orient=tk.HORIZONTAL, resolution=0.1)
r2_unit = tk.Label(window, text="AU")
phi1_label = tk.Label(window, text="F1")
phi1_scale = tk.Scale(window, from_=0, to=360, length=600, tickinterval=30, orient=tk.HORIZONTAL)
phi1_unit = tk.Label(window, text="Degrees")
phi2_label = tk.Label(window, text="F2")
phi2_scale = tk.Scale(window, from_=0, to=360, length=600, tickinterval=30, orient=tk.HORIZONTAL)
phi2_unit = tk.Label(window, text="Degrees")
btn_plot = tk.Button(text="Plot!", command=prepare)

# put all the UI elements on the interface
m1_label.grid(row=0, column=0)
m1_scale.grid(row=0, column=1)
m1_unit.grid(row=0, column=2)
m1_selector.grid(row=0, column=3)
m2_label.grid(row=1, column=0)
m2_scale.grid(row=1, column=1)
m2_unit.grid(row=1, column=2)
m2_selector.grid(row=1, column=3)
m3_label.grid(row=2, column=0)
m3_scale.grid(row=2, column=1)
m3_unit.grid(row=2, column=2)
m3_selector.grid(row=2, column=3)
v1_label.grid(row=3, column=0)
v1_scale.grid(row=3, column=1)
v1_unit.grid(row=3, column=2)
v2_label.grid(row=4, column=0)
v2_scale.grid(row=4, column=1)
v2_unit.grid(row=4, column=2)
r1_label.grid(row=6, column=0)
r1_scale.grid(row=6, column=1)
r1_unit.grid(row=6, column=2)
r2_label.grid(row=7, column=0)
r2_scale.grid(row=7, column=1)
r2_unit.grid(row=7, column=2)
phi1_label.grid(row=9, column=0)
phi1_scale.grid(row=9, column=1)
phi1_unit.grid(row=9, column=2)
phi2_label.grid(row=10, column=0)
phi2_scale.grid(row=10, column=1)
phi2_unit.grid(row=10, column=2)
btn_plot.grid(row=12, column=1)

# show the window
window.mainloop()
