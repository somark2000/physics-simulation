import math

import sympy as sp
import numpy as np

Me = 6e24  # Mass of Earth in kg
Ms = 2e30  # Mass of Sun in kg
Mj = 1.9e27  # Mass of Jupiter

G = 6.673e-11  # Gravitational Constant

RR = 1.496e11  # Normalizing distance in km (= 1 AU)
MM = 6e24  # Normalizing mass
TT = 365 * 24 * 60 * 60.0  # Normalizing time (1 year)

FF = (G * MM ** 2) / RR ** 2  # Unit force
EE = FF * RR  # Unit energy

GG = (MM * G * TT ** 2) / (RR ** 3)

Me = Me / MM  # Normalized mass of Earth
Ms = Ms / MM  # Normalized mass of Sun
Mj = 500 * Mj / MM  # Normalized mass of Jupiter/Super Jupiter


def ff_velocity(t):
    """
    Calculates velocity of a freely falling object
    Args:
    -t: time
    Returns:
    -vel: free fall velocity
    """
    g = 9.81  # m/s^2
    vel = g * t
    return vel


def ff_position(t, h):
    """
    Calculates position of a freely falling object
    Args:
    -vel: Velocity of the object at a given time
    -t: time
    Returns:
    -y: Position of the body
    """
    g = 9.81  # m/s^2
    y = h - (g * t ** 2) / 2
    return y


def vt_velocity(v, t):
    """
    Calculates velocity of a freely falling object
    Args:
    -t: time
    -v: Initial velocity of the object
    Returns:
    -vel: free fall velocity
    """
    g = 9.81  # m/s^2
    vel = v - g * t
    return vel


def vt_position(v, t, h):
    """
    Calculates position of a freely falling object
    Args:
    -v: Initial velocity of the object
    -t: time
    Returns:
    -y: Position of the body
    """
    g = 9.81  # m/s^2
    y = h + (v * t) - (g * t ** 2) / 2
    return y


def hz_position(v, t):
    return v * t


def position(vel, phi, time, height):
    t = sp.Symbol('t', real=True, positive=True)
    g = sp.Symbol('g', real=True, positive=True)
    v = sp.Symbol('v', real=True, positive=True)
    angle = sp.Symbol('angle', real=True, positive=True)
    h = sp.Symbol('h', real=True, positive=True)
    G = 9.81
    acc_x = 0
    acc_y = -g
    vel_x = sp.integrate(acc_x, t) + v * sp.cos(angle)
    vel_y = sp.integrate(acc_y, t) + v * sp.sin(angle)
    pos_x = sp.integrate(vel_x, t)
    pos_y = sp.integrate(vel_y, t) + h

    ANGLE = np.deg2rad(phi)

    pos_x_t = pos_x.subs({angle: ANGLE, v: vel})
    pos_y_t = pos_y.subs({v: vel, angle: ANGLE, g: G, h: height})
    pxs, pys = [], []

    for T in np.linspace(0, time):
        px = float(pos_x_t.subs(t, T))
        py = float(pos_y_t.subs(t, T))
        pxs.append(px)
        pys.append(py)
    return pxs, pys


def v_tot(vel, phi, time):
    t = sp.Symbol('t', real=True, positive=True)
    g = sp.Symbol('g', real=True, positive=True)
    v = sp.Symbol('v', real=True, positive=True)
    angle = sp.Symbol('angle', real=True, positive=True)
    G = 9.81
    ANGLE = np.deg2rad(phi)
    acc_x = 0
    acc_y = -g
    vel_x = sp.integrate(acc_x, t) + v * sp.cos(angle)
    vel_y = sp.integrate(acc_y, t) + v * sp.sin(angle)

    vel_x_t = vel_x.subs({angle: ANGLE, v: vel})
    vel_y_t = vel_y.subs({angle: ANGLE, v: vel, g: G})
    velocity = []

    for T in np.linspace(0, time):
        vx = float(vel_x_t.subs(t, T))
        vy = float(vel_y_t.subs(t, T))
        velocity.append(math.sqrt(vx ** 2 + vy ** 2))
    return velocity


def force_es(r):
    F = np.zeros(2)
    Fmag = GG * Me * Ms / (np.linalg.norm(r) + 1e-20) ** 2
    theta = math.atan(np.abs(r[1]) / (np.abs(r[0]) + 1e-20))
    F[0] = Fmag * np.cos(theta)
    F[1] = Fmag * np.sin(theta)
    if r[0] > 0:
        F[0] = -F[0]
    if r[1] > 0:
        F[1] = -F[1]

    return F


def force_js(r):
    F = np.zeros(2)
    Fmag = GG * Mj * Ms / (np.linalg.norm(r) + 1e-20) ** 2
    theta = math.atan(np.abs(r[1]) / (np.abs(r[0]) + 1e-20))
    F[0] = Fmag * np.cos(theta)
    F[1] = Fmag * np.sin(theta)
    if r[0] > 0:
        F[0] = -F[0]
    if r[1] > 0:
        F[1] = -F[1]

    return F


def force_ej(re, rj):
    r = np.zeros(2)
    F = np.zeros(2)
    r[0] = re[0] - rj[0]
    r[1] = re[1] - rj[1]
    Fmag = GG * Me * Mj / (np.linalg.norm(r) + 1e-20) ** 2
    theta = math.atan(np.abs(r[1]) / (np.abs(r[0]) + 1e-20))
    F[0] = Fmag * np.cos(theta)
    F[1] = Fmag * np.sin(theta)
    if r[0] > 0:
        F[0] = -F[0]
    if r[1] > 0:
        F[1] = -F[1]

    return F


def force(r, planet, ro, vo):
    if planet == 'earth':
        return force_es(r) + force_ej(r, ro)
    if planet == 'jupiter':
        return force_js(r) - force_ej(r, ro)


def dr_dt(t, r, v):
    return v


def dr_dt(t, r, v, planet, ro, vo):
    return v


def dv_dt(t, r, v, planet=None, ro=None, vo=None):
    F = force(r, planet, ro, vo)
    if planet == 'earth':
        y = F / Me
    if planet == 'jupiter':
        y = F / Mj
    return y


def KineticEnergy(v):
    vn = np.linalg.norm(v)
    return 0.5 * Me * vn ** 2


def PotentialEnergy(r):
    fmag = np.linalg.norm(force_es(r))
    rmag = np.linalg.norm(r)
    return -fmag * rmag


def AngMomentum(r, v):
    rn = np.linalg.norm(r)
    vn = np.linalg.norm(v)
    r = r / rn
    v = v / vn
    rdotv = r[0] * v[0] + r[1] * v[1]
    theta = math.acos(rdotv)
    return Me * rn * vn * np.sin(theta)


def AreaCalc(r1, r2):
    r1n = np.linalg.norm(r1)
    r2n = np.linalg.norm(r2)
    r1 = r1 + 1e-20
    r2 = r2 + 1e-20
    theta1 = math.atan(abs(r1[1] / r1[0]))
    theta2 = math.atan(abs(r2[1] / r2[0]))
    rn = 0.5 * (r1n + r2n)
    del_theta = np.abs(theta1 - theta2)
    return 0.5 * del_theta * rn ** 2
