#imports
import math
import formula.kinematics as kin

#quadratic equation solver for fall time:
import numpy as np


def quad(a,b,c):
    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)
    print("quad")
    print(a)
    print(b)
    print(c)
    print(d)
    print("----")

    # find two solutions
    sol1 = float((-b - math.sqrt(d)) / (2 * a))
    sol2 = float((-b + math.sqrt(d)) / (2 * a))

    return max(sol1,sol2)

# Differential equation solvers
# ===================================================================
def EulerSolver(t, r, v, h):
    z = np.zeros([2, 2])
    r1 = r + h * kin.dr_dt(t, r, v)
    v1 = v + h * kin.dv_dt(t, r, v)
    z = [r1, v1]
    return z


def EulerCromerSolver(t, r, v, h):
    z = np.zeros([2, 2])
    r = r + h * kin.dr_dt(t, r, v)
    v = v + h * kin.dv_dt(t, r, v)
    z = [r, v]
    return z


def RK4Solver(t, r, v, h, planet, ro, vo):
    k11 = kin.dr_dt(t, r, v, planet, ro, vo)
    k21 = kin.dv_dt(t, r, v, planet, ro, vo)

    k12 = kin.dr_dt(t + 0.5 * h, r + 0.5 * h * k11, v + 0.5 * h * k21, planet, ro, vo)
    k22 = kin.dv_dt(t + 0.5 * h, r + 0.5 * h * k11, v + 0.5 * h * k21, planet, ro, vo)

    k13 = kin.dr_dt(t + 0.5 * h, r + 0.5 * h * k12, v + 0.5 * h * k22, planet, ro, vo)
    k23 = kin.dv_dt(t + 0.5 * h, r + 0.5 * h * k12, v + 0.5 * h * k22, planet, ro, vo)

    k14 = kin.dr_dt(t + h, r + h * k13, v + h * k23, planet, ro, vo)
    k24 = kin.dv_dt(t + h, r + h * k13, v + h * k23, planet, ro, vo)

    y0 = r + h * (k11 + 2. * k12 + 2. * k13 + k14) / 6.
    y1 = v + h * (k21 + 2. * k22 + 2. * k23 + k24) / 6.

    z = np.zeros([2, 2])
    z = [y0, y1]
    return z
