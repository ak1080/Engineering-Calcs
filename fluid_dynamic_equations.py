import numpy as np
from scipy.optimize import fsolve

GRAVITY = 32.174 # ft/s^2

def reynolds_num(density, velocity, diam, visc):
    """Simple function to calculate Reynolds number"""
    reynolds = (density * velocity * diam / 12) / visc
    return reynolds

def darcy_weisbach(f, length, velocity, diam):
    """Calculates the pressure loss in ft of head for a straight section of pipe using the Darcy equation"""
    darcy_weisbach = round((f * length * velocity ** 2) / (diam / 12 * 2 * GRAVITY),2)
    return darcy_weisbach

def colebrook_white_solver_fsolve(re, epsilon, diam, initial_guess=0.02):
    """ Solves the Colebrook-White equation for the Darcy-Weisbach friction factor using fsolve."""
    # Define the Colebrook-White equation function. Set to zero and use a root finding method to solve for f.
    def colebrook_white(f):
        return 1/np.sqrt(f) + 2 * np.log10((epsilon / diam) / 3.7 + 2.51 / (re * np.sqrt(f)))
    # Solve for f using fsolve
    friction_factor: object = round(fsolve(colebrook_white, initial_guess)[0], 4)
    return friction_factor