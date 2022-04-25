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