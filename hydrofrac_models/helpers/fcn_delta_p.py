import numpy as np
import warnings

def fcn_delta_p(Kh, Ch, p):
    """
    TODO describe this

    Args:
        Kh (float or numpy.ndarray): Input parameter Kh.
        Ch (float or numpy.ndarray): Input parameter Ch.
        val (float or numpy.ndarray): Input value (in this context, 0).

    Returns:
        float or numpy.ndarray:  Result of fcn_Delta_p.
    """

    # Kh<0 or complex
    iKh = (Kh < 0) | (np.abs(np.imag(Kh)) > 0) # | is element-wise OR for numpy arrays
    if np.any(iKh):
        Kh[iKh] = 0
        warnings.warn('Warning: Kh is negative or complex in fcn_Delta_p')

    # to fix the M vertex
    Kh = Kh + np.finfo(float).eps

    # no propagation in this case
    Kh = np.clip(Kh, None, 1) # Equivalent to Kh(Kh>1)=1 in Matlab

    # Ch<0 or complex
    iCh0 = (Ch < 0) | (np.abs(np.imag(Ch)) > 0)
    if np.any(iCh0):
        Ch[iCh0] = 0
        warnings.warn('Warning: Ch is negative or complex in fcn_Delta_p')

    betam = 2**(1/3) * 3**(5/6)
    betamt = 4 / (15**(1/4)) / ((np.sqrt(2) - 1)**(1/4))
    b0 = 3 * betamt**4 / 4 / betam**3  # b0=0.9912

    def f(Kh, Ch, C1):
        term_atanh = np.arctanh((1 - Kh) / (2 * Ch + 1 + Kh))
        return (1 - Kh**3 - 3/2 * Ch * (1 - Kh**2) + 3 * Ch**2 * (1 - Kh) - 3 * Ch**3 * 2 * term_atanh) / (3 * C1)

    def fkmt(Kh, Ch, C1):
        return (1 / (4 * Ch) * (1 - Kh**4) - 1 / (5 * Ch**2) * (1 - Kh**5) + 1 / (6 * Ch**3) * (1 - Kh**6)) / C1

    iCh_large = Ch > 1e3

    Delta = (betam**3 / 3) * f(Kh, Ch * b0, betam**3 / 3) * (1 + b0 * Ch)
    if np.any(iCh_large):
        Delta[iCh_large] = (betam**3 / 3) * fkmt(Kh[iCh_large], Ch[iCh_large] * b0, betam**3 / 3) * (1 + b0 * Ch[iCh_large])

    Deltap = (1 - p + p * f(Kh, Ch * b0, betam**3 / 3) * (betam**3 + betamt**4 * Ch)) * Delta
    if np.any(iCh_large):
        Deltap[iCh_large] = (1 - p + p * fkmt(Kh[iCh_large], Ch[iCh_large] * b0, betam**3 / 3) * (betam**3 + betamt**4 * Ch[iCh_large])) * Delta[iCh_large]

    return Deltap