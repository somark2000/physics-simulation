def potential_energy(m,h):
    """
    Calculates potential energy of a body of mass m at height h
    Args:
    -m: Mass of the object
    -h: Height of the object
    Returns:
    -p_e: Potential energy
    """
    g = 9.81 #m/s^2
    p_e = m*g*h
    return p_e

def kinetic_energy(m,v):
    """
    Calculates kinetic energy of a body
    Args:
    -m: Mass of the object
    -v: Velocity of the object
    Returns:
    -k_e: Kinetic Energy
    """
    k_e = ((1/2)*m*(v**2))
    return k_e

def ke_by_pe(ke,pe):
    """
    Calculates the ratio of KE to PE
    Args:
    -ke: Kinetic energy
    -pe: Potential energy
    Returns:
    -ratio: KE/PE
    """
    ratio = ke/pe
    return ratio