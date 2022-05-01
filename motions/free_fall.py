# imports
import tkinter as tk
from math import sqrt, floor

import numpy as np
import matplotlib.pyplot as plt
from formula import energy
from formula import kinematics
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)


# verification flags
f_plot = False

class FreeFall():
    fig, ax = plt.subplots(2, 2, figsize=(15, 7))
    window = tk.Tk()
    h_label = tk.Label(window, text="Select the initial height")
    h_scale = tk.Scale(window, from_=0, to=300, length=600, tickinterval=15, orient=tk.HORIZONTAL)
    m_label = tk.Label(window, text="Select the projectile mass")
    m_scale = tk.Scale(window, from_=0, to=20, length=600, tickinterval=1, orient=tk.HORIZONTAL)
    t_label = tk.Label(window, text="Select the plotting time")
    t_scale = tk.Scale(window, from_=0, to=30, length=600, tickinterval=2, orient=tk.HORIZONTAL, resolution=0.01)
    ax_1 = ax[0, 0]
    ax_2 = ax[0, 1]
    ax_3 = ax[1, 0]
    ax_4 = ax[1, 1]
    canvas = FigureCanvasTkAgg(fig, master=window)
    btn_plot = tk.Button(text="Plot!")
    btn_adjust = tk.Button(text="Adjust to ground level")

    def run(self):
        # setup for the UI window
        self.window.title("Free fall")
        self.ax[0, 0].set_xlabel("Time (s)")
        self.ax[0, 0].set_ylabel("Height (m)")
        self.ax[0, 0].grid(True)
        self.ax1 = self.ax[0, 0].twinx()

        self.ax[0, 1].set_xlabel("Time (s)")
        self.ax[0, 1].set_ylabel("Potential Energy (J)")
        self.ax[0, 1].grid(True)
        self.ax[0, 1].legend(loc='lower center', frameon=False, ncol=2)
        self.ax2 = self.ax[0, 1].twinx()
        self.ax2.set_ylabel("Kinetic Energy (J)", color="r")
        self.ax2.tick_params(axis='y', labelcolor='r')
        self.ax2.legend(loc='upper center', frameon=False, ncol=2)

        self.ax[1, 1].set_xlabel("Height (m)")
        self.ax[1, 1].set_ylabel("Kinetic Energy (J)")
        self.ax[1, 1].grid(True)
        self.ax[1, 1].legend(loc='lower center', frameon=False, ncol=2)
        self.ax3 = self.ax[1, 1].twinx()
        self.ax3.set_ylabel("Potential Energy (J)", color="g")
        self.ax3.tick_params(axis='y', labelcolor='g')
        self.ax3.legend(loc='upper center', frameon=False, ncol=2)

        self.ax[1, 0].set_xlabel("Time (s)")
        self.ax[1, 0].set_ylabel("Velocity (m/s)")
        self.ax[1, 0].grid(True)
        self.ax[1, 0].legend(loc='lower center', frameon=False, ncol=2)
        self.ax4 = self.ax[1, 0].twinx()
        self.ax4.set_ylabel("KE/PE", color="r")
        self.ax4.tick_params(axis='y', labelcolor='r')
        self.ax4.legend(loc='upper center', frameon=False, ncol=2)

        self.btn_plot.configure(command=self.do_calculations)
        self.btn_adjust.configure(command=self.adjust)

        # put all the UI elements on the interface
        self.h_label.grid(row=0, column=0)
        self.h_scale.grid(row=0, column=1)
        self.m_label.grid(row=1, column=0)
        self.m_scale.grid(row=1, column=1)
        self.t_label.grid(row=2, column=0)
        self.t_scale.grid(row=2, column=1)
        self.btn_plot.grid(row=3, column=0, pady=20)
        self.btn_adjust.grid(row=3, column=1, pady=20)

        # show the window
        self.window.mainloop()



    # functions to read the input data
    def get_h(self):
        return self.h_scale.get()


    def get_m(self):
        return self.m_scale.get()


    def get_t(self):
        return self.t_scale.get()


# # setup for the UI window
# window = tk.Tk()
# window.title("Free fall")
# h_label = tk.Label(window, text="Select the initial height")
# h_scale = tk.Scale(window, from_=0, to=300, length=600, tickinterval=15, orient=tk.HORIZONTAL)
# m_label = tk.Label(window, text="Select the projectile mass")
# m_scale = tk.Scale(window, from_=0, to=20, length=600, tickinterval=1, orient=tk.HORIZONTAL)
# t_label = tk.Label(window, text="Select the plotting time")
# t_scale = tk.Scale(window, from_=0, to=30, length=600, tickinterval=2, orient=tk.HORIZONTAL,resolution=0.01)
#
# fig, ax = plt.subplots(2, 2, figsize=(15, 7))
#
# ax[0, 0].set_xlabel("Time (s)")
# ax[0, 0].set_ylabel("Height (m)")
# ax[0, 0].grid(True)
# ax1 = ax[0, 0].twinx()
#
# ax[0, 1].set_xlabel("Time (s)")
# ax[0, 1].set_ylabel("Potential Energy (J)")
# ax[0, 1].grid(True)
# ax[0, 1].legend(loc='lower center', frameon=False, ncol=2)
# ax2 = ax[0, 1].twinx()
# ax2.set_ylabel("Kinetic Energy (J)", color="r")
# ax2.tick_params(axis='y', labelcolor='r')
# ax2.legend(loc='upper center', frameon=False, ncol=2)
#
# ax[1, 1].set_xlabel("Height (m)")
# ax[1, 1].set_ylabel("Kinetic Energy (J)")
# ax[1, 1].grid(True)
# ax[1, 1].legend(loc='lower center', frameon=False, ncol=2)
# ax3 = ax[1, 1].twinx()
# ax3.set_ylabel("Potential Energy (J)", color="g")
# ax3.tick_params(axis='y', labelcolor='g')
# ax3.legend(loc='upper center', frameon=False, ncol=2)
#
# ax[1, 0].set_xlabel("Time (s)")
# ax[1, 0].set_ylabel("Velocity (m/s)")
# ax[1, 0].grid(True)
# ax[1, 0].legend(loc='lower center', frameon=False, ncol=2)
# ax4 = ax[1, 0].twinx()
# ax4.set_ylabel("KE/PE", color="r")
# ax4.tick_params(axis='y', labelcolor='r')
# ax4.legend(loc='upper center', frameon=False, ncol=2)
# ax_1 = ax[0, 0]
# ax_2 = ax[0, 1]
# ax_3 = ax[1, 0]
# ax_4 = ax[1, 1]


    def do_calculations(self):
        self.ax1.cla()
        self.ax2.cla()
        self.ax3.cla()
        self.ax4.cla()
        self.ax_1.cla()
        self.ax_2.cla()
        self.ax_3.cla()
        self.ax_4.cla()

        # declaration of user given input variables
        t = self.get_t()
        m = self.get_m()
        h = self.get_h()

        # calculations
        print(float(t))
        print(float(sqrt(2 / 9.81 * h)))
        if float(t) > float(sqrt(2 / 9.81 * h)):
            tk.messagebox.showwarning("Warning", "The desired plotting time is greater than the timespan of the fall!")

        time = np.linspace(0, t)
        h_list = [h for x in range(len(time))]
        v = list(map(kinematics.ff_velocity, time))
        pos = list(map(kinematics.ff_position, time, h_list))

        print(pos)

        x = np.ones((len(pos)))

        m_ene = []
        for i in range((len(pos))):
            m_ene.append(m)

        pe = list(map(energy.potential_energy, m_ene, pos))
        ke = list(map(energy.kinetic_energy, m_ene, v))
        r = list(map(energy.ke_by_pe, ke, pe))

        self.ax[0, 0].grid(True)
        self.ax[0, 1].grid(True)
        self.ax[1, 0].grid(True)
        self.ax[1, 1].grid(True)

        self.ax[0, 0].set_xlabel("Time (s)")
        self.ax[0, 0].set_ylabel("Height (m)")

        self.ax[0, 1].set_xlabel("Time (s)")
        self.ax[0, 1].set_ylabel("Potential Energy (J)")
        self.ax[0, 1].legend(loc='lower center', frameon=False, ncol=2)
        self.ax2.set_ylabel("Kinetic Energy (J)", color="r")
        self.ax2.tick_params(axis='y', labelcolor='r')
        self.ax2.legend(loc='upper center', frameon=False, ncol=2)

        self.ax[1, 1].set_xlabel("Height (m)")
        self.ax[1, 1].set_ylabel("Kinetic Energy (J)")
        self.ax[1, 1].legend(loc='lower center', frameon=False, ncol=2)
        self.ax3.set_ylabel("Potential Energy (J)", color="g")
        self.ax3.tick_params(axis='y', labelcolor='g')
        self.ax3.legend(loc='upper center', frameon=False, ncol=2)

        self.ax[1, 0].set_xlabel("Time (s)")
        self.ax[1, 0].set_ylabel("Velocity (m/s)")
        self.ax[1, 0].legend(loc='lower center', frameon=False, ncol=2)
        self.ax4.set_ylabel("KE/PE", color="r")
        self.ax4.tick_params(axis='y', labelcolor='r')
        self.ax4.legend(loc='upper center', frameon=False, ncol=2)

        self.ax[0, 0].scatter(time, pos, c='red', alpha=0.3)
        self.ax[0, 1].plot(time, pe, linestyle=":", color='black', label="Potential Energy")
        self.ax2.plot(time, ke, linestyle="-", color='r', label="Kinetic Energy")
        self.ax[1, 1].plot(pos, ke, linestyle=":", color='b', label="Kinetic Energy")
        self.ax3.plot(pos, pe, linestyle="--", color='g', label="Potential Energy")
        self.ax[1, 0].plot(time, v, linestyle="-.", color='b', label="Velocity")
        self.ax4.plot(time, r, linestyle="--", color='r', label="KE/PE")
        self.plot_graph()


    def adjust(self):
        if f_plot:
            h = self.get_h()
            self.t_scale.set(floor(float(sqrt(2 / 9.81 * h))))
            self.do_calculations()
        else:
            tk.messagebox.showerror("Error!", "First you need to plot!")


    def plot_graph(self):
        global f_plot
        f_plot = True
        self.canvas.flush_events()
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=4, column=0, ipadx=20, ipady=20, columnspan=2)


# canvas = FigureCanvasTkAgg(fig, master=window)
# btn_plot = tk.Button(text="Plot!", command=do_calculations)
# btn_adjust = tk.Button(text="Adjust to ground level", command=adjust)
#
# # put all the UI elements on the interface
# h_label.grid(row=0, column=0)
# h_scale.grid(row=0, column=1)
# m_label.grid(row=1, column=0)
# m_scale.grid(row=1, column=1)
# t_label.grid(row=2, column=0)
# t_scale.grid(row=2, column=1)
# btn_plot.grid(row=3, column=0, pady=20)
# btn_adjust.grid(row=3, column=1, pady=20)
#
# # show the window
# window.mainloop()
