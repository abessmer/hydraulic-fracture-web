import numpy as np
from scipy.special import beta
from .fcn_g_del import fcn_g_del
from .fcn_b_kgd import fcn_b_kgd
from .fcn_delta_p import fcn_delta_p
from .fcn_lam_kgd import fcn_lam_kgd

def kgd_hf_appr(tau, Km):
    """
    TODO describe this

    Args:
        tau (numpy.ndarray): Input tau values.
        Km (numpy.ndarray): Input Km values.

    Returns:
        tuple: Om, gamma, eff, del_val, lam_val, alp
    """
    Km = np.where(Km < 1e-30, 1e-30, Km)

    th = tau * (2**6) * (Km**-12)
    Qh = Km**-4 / 2

    # initial guess (for viscous regime)
    alp = 2/3
    Kh0 = 0 * th + 1/2
    Ch0 = 0 * th + 1/2

    # alpha iteration
    for ialp in range(1, 4):

        Res = 1
        ittmax = 100
        itt = 0
        tol = 1e-5

        while (itt < ittmax) and (Res > tol):

            if (itt == ittmax - 1) and (ialp == 3):
                print('No convergence, wl_radHF_appr')
                print(Res)
            itt += 1
            Kh = Kh0.copy()
            Ch = Ch0.copy()

            ittK = 0
            ResK = 1
            eps_val = np.finfo(float).eps
            while (ittK < ittmax) and (ResK > tol):
                ittK += 1
                fg = fcn_g_del(Kh, Ch)  # Placeholder function
                fgK = (-fg) / (1 - Kh + eps_val)
                f1 = Kh**6 - alp**(1/2) / th**(1/2) * Ch**3 * fg
                f1K = 6 * Kh**5 - alp**(1/2) / th**(1/2) * Ch**3 * fgK

                Kh = 0.0 * Kh + 1.0 * (Kh - f1 / f1K)
                Kh = np.where(Kh < 0, 1e-5, Kh)
                Kh = np.where(Kh > 1, 1 - 1e-5, Kh)

                ResK = np.max(np.abs(f1 / f1K))

            ittC = 0
            ResC = 1
            while (ittC < ittmax) and (ResC > tol):
                ittC += 1
                Chtest = Ch.copy()

                Ch = th**(1/6) * Kh**(2/3) / alp**(1/2) / Qh**(1/3) * (fcn_b_kgd(Kh, Ch, alp))**(1/3) # Placeholder function

                ResC = np.max(np.abs(Ch - Chtest))

            Res = np.max(np.sqrt((Kh - Kh0)**2 + (Ch - Ch0)**2))

            Kh0 = Kh.copy()
            Ch0 = Ch.copy()

        sh = fcn_g_del(Kh, Ch) # Placeholder function

        # calculate length
        lh = Ch**4 * sh**2 / Kh**10

        # update alpha
        alp_new = np.zeros_like(lh)
        alp_new[1:] = (np.log(lh[1:]) - np.log(lh[:-1])) / (np.log(th[1:]) - np.log(th[:-1]))
        alp_new[0] = alp_new[1]
        alp = alp_new


    p = 0.0  # parameter for delta calculations
    del_val = (1 + fcn_delta_p(Kh, Ch, p)) / 2 # Placeholder function

    # efficiency
    eff = 1 - Ch * alp**(3/2) * beta(alp, 3/2) / fcn_b_kgd(Kh, Ch, alp) # Placeholder function

    # width at the wellbore
    lam_val = fcn_lam_kgd(Kh, Ch, alp) # Placeholder function
    wha = Ch**2 * sh / Kh**6 / (2**lam_val)

    # converting to original scaling
    gamma = lh / (2**4) * Km**10
    Om = wha / (2**2) * Km**6

    return Om, gamma, eff, del_val, lam_val, alp