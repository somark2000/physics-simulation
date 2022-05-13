# imports
import math
import formula.kinematics as kin
import numpy as np
import sympy as sp


# Quadratic equation solver for fall time:
def quad(a, b, c):
    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)

    # find two solutions
    sol1 = float((-b - math.sqrt(d)) / (2 * a))
    sol2 = float((-b + math.sqrt(d)) / (2 * a))

    return max(sol1, sol2)


# Differential equation solvers
# def EulerSolver(t, r, v, h):
#     z = np.zeros([2, 2])
#     r1 = r + h * kin.dr_dt(t, r, v)
#     v1 = v + h * kin.dv_dt(t, r, v)
#     z = [r1, v1]
#     return z
#
#
# def EulerCromerSolver(t, r, v, h):
#     z = np.zeros([2, 2])
#     r = r + h * kin.dr_dt(t, r, v)
#     v = v + h * kin.dv_dt(t, r, v)
#     z = [r, v]
#     return z


def RK4Solver(r1,r2,m1,m2,M, v1, v2, h, planet):
    if planet == 1:
        k11 = kin.dr_dt(v1)
        k21 = kin.dv_dt(r1, r2, m1, m2, M, planet)

        k12 = kin.dr_dt(v1 + 0.5 * h * k21)
        k22 = kin.dv_dt(r1 + 0.5 * h * k11,r2,m1,m2,M,planet)

        k13 = kin.dr_dt(v1 + 0.5 * h * k22)
        k23 = kin.dv_dt(r1 + 0.5 * h * k12,r2,m1,m2,M,planet)

        k14 = kin.dr_dt(v1 + h * k23)
        k24 = kin.dv_dt(r1 + h * k13,r2,m1,m2,M,planet)
        y0 = r1 + h * (k11 + 2. * k12 + 2. * k13 + k14) / 6.
        y1 = v1 + h * (k21 + 2. * k22 + 2. * k23 + k24) / 6.

    if planet == 2:
        k11 = kin.dr_dt(v2)
        k21 = kin.dv_dt(r1, r2, m1, m2, M, planet)

        k12 = kin.dr_dt(v2 + 0.5 * h * k21)
        k22 = kin.dv_dt(r1, r2 + 0.5 * h * k11, m1, m2, M, planet)

        k13 = kin.dr_dt(v2 + 0.5 * h * k22)
        k23 = kin.dv_dt(r1, r2 + 0.5 * h * k12, m1, m2, M, planet)

        k14 = kin.dr_dt(v2 + h * k23)
        k24 = kin.dv_dt(r1, r2 + h * k13, m1, m2, M, planet)
        y0 = r2 + h * (k11 + 2. * k12 + 2. * k13 + k14) / 6.
        y1 = v2 + h * (k21 + 2. * k22 + 2. * k23 + k24) / 6.

    z = [y0, y1]
    return z
