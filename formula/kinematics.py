import math

import sympy as sp
import numpy as np


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
    '''
    Caclulates the horizontal position of the projectile at a given moment
    :param v: initial velocity
    :param t: time
    :return: position
    '''
    return v * t


def position(vel, phi, time, height):
    '''
    Calculates the position in a xOy system of the projectile at any time
    :param vel: initial value of the velocity
    :param phi: initial angle between the horizontal and the velocity vector
    :param time: plotting time
    :param height: initial height
    :return: lists with the x and y positions accordingly
    '''
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
    """
    Calculates the resultant velocity at any given moment
    :param vel: initial velocity
    :param phi: initial angle
    :param time: plotting time
    :return: list of velocities
    """
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

# Symbolic equation solver for force between two bodies
def focrce_function(m1, m2, r):
    G = 6.673e-11  # Gravitational Constant)
    F=(m1*m2)/(r[1]**2+r[0]**2)*G
    return F

def force_12(r1,r2,m1,m2):
    '''
    force between m1 and m2
    :param m1: mass of m1
    :param m2: mass of m2
    :param r: distance between the two astronomical objects
    :return: force on the axes
    '''
    r = np.zeros(2)
    F = np.zeros(2)
    r[0] = r1[0] - r2[0]
    r[1] = r1[1] - r2[1]
    Fmag = focrce_function(m1,m2,r) / (np.linalg.norm(r) + 1e-20) ** 2
    theta = math.atan(np.abs(r[1]) / (np.abs(r[0]) + 1e-20))
    F[0] = Fmag * np.cos(theta)
    F[1] = Fmag * np.sin(theta)
    if r[0] < 0:
        F[0] = -F[0]
    if r[1] < 0:
        F[1] = -F[1]
    return F


def force_13(r1,r3,m1,m3):
    '''
    force between m1 and m3
    :param r: distance between the two astronomical objects
    :param m1: mass of m1
    :param m3: mass of m3
    :return: force on the axes
    '''
    r = np.zeros(2)
    F = np.zeros(2)
    r[0] = r1[0] - r3[0]
    r[1] = r1[1] - r3[1]
    Fmag = focrce_function(m1,m3,r) / (np.linalg.norm(r) + 1e-20) ** 2
    theta = math.atan(np.abs(r[1]) / (np.abs(r[0]) + 1e-20))
    F[0] = Fmag * np.cos(theta)
    F[1] = Fmag * np.sin(theta)
    if r[0] < 0:
        F[0] = -F[0]
    if r[1] < 0:
        F[1] = -F[1]
    return F


def force_23(r2, r3, m2, m3):
    '''
    force between m2 and m3
    :param r2: position of m2
    :param r3: position of m3
    :param m2: mass of m2
    :param m3: mass of m3
    :return: force on the axes
    '''
    r = np.zeros(2)
    F = np.zeros(2)
    r[0] = r2[0] - r3[0]
    r[1] = r2[1] - r3[1]
    Fmag = focrce_function(m2,m3,r) / (np.linalg.norm(r) + 1e-20) ** 2
    theta = math.atan(np.abs(r[1]) / (np.abs(r[0]) + 1e-20))
    F[0] = Fmag * np.cos(theta)
    F[1] = Fmag * np.sin(theta)
    if r[0] < 0:
        F[0] = -F[0]
    if r[1] < 0:
        F[1] = -F[1]
    return F


def force(m1, m2, m3, r1, r2, r3, planet):
    '''
    calculates all the forces for the selected planet
    :param m1:
    :param m2:
    :param m3:
    :param r1:
    :param r2:
    :param r3:
    :param planet:
    :return:
    '''
    if planet == 1:
        return force_12(r1, r2, m1, m2) + force_13(r1, r3, m1, m3)
    if planet == 2:
        return force_12(r1, r2, m1, m2) + force_23(r2, r3, m2, m3)
    if planet == 3:
        return force_13(r1, r3, m1, m3) + force_23(r2, r3, m2, m3)


def dr_dt(v):
    return v


def dv_dt(m1, m2, m3, r1, r2, r3, planet):
    F = force(m1, m2, m3, r1, r2, r3, planet)
    if planet == 1:
        a = F / m1
    if planet == 2:
        a = F / m2
    if planet == 3:
        a = F / m3
    return a


def KineticEnergy(v1, v2, v3, m1, m2, m3):
    vn1 = np.linalg.norm(v1)
    vn2 = np.linalg.norm(v2)
    vn3 = np.linalg.norm(v3)
    return 0.5 * m1 * vn1 ** 2, 0.5 * m2 * vn2 ** 2, 0.5 * m3 * vn3 ** 2


def PotentialEnergy(m1, m2, m3, r1, r2, r3):
    fmag1 = np.linalg.norm(force(m1, m2, m3, r1, r2, r3, 1))
    rmag1 = np.linalg.norm(r1)
    fmag2 = np.linalg.norm(force(m1, m2, m3, r1, r2, r3, 2))
    rmag2 = np.linalg.norm(r2)
    fmag3 = np.linalg.norm(force(m1, m2, m3, r1, r2, r3, 3))
    rmag3 = np.linalg.norm(r3)
    return -fmag1 * rmag1, -fmag2 * rmag2, -fmag3 * rmag3


def AngMomentum(r, v, m):
    rn = np.linalg.norm(r)
    vn = np.linalg.norm(v)
    r = [x / rn for x in r]
    v = [x / vn for x in v]

    print("///")
    print(r)
    print(v)
    rdotv = r[0] * v[0] + r[1] * v[1]
    theta = math.acos(rdotv)
    return m * rn * vn * np.sin(theta)


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
