# imports
import tkinter as tk
from math import sqrt, floor
import numpy as np
import matplotlib.pyplot as plt
from formula import energy
from formula import kinematics
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from formula import calculates

# verification flags
f_plot = False
global gapp


class VerticalThrowUp:

    def __init__(self):
        self.app = None
        self.practice = None
        self.home_butt = None
        self.btn_adjust = None
        self.btn_plot = None
        self.canvas = None
        self.ax_4 = None
        self.ax_3 = None
        self.ax_2 = None
        self.ax_1 = None
        self.ax4 = None
        self.ax3 = None
        self.ax2 = None
        self.ax1 = None
        self.ax = None
        self.fig = None
        self.v_scale = None
        self.v_label = None
        self.t_scale = None
        self.t_label = None
        self.m_label = None
        self.h_scale = None
        self.m_scale = None
        self.h_label = None
        self.window = None

    def run(self, practice, app, h, m, v, t):
        self.practice = practice
        self.app = app
        global gapp
        gapp = app
        # setup for the UI window
        self.window = tk.Tk()
        self.window.title("Vertical throw upwards")
        self.window.configure(bg='#0e1c1d')
        self.window.configure(width=1200)
        self.h_label = tk.Label(self.window, text="Select the initial height", bg='#0e1c1d', font=("Arial", 16),
                                fg='white', border=0)
        self.h_scale = tk.Scale(self.window, from_=0, to=300, length=600, tickinterval=15, orient=tk.HORIZONTAL,
                                bg='#0e1c1d', font=("Arial", 10), fg='white', bd=0, highlightthickness=0)
        self.m_label = tk.Label(self.window, text="Select the projectile mass", bg='#0e1c1d', font=("Arial", 16),
                                fg='white', border=0)
        self.m_scale = tk.Scale(self.window, from_=0, to=20, length=600, tickinterval=1, orient=tk.HORIZONTAL,
                                bg='#0e1c1d', font=("Arial", 10), fg='white', bd=0, highlightthickness=0)
        self.t_label = tk.Label(self.window, text="Select the plotting time", bg='#0e1c1d', font=("Arial", 16),
                                fg='white', border=0)
        self.t_scale = tk.Scale(self.window, from_=0, to=30, length=600, tickinterval=3, orient=tk.HORIZONTAL,
                                resolution=0.01, bg='#0e1c1d', font=("Arial", 10), fg='white', bd=0,
                                highlightthickness=0)
        self.v_label = tk.Label(self.window, text="Select the initial velocity of the projectile", bg='#0e1c1d',
                                font=("Arial", 16),
                                fg='white', border=0)
        self.v_scale = tk.Scale(self.window, from_=0, to=60, length=600, tickinterval=3, orient=tk.HORIZONTAL,
                                bg='#0e1c1d', font=("Arial", 10), fg='white', bd=0, highlightthickness=0)

        self.h_scale.set(h)
        self.m_scale.set(m)
        self.v_scale.set(v)
        self.t_scale.set(t)
        self.fig, self.ax = plt.subplots(2, 2, figsize=(15, 7))

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
        self.ax_1 = self.ax[0, 0]
        self.ax_2 = self.ax[0, 1]
        self.ax_3 = self.ax[1, 0]
        self.ax_4 = self.ax[1, 1]

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.btn_plot = tk.Button(text="Plot!", command=self.do_calculations, bg='#0e1c1d', font=("Arial", 20),
                                  fg='white', border=0)
        self.btn_adjust = tk.Button(text="Adjust to ground level", command=self.adjust, bg='#0e1c1d',
                                    font=("Arial", 20), fg='white', border=0)

        # put all the UI elements on the interface
        self.h_label.grid(row=0, column=0)
        self.h_scale.grid(row=0, column=1, columnspan=3)
        self.m_label.grid(row=1, column=0)
        self.m_scale.grid(row=1, column=1, columnspan=3)
        self.t_label.grid(row=2, column=0)
        self.t_scale.grid(row=2, column=1, columnspan=3)
        self.v_label.grid(row=3, column=0)
        self.v_scale.grid(row=3, column=1, columnspan=3)
        self.btn_plot.grid(row=4, column=0, pady=20, columnspan=2)
        self.btn_adjust.grid(row=4, column=1, pady=20, columnspan=2)
        self.home_butt = tk.Button(text="Back", bg='#0e1c1d', fg="white", border=0,
                                   command=lambda: self.home(self.window))
        self.home_butt.grid(row=4, column=3, pady=20)

        # show the window
        self.window.mainloop()

    # functions to read the input data
    def get_t(self):
        return self.t_scale.get()

    def get_h(self):
        return self.h_scale.get()

    def get_m(self):
        return self.m_scale.get()

    def get_v(self):
        return self.v_scale.get()

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
        v = self.get_v()
        g = 9.81

        # calculations
        print("time")
        print(float(t))
        print(float(calculates.quad(-g / 2, v, h)))
        print("---")
        if float(t) > float(calculates.quad(-g / 2, v, h)):
            tk.messagebox.showwarning("Warning", "The desired plotting time is greater than the timespan of the fall!")

        time = np.linspace(0, t)
        h_list = [h for x in range(len(time))]
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
            v = self.get_v()
            g = 9.81
            self.t_scale.set(float(calculates.quad(-g / 2, v, h)))
            print("t")
            print(self.get_t())
            print("--")
            self.do_calculations()
        else:
            tk.messagebox.showerror("Error!", "First you need to plot!")

    def plot_graph(self):
        global f_plot
        f_plot = True
        self.canvas.flush_events()
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=5, column=0, ipadx=5, ipady=5, columnspan=4)

    def home(self, window):
        window.destroy()
        global gapp
        print(gapp)
        print(self.practice)
        self.practice.run(practice=self.practice, app=gapp)
