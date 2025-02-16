import matplotlib.pyplot as plt
import numpy as np

def plot_phase_diagram(tau_val, Km_val):
    """
    Plots a phase diagram and highlights a specific point (tau, Km) on it.

    Args:
        tau_val (float or array-like): The value(s) of tau to plot.
        Km_val (float or array-like): The value(s) of Km to plot.

    Returns:
        None (displays the plot)
    """
    # axis limits
    taumin = -30
    taumax = 25
    Kmin = -2.5
    Kmax = 3

    # boundaries
    tmmt0 = 1.21e-13
    tmmt1 = 2.36e6

    Kmk0 = 0.70
    Kmk1 = 4.80

    tkkt0 = 1.25e-14
    tkkt1 = 1.76e5

    Kmtkt0 = 0.90
    Kmtkt1 = 4.80

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # plot edge limits
    ax.plot(np.log10([tmmt0, tmmt0, 10**taumin]), np.log10([10**Kmin, Kmk0, Kmk0]), 1e5*np.ones(3), 'b-')  # M
    ax.plot(np.log10([tmmt1, tmmt1, 10**taumax]), np.log10([10**Kmin, Kmtkt0, Kmtkt0]), 1e5*np.ones(3), 'g-')  # Mt
    ax.plot(np.log10([10**taumin, tkkt0*Kmk1**(4), tkkt0*1e2**(4)]), np.log10([Kmk1, Kmk1, 10**Kmax]), 1e5*np.ones(3), 'r-')  # K
    ax.plot(np.log10([10**taumax, tkkt1*Kmtkt1**(4), tkkt1*1e2**(4)]), np.log10([Kmtkt1, Kmtkt1, 10**Kmax]), 1e5*np.ones(3), 'm-')  # Kt

    # add labels
    ax.text(-23.5, -1.35, 1e5, r'$M$', fontsize=30)
    ax.text(-20.5, 1.85, 1e5, r'$K$', fontsize=30)
    ax.text(14, -1.35, 1e5, r'$\tilde M$', fontsize=30)
    ax.text(15.5, 1.7, 1e5, r'$\tilde K$', fontsize=30)

    ax.set_title(r'$\tau=$' + f'{tau_val:.3g}' + r' $K_m=$' + f'{Km_val:.3g}')

    # show the location on the phase diagram
    tau = np.array([tau_val]) # Ensure tau is array-like
    Km = np.array([Km_val])   # Ensure Km is array-like

    tau = np.clip(tau, 10**taumin, 10**taumax)
    Km = np.clip(Km, 10**Kmin, 10**Kmax)

    ax.plot(np.log10(tau), np.log10(Km), 1e5*np.ones_like(tau), marker='o', linestyle='none', color='black', markerfacecolor='black')

    ax.set_xlabel(r'$\log_{10}(\tau)$')
    ax.set_ylabel(r'$\log_{10}(K_m)$')

    ax.set_xlim([taumin, taumax])
    ax.set_ylim([Kmin, Kmax])

    ax.view_init(elev=90, azim=0)

    plt.show()

if __name__ == '__main__':
    # Example usage:
    tau_example = 1e-10
    Km_example = 1
    plot_phase_diagram(tau_example, Km_example)

    tau_example_array = [1e-10, 1e-9] # Example with array inputs
    Km_example_array = [1, 2]
    plot_phase_diagram(tau_example_array, Km_example_array)