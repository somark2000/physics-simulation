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
    g = 9.81 #m/s^2
    vel = g*t
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
    g = 9.81 #m/s^2
    y = h - (g*t**2)/2
    return y

def vt_velocity(v,t):
    """
    Calculates velocity of a freely falling object
    Args:
    -t: time
    -v: Initial velocity of the object
    Returns:
    -vel: free fall velocity
    """
    g = 9.81 #m/s^2
    vel = v - g*t
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
    y = h + (v*t) - (g*t**2)/2
    return y

def hz_position(v,t):
    return v*t

def position(vel,phi,time,height):
    t = sp.Symbol('t', real=True, positive=True)
    g = sp.Symbol('g', real=True, positive=True)
    v = sp.Symbol('v', real=True, positive=True)
    angle = sp.Symbol('angle', real=True, positive=True)
    h = sp.Symbol('h',real=True,positive=True)
    G = 9.81
    acc_x = 0
    acc_y = -g
    vel_x = sp.integrate(acc_x, t) + v * sp.cos(angle)
    vel_y = sp.integrate(acc_y, t) + v * sp.sin(angle)
    pos_x = sp.integrate(vel_x, t)
    pos_y = sp.integrate(vel_y, t) + h

    print('acc_x =', acc_x)
    print('acc_y =', acc_y)
    print('vel_x =', vel_x)
    print('vel_y =', vel_y)
    print('pos_x =', pos_x)
    print('pos_y =', pos_y)

    ANGLE = np.deg2rad(phi)

    pos_x_t = pos_x.subs({angle: ANGLE, v: vel})
    pos_y_t = pos_y.subs({v: vel, angle: ANGLE, g: G, h: height})
    print(pos_x_t)
    print(pos_y_t)
    pxs, pys = [], []
    print(("888888888888888888888"))

    for T in np.linspace(0, time):
        px = float(pos_x_t.subs(t, T))
        py = float(pos_y_t.subs(t, T))
        pxs.append(px)
        pys.append(py)
    return pxs,pys
