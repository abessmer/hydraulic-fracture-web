import numpy as np
import warnings

def fcn_g_del(Kh, Ch):
    # Kh<0 or complex
    iKh = (Kh < 0) | (np.abs(np.imag(Kh)) > 0)
    if np.any(iKh):
        Kh[iKh] = 0
        warnings.warn('Warning: Kh is negative or complex in fcn_g_del')

    # to fix the M vertex
    Kh = Kh + np.finfo(float).eps

    # no propagation in this case
    Kh = np.clip(Kh, None, 1)

    # Ch<0 or complex
    iCh0 = (Ch < 0) | (np.abs(np.imag(Ch)) > 0)
    if np.any(iCh0):
        Ch[iCh0] = 0
        warnings.warn('Warning: Ch is negative or complex in fcn_g_del')

    betam = 2**(1/3) * 3**(5/6)
    betamt = 4 / (15**(1/4)) / ((np.sqrt(2) - 1)**(1/4))
    b0 = 3 * betamt**4 / 4 / betam**3  # b0=0.9912

    def f(Kh, Ch, C1):
        term_atanh = np.arctanh((1 - Kh) / (2 * Ch + 1 + Kh))
        return (1 - Kh**3 - 3/2 * Ch * (1 - Kh**2) + 3 * Ch**2 * (1 - Kh) - 3 * Ch**3 * 2 * term_atanh) / (3 * C1)

    def fkmt(Kh, Ch, C1):
        return (1 / (4 * Ch) * (1 - Kh**4) - 1 / (5 * Ch**2) * (1 - Kh**5) + 1 / (6 * Ch**3) * (1 - Kh**6)) / C1

    def C1_func(del_val):  # Renamed to avoid shadowing built-in C1
        return 4 * (1 - 2 * del_val) / (del_val * (1 - del_val)) * np.tan(np.pi * del_val)

    def C2_func(del_val):  # Renamed to avoid shadowing built-in C2
        return 16 * (1 - 3 * del_val) / (3 * del_val * (2 - 3 * del_val)) * np.tan(3 * np.pi / 2 * del_val)

    iCh_large = Ch > 1e3

    del_val = (betam**3 / 3) * f(Kh, b0 * Ch, betam**3 / 3) * (1 + b0 * Ch)
    if np.any(iCh_large):
        del_val[iCh_large] = (betam**3 / 3) * fkmt(Kh[iCh_large], b0 * Ch[iCh_large], betam**3 / 3) * (1 + b0 * Ch[iCh_large])

    del_val = np.clip(del_val, 1e-6, 1/3 - 1e-6) # Clamping del values

    bh = C2_func(del_val) / C1_func(del_val)

    xh = f(Kh, Ch * bh, C1_func(del_val))
    if np.any(iCh_large):
        xh[iCh_large] = fkmt(Kh[iCh_large], Ch[iCh_large] * bh[iCh_large], C1_func(del_val[iCh_large]))

    return xh