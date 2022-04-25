# imports
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from formula import energy
from formula import kinematics
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from formula import calculate

# verification flags
f_plot = False


# functions to read the input data
def get_h():
    return h_scale.get()


def get_m():
    return m_scale.get()


def get_t():
    return t_scale.get()


def get_v():
    return -1 * v_scale.get()


# setup for the UI window
window = tk.Tk()
window.title("Vertical throw downwards")
h_label = tk.Label(window, text="Select the initial height")
h_scale = tk.Scale(window, from_=0, to=300, length=600, tickinterval=15, orient=tk.HORIZONTAL)
m_label = tk.Label(window, text="Select the projectile mass")
m_scale = tk.Scale(window, from_=0, to=20, length=600, tickinterval=1, orient=tk.HORIZONTAL)
t_label = tk.Label(window, text="Select the plotting time")
t_scale = tk.Scale(window, from_=0, to=30, length=600, tickinterval=3, orient=tk.HORIZONTAL, resolution=0.01)
v_label = tk.Label(window, text="Select the initial velocity of the projectile")
v_scale = tk.Scale(window, from_=0, to=60, length=600, tickinterval=3, orient=tk.HORIZONTAL)

fig, ax = plt.subplots(2, 2, figsize=(15, 7))

ax[0, 0].set_xlabel("Time (s)")
ax[0, 0].set_ylabel("Height (m)")
ax[0, 0].grid(True)
ax1 = ax[0, 0].twinx()

ax[0, 1].set_xlabel("Time (s)")
ax[0, 1].set_ylabel("Potential Energy (J)")
ax[0, 1].grid(True)
ax[0, 1].legend(loc='lower center', frameon=False, ncol=2)
ax2 = ax[0, 1].twinx()
ax2.set_ylabel("Kinetic Energy (J)", color="r")
ax2.tick_params(axis='y', labelcolor='r')
ax2.legend(loc='upper center', frameon=False, ncol=2)

ax[1, 1].set_xlabel("Height (m)")
ax[1, 1].set_ylabel("Kinetic Energy (J)")
ax[1, 1].grid(True)
ax[1, 1].legend(loc='lower center', frameon=False, ncol=2)
ax3 = ax[1, 1].twinx()
ax3.set_ylabel("Potential Energy (J)", color="g")
ax3.tick_params(axis='y', labelcolor='g')
ax3.legend(loc='upper center', frameon=False, ncol=2)

ax[1, 0].set_xlabel("Time (s)")
ax[1, 0].set_ylabel("Velocity (m/s)")
ax[1, 0].grid(True)
ax[1, 0].legend(loc='lower center', frameon=False, ncol=2)
ax4 = ax[1, 0].twinx()
ax4.set_ylabel("KE/PE", color="r")
ax4.tick_params(axis='y', labelcolor='r')
ax4.legend(loc='upper center', frameon=False, ncol=2)
ax_1 = ax[0, 0]
ax_2 = ax[0, 1]
ax_3 = ax[1, 0]
ax_4 = ax[1, 1]


def do_calculations():
    ax1.cla()
    ax2.cla()
    ax3.cla()
    ax4.cla()
    ax_1.cla()
    ax_2.cla()
    ax_3.cla()
    ax_4.cla()

    # declaration of user given input variables
    t = get_t()
    m = get_m()
    h = get_h()
    v = get_v()
    g = 9.81

    # calculations
    print("time")
    print(v)
    print(float(t))
    print(float(calculate.quad(-g / 2, v, h)))
    print("---")
    if float(t) > float(calculate.quad(-g / 2, v, h)):
        tk.messagebox.showwarning("Warning", "The desired plotting time is greater than the timespan of the fall!")

    time = np.linspace(0, t)
    h_list = [h for _ in range(len(time))]
    v_list = [v for x in range(len(time))]
    v = list(map(kinematics.vt_velocity, v_list, time))
    pos = list(map(kinematics.vt_position, v_list, time, h_list))

    print(pos)

    x = np.ones((len(pos)))

    m_ene = []
    for i in range((len(pos))):
        m_ene.append(m)

    pe = list(map(energy.potential_energy, m_ene, pos))
    ke = list(map(energy.kinetic_energy, m_ene, v))
    r = list(map(energy.ke_by_pe, ke, pe))

    ax[0, 0].grid(True)
    ax[0, 1].grid(True)
    ax[1, 0].grid(True)
    ax[1, 1].grid(True)

    ax[0, 0].set_xlabel("Time (s)")
    ax[0, 0].set_ylabel("Height (m)")

    ax[0, 1].set_xlabel("Time (s)")
    ax[0, 1].set_ylabel("Potential Energy (J)")
    ax[0, 1].legend(loc='lower center', frameon=False, ncol=2)
    ax2.set_ylabel("Kinetic Energy (J)", color="r")
    ax2.tick_params(axis='y', labelcolor='r')
    ax2.legend(loc='upper center', frameon=False, ncol=2)

    ax[1, 1].set_xlabel("Height (m)")
    ax[1, 1].set_ylabel("Kinetic Energy (J)")
    ax[1, 1].legend(loc='lower center', frameon=False, ncol=2)
    ax3.set_ylabel("Potential Energy (J)", color="g")
    ax3.tick_params(axis='y', labelcolor='g')
    ax3.legend(loc='upper center', frameon=False, ncol=2)

    ax[1, 0].set_xlabel("Time (s)")
    ax[1, 0].set_ylabel("Velocity (m/s)")
    ax[1, 0].legend(loc='lower center', frameon=False, ncol=2)
    ax4.set_ylabel("KE/PE", color="r")
    ax4.tick_params(axis='y', labelcolor='r')
    ax4.legend(loc='upper center', frameon=False, ncol=2)

    ax[0, 0].scatter(time, pos, c='red', alpha=0.3)
    ax[0, 1].plot(time, pe, linestyle=":", color='black', label="Potential Energy")
    ax2.plot(time, ke, linestyle="-", color='r', label="Kinetic Energy")
    ax[1, 1].plot(pos, ke, linestyle=":", color='b', label="Kinetic Energy")
    ax3.plot(pos, pe, linestyle="--", color='g', label="Potential Energy")
    ax[1, 0].plot(time, v, linestyle="-.", color='b', label="Velocity")
    ax4.plot(time, r, linestyle="--", color='r', label="KE/PE")
    plot_graph()


def adjust():
    if f_plot:
        h = get_h()
        v = get_v()
        g = 9.81
        t_scale.set(float(calculate.quad(-g / 2, v, h)))
        print("t")
        print(get_t())
        print("--")
        do_calculations()
    else:
        tk.messagebox.showerror("Error!", "First you need to plot!")


def plot_graph():
    global f_plot
    f_plot = True
    canvas.flush_events()
    canvas.draw()
    canvas.get_tk_widget().grid(row=5, column=0, ipadx=5, ipady=5, columnspan=4)


canvas = FigureCanvasTkAgg(fig, master=window)
btn_plot = tk.Button(text="Plot!", command=do_calculations)
btn_adjust = tk.Button(text="Adjust to ground level", command=adjust)

# put all the UI elements on the interface
h_label.grid(row=0, column=0)
h_scale.grid(row=0, column=1, columnspan=3)
m_label.grid(row=1, column=0)
m_scale.grid(row=1, column=1, columnspan=3)
t_label.grid(row=2, column=0)
t_scale.grid(row=2, column=1, columnspan=3)
v_label.grid(row=3, column=0)
v_scale.grid(row=3, column=1, columnspan=3)
btn_plot.grid(row=4, column=0, pady=20, columnspan=2)
btn_adjust.grid(row=4, column=1, pady=20, columnspan=2)

# show the window
window.mainloop()
