# imports
import tkinter as tk
import pylab as py
from matplotlib import animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from formula.calculates import *
from formula.kinematics import *

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
r3 = np.zeros([N, 2])  # position vector of m3
v3 = np.zeros([N, 2])  # velocity vector of m3

# mass options
options = [1e22, 1e23, 1e24, 1e25, 1e26, 1e27, 1e28, 1e29, 1e30, 1e31]


# functions to read the input data
def get_data():
    data = []
    MM = 1e24
    d=1/1e20
    print(m1_scale.get()*float(clicked1.get()))
    data.append(m1_scale.get()*float(clicked1.get())/MM)
    data.append(m2_scale.get()*float(clicked2.get())/MM)
    data.append(m3_scale.get()*float(clicked3.get())/MM)
    data.append(v1_scale.get()+d)
    data.append(v2_scale.get()+d)
    data.append(v3_scale.get()+d)
    data.append(r1_scale.get()+d)
    data.append(r2_scale.get()+d)
    data.append(r3_scale.get()+d)
    data.append(phi1_scale.get()+d)
    data.append(phi2_scale.get()+d)
    data.append(phi3_scale.get()+d)
    return data


# initialization animation function: plot the background of each frame
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line1, line2, line3


# Animation function. Reads out the position coordinates sequentially
def animate(i):
    trail1 = 2000
    trail2 = 2000
    trail3 = 2000
    line1.set_data(r1[i:max(1, i - trail1):-1, 0], r1[i:max(1, i - trail1):-1, 1])
    line2.set_data(r2[i:max(1, i - trail2):-1, 0], r2[i:max(1, i - trail3):-1, 1])
    line3.set_data(r3[i:max(1, i - trail3):-1, 0], r3[i:max(1, i - trail3):-1, 1])
    return line1, line2, line3


def do_plot():
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=4000, interval=5, blit=True)
    canvas.flush_events()
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=4, rowspan=10)
    # plt.show()


def prepare():
    data = get_data()
    m1, m2, m3, vv1, vv2, vv3, rr1, rr2, rr3, phi1, phi2, phi3 = data
    ti = 0  # initial time = 0
    tf = 120  # final time = 120 years
    N = 100 * tf  # 100 points per year
    t = np.linspace(ti, tf, N)  # time array from ti to tf with N points
    h = t[2] - t[1]  # time step (uniform)

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

    r1i = [rr1*math.cos(np.deg2rad(phi1)), rr1*math.sin(np.deg2rad(phi1))]  # initial position of m1
    r2i = [rr2*math.cos(np.deg2rad(phi1)), rr2*math.sin(np.deg2rad(phi2))]  # initial position of m2
    r3i = [rr3*math.cos(np.deg2rad(phi3)), rr3*math.sin(np.deg2rad(phi3))]  # initial position of m3
    v1i = [vv1 * math.cos(np.pi/2 + np.deg2rad(phi1)), vv1 * math.sin(np.pi/2 + np.deg2rad(phi1))]  # initial position of m1
    v2i = [vv2 * math.cos(np.pi/2 + np.deg2rad(phi1)), vv2 * math.sin(np.pi/2 + np.deg2rad(phi2))]  # initial position of m2
    v3i = [vv3 * math.cos(np.pi/2 + np.deg2rad(phi3)), vv3 * math.sin(np.pi/2 + np.deg2rad(phi3))]  # initial position of m3

    # Initializing the arrays with initial values.
    t[0] = ti
    r1[0, :] = r1i
    v1[0, :] = v1i
    r2[0, :] = r2i
    v2[0, :] = v2i
    r3[0, :] = r3i
    v3[0, :] = v3i

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

        KE1[i + 1], KE2[i + 1], KE3[i + 1] = KineticEnergy(v1[i + 1, :], v2[i + 1, :], v3[i + 1, :], m1, m2, m3)
        PE1[i + 1], PE2[i + 1], PE3[i + 1] = PotentialEnergy(m1, m2, m3, r1[i + 1, :], r2[i + 1, :], r3[i + 1, :])
        AM1[i + 1] = AngMomentum(r1[i + 1, :], v1[i + 1, :], m1)
        AM2[i+1] = AngMomentum(r2[i+1, :], v2[i+1, :], m2)
        AM3[i+1] = AngMomentum(r3[i+1, :], v3[i+1, :], m3)
        AreaVal1[i + 1] = AreaVal1[i] + AreaCalc(r1[i, :], r1[i + 1, :])
        AreaVal2[i + 1] = AreaVal2[i] + AreaCalc(r2[i, :], r2[i + 1, :])
        AreaVal3[i + 1] = AreaVal3[i] + AreaCalc(r3[i, :], r3[i + 1, :])
    ax.cla()
    ax.axis('square')
    ax.set_xlim(-90, 90)
    ax.set_ylim(-90, 90)
    ax.get_xaxis().set_ticks([])  # enable this to hide x axis ticks
    ax.get_yaxis().set_ticks([])  # enable this to hide y axis ticks
    do_plot()

# setup for the UI window
window = tk.Tk()
window.title("Throw at an angle")

fig, ax = py.subplots()
ax.axis('square')
ax.set_xlim(-90, 90)
ax.set_ylim(-90, 90)
ax.get_xaxis().set_ticks([])    # enable this to hide x axis ticks
ax.get_yaxis().set_ticks([])    # enable this to hide y axis ticks
canvas = FigureCanvasTkAgg(fig, master=window)

ax.plot(0, 0, 'o', markersize=9, markerfacecolor="#FDB813", markeredgecolor="#FD7813")
line1, = ax.plot([], [], 'o-', color='blue', markevery=10000, markerfacecolor='#0077BE', lw=2)  # line for m1
line2, = ax.plot([], [], 'o-', color='green', markevery=10000, markerfacecolor='#f66338', lw=2)  # line for m2
line3, = ax.plot([], [], 'o-', color='red', markevery=10000, markerfacecolor='#ff6338', lw=2)  # line for m3

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
v3_label = tk.Label(window, text="V3")
v3_scale = tk.Scale(window, from_=0, to=60, length=600, tickinterval=5, orient=tk.HORIZONTAL, resolution=0.1)
v3_unit = tk.Label(window, text="km/s")
r1_label = tk.Label(window, text="R1")
r1_scale = tk.Scale(window, from_=0, to=90, length=600, tickinterval=5, orient=tk.HORIZONTAL, resolution=0.1)
r1_unit = tk.Label(window, text="AU")
r2_label = tk.Label(window, text="R2")
r2_scale = tk.Scale(window, from_=0, to=90, length=600, tickinterval=5, orient=tk.HORIZONTAL, resolution=0.1)
r2_unit = tk.Label(window, text="AU")
r3_label = tk.Label(window, text="R3")
r3_scale = tk.Scale(window, from_=0, to=90, length=600, tickinterval=5, orient=tk.HORIZONTAL, resolution=0.1)
r3_unit = tk.Label(window, text="AU")
phi1_label = tk.Label(window, text="F1")
phi1_scale = tk.Scale(window, from_=0, to=360, length=600, tickinterval=30, orient=tk.HORIZONTAL)
phi1_unit = tk.Label(window, text="Degrees")
phi2_label = tk.Label(window, text="F2")
phi2_scale = tk.Scale(window, from_=0, to=360, length=600, tickinterval=30, orient=tk.HORIZONTAL)
phi2_unit = tk.Label(window, text="Degrees")
phi3_label = tk.Label(window, text="F3")
phi3_scale = tk.Scale(window, from_=0, to=360, length=600, tickinterval=30, orient=tk.HORIZONTAL)
phi3_unit = tk.Label(window, text="Degrees")
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
v3_label.grid(row=5, column=0)
v3_scale.grid(row=5, column=1)
v3_unit.grid(row=5, column=2)
r1_label.grid(row=6, column=0)
r1_scale.grid(row=6, column=1)
r1_unit.grid(row=6, column=2)
r2_label.grid(row=7, column=0)
r2_scale.grid(row=7, column=1)
r2_unit.grid(row=7, column=2)
r3_label.grid(row=8, column=0)
r3_scale.grid(row=8, column=1)
r3_unit.grid(row=8, column=2)
phi1_label.grid(row=9, column=0)
phi1_scale.grid(row=9, column=1)
phi1_unit.grid(row=9, column=2)
phi2_label.grid(row=10, column=0)
phi2_scale.grid(row=10, column=1)
phi2_unit.grid(row=10, column=2)
phi3_label.grid(row=11, column=0)
phi3_scale.grid(row=11, column=1)
phi3_unit.grid(row=11, column=2)
btn_plot.grid(row=12, column=1)

# show the window
window.mainloop()
