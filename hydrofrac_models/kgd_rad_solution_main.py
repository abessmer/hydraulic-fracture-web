import numpy as np
import matplotlib.pyplot as plt
import sys

from hydrofrac_models.helpers.global_kgd_solution import get_kgd_sol
from hydrofrac_models.helpers.kgd_local_solutions import kgd_vert_sol

# # Assuming 'KGD-rad_sol_fcns' is a directory in the same location as this script
# # If not, you need to add the path to sys.path, e.g.,
# # sys.path.append('/path/to/KGD-rad_sol_fcns')
# try:
#     from KGD_rad_sol_fcns import get_KGD_sol, KGD_vert_sol, get_rad_sol, rad_vert_sol
# except ImportError:
#     print("Error: Could not import functions from KGD_rad_sol_fcns directory.")
#     print("Please ensure that the KGD_rad_sol_fcns directory is in the same directory as this script,")
#     print("or add the correct path to sys.path.")
#     # You can choose to exit here if the functions are essential
#     # sys.exit(1) # Uncomment to exit if functions are crucial and not found


# material parameters
Ep = 15/(1-0.2**2)  # GPa
mup = 12*0.02  # Pa s
Kp = 4*(2/np.pi)**0.5*1  # MPa*m^(1/2)
Q0 = 0.0004*1e3  # [m^3/s]*10^-3
H = 50  # m
t = 100  # s  (assuming t is time in seconds, based on context)
Cp = 2*3*1e-6*1e3

# number of points
N = 1000

# fracture geometry
type_fracture = 1  # 1 - KGD, 2 - radial (using a more descriptive variable name)
plotfig = 1  # 1 - plot parametric space figure, 0 - do not plot

if type_fracture == 1:

    # global solution
    l, w, p, xi, eta = get_kgd_sol(Ep, mup, Kp, Cp, Q0/H, t, N, plotfig)

    # vertex solutions
    lv, wv, pv, xiv, etav = kgd_vert_sol(Ep, mup, Kp, Cp, Q0/H, t, N)

    ind = 1  # 1 - M, 2 - Mt, 3 - K, 4 - Kt
    if ind == 1:
        col = 'blue'
    elif ind == 2:
        col = 'green'
    elif ind == 3:
        col = 'red'
    elif ind == 4:
        col = 'magenta'

    plt.figure()
    plt.plot(l*xi, w, 'k-', label='Global solution') # Added label for legend
    plt.plot(lv[ind-1]*xiv, wv[:, ind-1], '--', color=col, label=f'Vertex solution (ind={ind})') # Added label for legend and f-string formatting

    plt.xlabel('$x$ [m]')
    plt.ylabel('$w$ [m]')
    plt.legend() # Added legend to distinguish plots

    plt.figure()
    plt.plot(l*xi, p, 'k-', label='Global solution') # Added label for legend
    plt.plot(lv[ind-1]*xiv, pv[:, ind-1], '--', color=col, label=f'Vertex solution (ind={ind})') # Added label for legend and f-string formatting

    plt.xlabel('$x$ [m]')
    plt.ylabel('$p$ [Pa]')
    plt.legend() # Added legend


# if type_fracture == 2:

#     # global solution
#     R, w, p, rho, eta = get_rad_sol(Ep, mup, Kp, Cp, Q0, t, N, plotfig)

#     # vertex solutions
#     Rv, wv, pv, rhov, etav = rad_vert_sol(Ep, mup, Kp, Cp, Q0, t, N)

#     ind = 1  # 1 - M, 2 - Mt, 3 - K, 4 - Kt
#     if ind == 1:
#         col = 'blue'
#     elif ind == 2:
#         col = 'green'
#     elif ind == 3:
#         col = 'red'
#     elif ind == 4:
#         col = 'magenta'

#     plt.figure()
#     plt.plot(R*rho, w, 'k-', label='Global solution') # Added label for legend
#     plt.plot(Rv[ind-1]*rhov, wv[:, ind-1], '--', color=col, label=f'Vertex solution (ind={ind})') # Added label for legend and f-string formatting


#     plt.xlabel('$r$ [m]')
#     plt.ylabel('$w$ [m]')
#     plt.legend() # Added legend

#     plt.figure()
#     plt.plot(R*rho, p, 'k-', label='Global solution') # Added label for legend
#     plt.plot(Rv[ind-1]*rhov, pv[:, ind-1], '--', color=col, label=f'Vertex solution (ind={ind})') # Added label for legend and f-string formatting

#     plt.xlabel('$r$ [m]')
#     plt.ylabel('$p$ [Pa]')
#     plt.legend() # Added legend

plt.show()