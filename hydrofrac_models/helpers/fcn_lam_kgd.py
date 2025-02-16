import numpy as np
from scipy.special import beta, betainc
from .fcn_delta_p import fcn_delta_p

def fcn_lam_kgd(Kh, Ch, alp):
    """
    TODO describe this

    Calculates 'lam' based on inputs Kh, Ch, and alp, using
    empirically defined constants and mathematical functions.

    Args:
        Kh (float or numpy.ndarray): Input parameter Kh.
        Ch (float or numpy.ndarray): Input parameter Ch.
        alp (float or numpy.ndarray): Input parameter alp.

    Returns:
        float or numpy.ndarray: Calculated value of lam.
    """

    lamK = 0.5  # for K and Kt vertex
    lamM = 0.588  # for M vertex
    lamMt = 0.520  # for Mt vertex

    # zeroth approximation for the efficiency
    lam0 = 0.5
    delta = (1 + fcn_delta_p(Kh, Ch, 0)) / 2  # Assuming fcn_Delta_p is defined elsewhere

    def B0(x, p1, p2):
        return beta(p1, p2) * (1 - betainc(p1, p2, x))

    fcn_B2 = 2**(1 + delta) * B0(1/2, lam0 + 1, 1 + delta) + Ch * alp**(3/2) * beta(alp, 3/2)
    eta0 = 1 - Ch * alp**(3/2) * beta(alp, 3/2) / fcn_B2

    # lambda interpolation
    pK = Kh**(3)
    peta = eta0
    lam = lamM * (1 - pK) * peta + lamMt * (1 - pK) * (1 - peta) + lamK * pK
    return lam