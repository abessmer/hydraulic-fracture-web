import numpy as np
from .fcn_pres_cal import fcn_pres_cal


def kgd_k_solution(Ep, mup, Kp, Cp, Q0, t, N):
    xi0 = np.linspace(0, 1, N + 1)
    xi = (xi0[:-1] + xi0[1:]) / 2

    l = 0
    eta = 0
    w = np.zeros(N)
    p = np.zeros(N)

    l = 0.9324 * (Ep * Q0 * t / Kp)**(2/3)
    eta = 1
    w = 0.6828 * (Kp**2 * Q0 * t / Ep**2)**(1/3) * (1 - xi**2)**(1/2)
    p = 0.1831 * (Kp**4 / Ep / Q0 / t)**(1/3) * np.ones(N)

    return l, w, p.flatten(), xi, eta


def kgd_m_solution(Ep, mup, Kp, Cp, Q0, t, N):
    xi0 = np.linspace(0, 1, N + 1)
    xi = (xi0[:-1] + xi0[1:]) / 2

    l = 0
    eta = 0
    w = np.zeros(N)
    p = np.zeros(N)

    l = 0.6159 * (Q0**3 * Ep * t**4 / mup)**(1/6)
    eta = 1
    w = 1.1265 * (mup * Q0**3 * t**2 / Ep)**(1/6) * \
        (1 + xi)**0.588 * (1 - xi)**(2/3)
    p = 2.7495 * (mup * Ep**2 / t)**(1/3) * \
        fcn_pres_cal(2/3, 0.588, xi, 1)

    return l, w, p.flatten(), xi, eta


def kgd_kt_solution(Ep, mup, Kp, Cp, Q0, t, N):
    xi0 = np.linspace(0, 1, N + 1)
    xi = (xi0[:-1] + xi0[1:]) / 2

    l = 0
    eta = 0
    w = np.zeros(N)
    p = np.zeros(N)

    l = 0.3183 * Q0 * t**(1/2) / Cp
    eta = 0
    w = 0.3989 * (Kp**4 * Q0**2 * t / Ep**4 / Cp **
                  2)**(1/4) * (1 - xi**2)**(1/2)
    p = 0.3183 * (Kp**4 * Cp**2 / Q0**2 / t)**(1/4) * np.ones(N)

    return l, w, p.flatten(), xi, eta


def kgd_mt_solution(Ep, mup, Kp, Cp, Q0, t, N):
    xi0 = np.linspace(0, 1, N + 1)
    xi = (xi0[:-1] + xi0[1:]) / 2

    l = 0
    eta = 0
    w = np.zeros(N)
    p = np.zeros(N)

    l = 0.3183 * Q0 * t**(1/2) / Cp
    eta = 0
    w = 0.8165 * (mup * Q0**3 * t / Ep / Cp**2)**(1 /
                                                  4) * (1 + xi)**0.520 * (1 - xi)**(5/8)
    p = 3.6783 * (Cp**2 * mup * Ep**3 / t / Q0)**(1 /
                                                  4) * fcn_pres_cal(5/8, 0.520, xi, 1)

    return l, w, p.flatten(), xi, eta
