# imports
import time
import tkinter as tk

import matplotlib.pyplot as plt
import pylab as py
from matplotlib import animation, pylab
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from formula.calculates import *
from formula.kinematics import *
from IPython.display import HTML
import ffmpeg

# verification flags
f_plot = False
global gapp
# mass options
options = [1e20, 1e21, 1e22, 1e23, 1e24, 1e25, 1e26, 1e27, 1e28, 1e29, 1e30, 1e31]


class ThreeBody:
    def __init__(self):
        self.app = None
        self.practice = None
        self.home_butt = None
        self.tm_yr = None
        self.trail2 = None
        self.trail1 = None
        self.btn_plot = None
        self.phi2_unit = None
        self.phi2_scale = None
        self.phi2_label = None
        self.phi1_unit = None
        self.phi1_scale = None
        self.phi1_label = None
        self.r2_unit = None
        self.r2_scale = None
        self.r2_label = None
        self.r1_unit = None
        self.r1_scale = None
        self.r1_label = None
        self.v2_unit = None
        self.v2_scale = None
        self.v2_label = None
        self.v1_unit = None
        self.v1_scale = None
        self.v1_label = None
        self.m3_selector = None
        self.m3_unit = None
        self.m3_scale = None
        self.m3_label = None
        self.m2_selector = None
        self.m2_unit = None
        self.m2_scale = None
        self.m2_label = None
        self.m1_selector = None
        self.m1_unit = None
        self.m1_scale = None
        self.m1_label = None
        self.clicked3 = None
        self.clicked2 = None
        self.clicked1 = None
        self.ttl = None
        self.line2 = None
        self.line1 = None
        self.canvas = None
        self.ax = None
        self.fig = None
        self.window = None
        self.t = None
        self.v2 = None
        self.r2 = None
        self.v1 = None
        self.r1 = None
        self.N = None
        self.tf = None
        self.ti = None

    def run(self, practice, app, m1, m2, mc, s1, s2, s3, v1, v2, r1, r2, p1, p2):
        self.practice = practice
        self.app = app
        global options
        global gapp
        gapp = app
        # positions
        self.ti = 0  # initial time = 0
        self.tf = 120  # final time = 200 years
        self.N = 100 * self.tf  # 100 points per year
        self.r1 = np.zeros([self.N, 2])  # position vector of m1
        self.v1 = np.zeros([self.N, 2])  # velocity vector of m1
        self.r2 = np.zeros([self.N, 2])  # position vector of m2
        self.v2 = np.zeros([self.N, 2])  # velocity vector of m2
        self.t = np.linspace(self.ti, self.tf, self.N)  # time array from ti to tf with N points

        # setup for the UI window
        self.window = tk.Tk()
        self.window.title("Three Body Problem")
        self.window.configure(bg='#0e1c1d')
        self.window.configure(width=1200)

        self.fig, self.ax = plt.subplots()
        self.ax.axis('square')
        self.ax.set_xlim((-10, 10))
        self.ax.set_ylim((-10, 10))
        self.ax.get_xaxis().set_ticks([])  # enable this to hide x-axis ticks
        self.ax.get_yaxis().set_ticks([])  # enable this to hide y-axis ticks
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)

        self.ax.plot(0, 0, 'o', markersize=9, markerfacecolor="#FDB813", markeredgecolor="#FD7813")
        self.line1, = self.ax.plot([], [], 'o-', color='blue', markevery=10000, markerfacecolor='#0077BE',
                                   lw=2)  # line for m1
        self.line2, = self.ax.plot([], [], 'o-', color='orange', markevery=10000, markerfacecolor='#f66338',
                                   lw=2)  # line for m2
        self.ttl = self.ax.text(0.24, 1.05, '', transform=self.ax.transAxes, va='center')

        # datatype of menu text
        global options
        self.clicked1 = tk.StringVar()
        self.clicked1.set(options[s1])
        self.clicked2 = tk.StringVar()
        self.clicked2.set(options[s2])
        self.clicked3 = tk.StringVar()
        self.clicked3.set(options[s3])

        self.m1_label = tk.Label(self.window, text="Orbiting mass 1", bg='#0e1c1d', font=("Arial", 16),
                                 fg='white', border=0)
        self.m1_scale = tk.Scale(self.window, from_=0, to=100, length=600, tickinterval=20, orient=tk.HORIZONTAL,
                                 resolution=0.1, bg='#0e1c1d', font=("Arial", 10), fg='white', bd=0,
                                 highlightthickness=0)
        self.m1_unit = tk.Label(self.window, text="kg", bg='#0e1c1d', font=("Arial", 12),
                                fg='white', border=0)
        self.m1_selector = tk.OptionMenu(self.window, self.clicked1, *options)
        self.m1_selector.configure(bg='#0e1c1d', font=("Arial", 12), fg='white', border=0)
        self.m2_label = tk.Label(self.window, text="Orbiting mass 2", bg='#0e1c1d', font=("Arial", 16),
                                 fg='white', border=0)
        self.m2_scale = tk.Scale(self.window, from_=0, to=100, length=600, tickinterval=20, orient=tk.HORIZONTAL,
                                 resolution=0.1, bg='#0e1c1d', font=("Arial", 10), fg='white', bd=0,
                                 highlightthickness=0)
        self.m2_unit = tk.Label(self.window, text="kg", bg='#0e1c1d', font=("Arial", 12),
                                fg='white', border=0)
        self.m2_selector = tk.OptionMenu(self.window, self.clicked2, *options)
        self.m2_selector.configure(bg='#0e1c1d', font=("Arial", 12), fg='white', border=0)
        self.m3_label = tk.Label(self.window, text="Central mass", bg='#0e1c1d', font=("Arial", 16),
                                 fg='white', border=0)
        self.m3_scale = tk.Scale(self.window, from_=0, to=100, length=600, tickinterval=20, orient=tk.HORIZONTAL,
                                 resolution=0.1, bg='#0e1c1d', font=("Arial", 10), fg='white', bd=0,
                                 highlightthickness=0)
        self.m3_unit = tk.Label(self.window, text="kg", bg='#0e1c1d', font=("Arial", 12),
                                fg='white', border=0)
        self.m3_selector = tk.OptionMenu(self.window, self.clicked3, *options)
        self.m3_selector.configure(bg='#0e1c1d', font=("Arial", 12), fg='white', border=0)
        self.v1_label = tk.Label(self.window, text="V1", bg='#0e1c1d', font=("Arial", 16),
                                 fg='white', border=0)
        self.v1_scale = tk.Scale(self.window, from_=0, to=60, length=600, tickinterval=5, orient=tk.HORIZONTAL,
                                 resolution=0.1, bg='#0e1c1d', font=("Arial", 10), fg='white', bd=0,
                                 highlightthickness=0)
        self.v1_unit = tk.Label(self.window, text="km/s", bg='#0e1c1d', font=("Arial", 12),
                                fg='white', border=0)
        self.v2_label = tk.Label(self.window, text="V2", bg='#0e1c1d', font=("Arial", 16),
                                 fg='white', border=0)
        self.v2_scale = tk.Scale(self.window, from_=0, to=60, length=600, tickinterval=5, orient=tk.HORIZONTAL,
                                 resolution=0.1, bg='#0e1c1d', font=("Arial", 10), fg='white', bd=0,
                                 highlightthickness=0)
        self.v2_unit = tk.Label(self.window, text="km/s", bg='#0e1c1d', font=("Arial", 12),
                                fg='white', border=0)
        self.r1_label = tk.Label(self.window, text="R1", bg='#0e1c1d', font=("Arial", 16),
                                 fg='white', border=0)
        self.r1_scale = tk.Scale(self.window, from_=0, to=90, length=600, tickinterval=5, orient=tk.HORIZONTAL,
                                 resolution=0.1, bg='#0e1c1d', font=("Arial", 10), fg='white', bd=0,
                                 highlightthickness=0)
        self.r1_unit = tk.Label(self.window, text="AU", bg='#0e1c1d', font=("Arial", 12),
                                fg='white', border=0)
        self.r2_label = tk.Label(self.window, text="R2", bg='#0e1c1d', font=("Arial", 16),
                                 fg='white', border=0)
        self.r2_scale = tk.Scale(self.window, from_=0, to=90, length=600, tickinterval=5, orient=tk.HORIZONTAL,
                                 resolution=0.1, bg='#0e1c1d', font=("Arial", 10), fg='white', bd=0,
                                 highlightthickness=0)
        self.r2_unit = tk.Label(self.window, text="AU", bg='#0e1c1d', font=("Arial", 12),
                                fg='white', border=0)
        self.phi1_label = tk.Label(self.window, text="F1", bg='#0e1c1d', font=("Arial", 16),
                                   fg='white', border=0)
        self.phi1_scale = tk.Scale(self.window, from_=0, to=360, length=600, tickinterval=30, orient=tk.HORIZONTAL,
                                   bg='#0e1c1d', font=("Arial", 10), fg='white', bd=0, highlightthickness=0)
        self.phi1_unit = tk.Label(self.window, text="Degrees", bg='#0e1c1d', font=("Arial", 12),
                                  fg='white', border=0)
        self.phi2_label = tk.Label(self.window, text="F2", bg='#0e1c1d', font=("Arial", 16),
                                   fg='white', border=0)
        self.phi2_scale = tk.Scale(self.window, from_=0, to=360, length=600, tickinterval=30, orient=tk.HORIZONTAL,
                                   bg='#0e1c1d', font=("Arial", 10), fg='white', bd=0, highlightthickness=0)
        self.phi2_unit = tk.Label(self.window, text="Degrees", bg='#0e1c1d', font=("Arial", 12),
                                  fg='white', border=0)
        self.btn_plot = tk.Button(text="Plot!", command=self.prepare, bg='#0e1c1d', font=("Arial", 20), fg='white',
                                  border=0)
        self.m1_scale.set(m1)
        self.m2_scale.set(m2)
        self.m3_scale.set(mc)
        self.v1_scale.set(v1)
        self.v2_scale.set(v2)
        self.r1_scale.set(r1)
        self.r2_scale.set(r2)
        self.phi1_scale.set(p1)
        self.phi1_scale.set(p2)

        # put all the UI elements on the interface
        self.m1_label.grid(row=0, column=0)
        self.m1_scale.grid(row=0, column=1)
        self.m1_unit.grid(row=0, column=2)
        self.m1_selector.grid(row=0, column=3)
        self.m2_label.grid(row=1, column=0)
        self.m2_scale.grid(row=1, column=1)
        self.m2_unit.grid(row=1, column=2)
        self.m2_selector.grid(row=1, column=3)
        self.m3_label.grid(row=2, column=0)
        self.m3_scale.grid(row=2, column=1)
        self.m3_unit.grid(row=2, column=2)
        self.m3_selector.grid(row=2, column=3)
        self.v1_label.grid(row=3, column=0)
        self.v1_scale.grid(row=3, column=1)
        self.v1_unit.grid(row=3, column=2)
        self.v2_label.grid(row=4, column=0)
        self.v2_scale.grid(row=4, column=1)
        self.v2_unit.grid(row=4, column=2)
        self.r1_label.grid(row=6, column=0)
        self.r1_scale.grid(row=6, column=1)
        self.r1_unit.grid(row=6, column=2)
        self.r2_label.grid(row=7, column=0)
        self.r2_scale.grid(row=7, column=1)
        self.r2_unit.grid(row=7, column=2)
        self.phi1_label.grid(row=9, column=0)
        self.phi1_scale.grid(row=9, column=1)
        self.phi1_unit.grid(row=9, column=2)
        self.phi2_label.grid(row=10, column=0)
        self.phi2_scale.grid(row=10, column=1)
        self.phi2_unit.grid(row=10, column=2)
        self.btn_plot.grid(row=12, column=1)
        self.home_butt = tk.Button(text="Back", bg='#0e1c1d', fg="white", border=0,
                                   command=lambda: self.home(self.window))
        self.home_butt.grid(row=12, column=2, pady=20)

        # show the window
        self.window.mainloop()

    # functions to read the input data
    def get_data(self):
        data = []
        MM = 6e24  # Normalizing mass
        data.append(self.m1_scale.get() * float(self.clicked1.get()) / MM)
        data.append(self.m2_scale.get() * float(self.clicked2.get()) / MM)
        data.append(self.m3_scale.get() * float(self.clicked3.get()) / MM)
        data.append(self.v1_scale.get())
        data.append(self.v2_scale.get())
        data.append(self.r1_scale.get())
        data.append(self.r2_scale.get())
        data.append(self.phi1_scale.get())
        data.append(self.phi2_scale.get())
        return data

    # initialization animation function: plot the background of each frame
    def init(self):
        self.line1.set_data([], [])
        self.line2.set_data([], [])
        self.ttl.set_text('')
        return self.line1, self.line2, self.ttl

    # Animation function. Reads out the position coordinates sequentially
    def animate(self, i):
        self.trail1 = 2000
        self.trail2 = 2000
        self.tm_yr = 'Elapsed time = ' + str(round(self.t[i], 1)) + ' years'
        self.ttl.set_text(self.tm_yr)
        self.line1.set_data(self.r1[i:max(1, i - self.trail1):-1, 0], self.r1[i:max(1, i - self.trail1):-1, 1])
        self.line2.set_data(self.r2[i:max(1, i - self.trail2):-1, 0], self.r2[i:max(1, i - self.trail2):-1, 1])
        return self.line1, self.line2,

    def mplot(self, fign, x, y, xl, yl, clr, lbl, alpha=1.0):
        plt.figure(fign)
        plt.xlabel(xl)
        plt.ylabel(yl)
        return plt.plot(x, y, clr, linewidth=1.0, label=lbl, alpha=alpha)

    def prepare(self):
        # resetting the figures
        # py.close(1)
        # py.close(2)
        # py.close(3)
        # py.close(4)
        for i in range(10):
            plt.close()
        self.canvas.flush_events()
        self.line1, self.line2, self.ttl = self.init()
        try:
            self.canvas.get_tk_widget().grid_forget()
        except AttributeError:
            pass

        # retrieving data from UI
        try:
            data = self.get_data()
            for i in range(7):
                if data[i] == 0:
                    raise Exception()
        except:
            tk.messagebox.showwarning("Warning", "Please set valid input values!")
            time.sleep(1)
            self.window.destroy()
            self.run(app=self.app, practice=self.practice, m1=0, m2=0, mc=0, v1=0, v2=0, r1=0, r2=0, p1=0, p2=0,s1=4,s2=4,s3=4)

        m1, m2, m3, vv1, vv2, rr1, rr2, phi1, phi2 = data
        ti = 0  # initial time = 0
        tf = 120  # final time = 120 years
        N = 100 * tf  # 100 points per year
        h = self.t[2] - self.t[1]  # time step (uniform)
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
        self.t[0] = ti
        self.r1[0, :] = r1i
        self.v1[0, :] = v1i
        self.r2[0, :] = r2i
        self.v2[0, :] = v2i

        KE1[0] = KineticEnergy(self.v1[0, :], m1)
        KE2[0] = KineticEnergy(self.v2[0, :], m2)
        PE1[0], PE2[0] = PotentialEnergy(self.r1[0, :], m1, self.r2[0, :], m2, m3)
        AM1[0] = AngMomentum(self.r1[0, :], self.v1[0, :], m1)
        AM2[0] = AngMomentum(self.r2[0, :], self.v2[0, :], m2)
        AreaVal1[0] = 0
        AreaVal2[0] = 0

        for i in range(0, N - 1):
            [self.r1[i + 1, :], self.v1[i + 1, :]] = RK4Solver(self.r1[i, :], self.r2[i, :], m1, m2, m3, self.v1[i, :],
                                                               self.v2[i, :], h, 1)
            [self.r2[i + 1, :], self.v2[i + 1, :]] = RK4Solver(self.r1[i, :], self.r2[i, :], m1, m2, m3, self.v1[i, :],
                                                               self.v2[i, :], h, 2)

            KE1[i + 1] = KineticEnergy(self.v1[i + 1, :], m1)
            KE2[i + 1] = KineticEnergy(self.v2[i + 1, :], m2)
            PE1[i + 1], PE2[i + 1] = PotentialEnergy(self.r1[i + 1, :], m1, self.r2[i + 1, :], m2, m3)
            AM1[i + 1] = AngMomentum(self.r1[i + 1, :], self.v1[i + 1, :], m1)
            AM2[i + 1] = AngMomentum(self.r2[i + 1, :], self.v2[i + 1, :], m2)
            AreaVal1[i + 1] = AreaVal1[i] + AreaCalc(self.r1[i, :], self.r1[i + 1, :])
            AreaVal2[i + 1] = AreaVal2[i] + AreaCalc(self.r2[i, :], self.r2[i + 1, :])
        self.do_plot(KE1, PE1, AM1, AreaVal1)

    def do_plot(self, KE1, PE1, AM1, AreaVal1):
        anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.init, frames=4000, interval=5, blit=True)
        self.canvas.flush_events()
        self.canvas.get_tk_widget().grid(row=0, column=4, rowspan=10)
        self.canvas.draw()

        G = 6.673e-11  # Gravitational Constant
        RR = 1.496e11  # Normalizing distance in km (= 1 AU)
        MM = 6e24  # Normalizing mass
        FF = (G * MM ** 2) / RR ** 2  # Unit force
        EE = FF * RR  # Unit energy

        lbl = 'orbit'
        plt.plot(0, 0, 'ro', linewidth=7)
        self.mplot(1, self.r1[:, 0], self.r1[:, 1], r'$x$ position (AU)', r'$y$ position (AU)', 'blue', 'M1', 0.1)
        self.mplot(1, self.r2[:, 0], self.r2[:, 1], r'$x$ position (AU)', r'$y$ position (AU)', 'green', 'M2', 0.1)
        plt.ylim([-9, 9])

        plt.axis('equal')
        self.mplot(2, self.t, KE1, r'Time, $t$ (years)',
                   r'Kinetice Energy, $KE$ ($\times$' + str("%.*e" % (2, EE)) + ' Joule)', 'blue', 'KE')
        self.mplot(2, self.t, PE1, r'Time, $t$ (years)',
                   r'Potential Energy, $KE$ ($\times$' + str("%.*e" % (2, EE)) + ' Joule)', 'red', 'PE')
        self.mplot(2, self.t, KE1 + PE1, r'Time, $t$ (years)',
                   r'Total Energy, $KE$ ($\times$' + str("%.*e" % (2, EE)) + ' Joule)', 'black', 'Total Energy')
        q = plt.legend(loc=0)
        q.draw_frame(False)
        plt.ylim([-180, 180])

        self.mplot(3, self.t, AM1, r'Time, $t$ (years)', r'Angular Momentum', 'black', lbl)
        plt.ylim([4, 8])

        self.mplot(4, self.t, AreaVal1, r'Time, $t$ (years)', r'Sweeped Area ($AU^2$)', 'black', lbl)
        plt.show()

    def home(self, window):
        for i in range(10):
            plt.close()
        window.destroy()
        global gapp
        print(gapp)
        print(self.practice)
        self.practice.run(practice=self.practice, app=gapp)
