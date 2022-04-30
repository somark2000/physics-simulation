import matplotlib.pyplot as plt
import pylab as py
from formula.calculates import *
from formula.kinematics import *
from matplotlib import animation, rc


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


# functions to read the input data
def get_data():
    data = []
    d=1/1e40
    m1 = 2e30  # Mass of Sun in kg
    m2 = 6e24  # Mass of Earth in kg
    m3 = 1.9e27  # Mass of Jupiter in kg
    r1 = 0  # dist of Sun from O in m
    r2 = 150.65e9  # dist of Earth from O in m
    r3 = 743.96e9  # dist of Jupiter from O in m
    v1=0
    v2 = 30e3
    v3 = 47e3
    data.append(m1)
    data.append(m2)
    data.append(m3)
    data.append(v1)
    data.append(v2)
    data.append(v3)
    data.append(r1)
    data.append(r2)
    data.append(r3)
    data.append(0)
    data.append(0)
    data.append(0)
    return data


# initialization animation function: plot the background of each frame
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line1, line2, line3

def mplot(fign, x, y, xl, yl, clr, lbl):
    py.figure(fign)
    py.xlabel(xl)
    py.ylabel(yl)
    return py.plot(x, y, clr, linewidth=1.0, label=lbl)


def prepare():
    data = get_data()
    m1, m2, m3, vv1, vv2, vv3, rr1, rr2, rr3, phi1, phi2, phi3 = data
    ti = 0  # initial time = 0
    tf = 10  # final time = 120 years
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
        [r1[i + 1, :], v1[i + 1, :]] = RK4Solver(m1, m2, m3, r1[i, :], r2[i, :], r3[i, :], v1[i, :], h, 1)
        [r2[i + 1, :], v2[i + 1, :]] = RK4Solver(m1, m2, m3, r1[i, :], r2[i, :], r3[i, :], v2[i, :], h, 2)
        [r3[i + 1, :], v3[i + 1, :]] = RK4Solver(m1, m2, m3, r1[i, :], r2[i, :], r3[i, :], v3[i, :], h, 3)

        KE1[i + 1], KE2[i + 1], KE3[i + 1] = KineticEnergy(v1[i + 1, :], v2[i + 1, :], v3[i + 1, :], m1, m2, m3)
        PE1[i + 1], PE2[i + 1], PE3[i + 1] = PotentialEnergy(m1, m2, m3, r1[i + 1, :], r2[i + 1, :], r3[i + 1, :])
        # AM1[i + 1] = AngMomentum(r1[i + 1, :], v1[i + 1, :], m1)
        # AM2[i+1] = AngMomentum(r2[i+1, :], v2[i+1, :], m2)
        # AM3[i+1] = AngMomentum(r3[i+1, :], v3[i+1, :], m3)
        # AreaVal1[i + 1] = AreaVal1[i] + AreaCalc(r1[i, :], r1[i + 1, :])
        # AreaVal2[i + 1] = AreaVal2[i] + AreaCalc(r2[i, :], r2[i + 1, :])
        # AreaVal3[i + 1] = AreaVal3[i] + AreaCalc(r3[i, :], r3[i + 1, :])
    print(r2)



# py.axis('equal')
# mplot(2, t, KE1, r'Time, $t$ (years)', r'Kinetice Energy, $KE$ ($\times$' + str("%.*e" % (2, EE)) + ' Joule)', 'blue',
#       'KE')
# mplot(2, t, PE1, r'Time, $t$ (years)', r'Potential Energy, $KE$ ($\times$' + str("%.*e" % (2, EE)) + ' Joule)', 'red',
#       'PE')
# mplot(2, t, KE1 + PE1, r'Time, $t$ (years)', r'Total Energy, $KE$ ($\times$' + str("%.*e" % (2, EE)) + ' Joule)', 'black',
#       'Total Energy')
# q = py.legend(loc=0)
# q.draw_frame(False)
# py.ylim([-180, 180])
#
# mplot(3, t, AM1, r'Time, $t$ (years)', r'Angular Momentum', 'black', lbl)
# py.ylim([4, 8])
#
# mplot(4, t, AreaVal1, r'Time, $t$ (years)', r'Sweeped Area ($AU^2$)', 'black', lbl)


# Animation function. Reads out the positon coordinates sequentially
def animate(i):
    trail1 = 200
    trail2 = 200
    trail3 = 200
    line1.set_data(r1[i:max(1, i - trail1):-1, 0], r1[i:max(1, i - trail1):-1, 1])
    line2.set_data(r2[i:max(1, i - trail2):-1, 0], r2[i:max(1, i - trail3):-1, 1])
    line3.set_data(r3[i:max(1, i - trail3):-1, 0], r3[i:max(1, i - trail3):-1, 1])
    return line1, line2, line3


# Function for setting up the animation
prepare()
fig, ax = py.subplots()
ax.axis('square')
ax.set_xlim((-90, 90))
ax.set_ylim((-90, 90))
ax.get_xaxis().set_ticks([])  # enable this to hide x axis ticks
ax.get_yaxis().set_ticks([])  # enable this to hide y axis ticks

lbl = 'orbit'
# py.plot(0, 0, 'ro', linewidth=7)
# mplot(1, r1[:, 0], r1[:, 1], r'$x$ position (AU)', r'$y$ position (AU)', 'blue', 'Earth')
# mplot(1, r2[:, 0], r2[:, 1], r'$x$ position (AU)', r'$y$ position (AU)', 'green', 'Super Jupiter')
# mplot(1, r3[:, 0], r3[:, 1], r'$x$ position (AU)', r'$y$ position (AU)', 'red', 'Sun')
# py.ylim([-90, 90])

# ax.plot(0, 0, 'o', markersize=9, markerfacecolor="#FDB813", markeredgecolor="#FD7813")
line1, = ax.plot([], [], 'o-', color='green', markevery=10000, markerfacecolor='green', lw=2)  # line for m1
line2, = ax.plot([], [], 'o-', color='blue', markevery=10000, markerfacecolor='blue', lw=2)  # line for m2
line3, = ax.plot([], [], 'o-', color='red', markevery=10000, markerfacecolor='red', lw=2)  # line for m3

# anim = animation.FuncAnimation(fig, animate, init_func=init,frames=4000, interval=5, blit=True)
a = [x[0] for x in r2]
b = [x[1] for x in r2]
print(a)
print('***')
print(b)
ax.plot(b,a)
plt.show()