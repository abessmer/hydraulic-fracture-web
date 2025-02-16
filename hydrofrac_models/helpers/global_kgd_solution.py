import numpy as np
from .kgd_hf_appr import kgd_hf_appr
from .fcn_pres_cal import fcn_pres_cal

def global_kgd_solution(Ep, mup, Kp, Cp, Q0, t, N):
    """
    TODO describe this function

    Args:
        Ep (float): Parameter Ep.
        mup (float): Parameter mup.
        Kp (float): Parameter Kp.
        Cp (float): Parameter Cp.
        Q0 (float): Parameter Q0.
        t (float): Time t.
        N (int): Number of points N.

    Returns:
        tuple: A tuple containing l, w, p, xi, eta.
            l (float): Unscaled length.
            w (numpy.ndarray): Unscaled width.
            p (numpy.ndarray): Unscaled pressure.
            xi (numpy.ndarray): Spatial coordinate xi.
            eta (float): Efficiency eta.
    """

    tmmt = mup * (Q0**3) / (Ep * (Cp**6))

    # dimensionless parameters
    tau = t / tmmt
    Km = (Kp**4 / (mup * Q0 * Ep**3))**(1/4)

    # determine length and width
    tau2 = np.array([tau/4, tau/2, tau])
    Om, gamma, eff, del_val, lam, _ = kgd_hf_appr(tau2, Km)  # Assuming KGD_HF_appr is defined elsewhere

    # scales
    Lst = (mup * (Q0**5) / (Ep * (Cp**8)))**(1/2)
    Eps = (Cp**2) / Q0

    xi0 = np.linspace(0, 1, N + 1)
    xi = (xi0[:-1] + xi0[1:]) / 2

    # unscaled results
    l = gamma[2] * Lst  # Index 3 in Matlab is index 2 in Python
    w = Om[2] * Eps * Lst * (1 - xi)**(del_val[2]) * (1 + xi)**(lam[2])
    p = Eps * Ep * (2**lam[2]) * Om[2] / gamma[2] * fcn_pres_cal(del_val[2], lam[2], xi.reshape(-1, 1), 1) # Assuming fcn_pres_cal is defined elsewhere, xi' in Matlab is xi transpose

    eta = eff[2] # Index 3 in Matlab is index 2 in Python

    return l, w, p.flatten(), xi, eta