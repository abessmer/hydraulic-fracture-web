import matplotlib.pyplot as plt

def plot_kgd_results(global_sol, vertex_sol, ind_vertex=1):
    """
    Plots the global and vertex solutions for KGD fracture.

    Args:
        global_sol (tuple): Global solution (l, w, p, xi, eta).
        vertex_sol (tuple): Vertex solutions (lv, wv, pv, xiv, etav).
        ind_vertex (int, optional): Index for vertex solution to plot (1-4). Defaults to 1.
    """
    l, w, p, xi = global_sol[0], global_sol[1], global_sol[2], global_sol[3]
    lv, wv, pv, xiv = vertex_sol[0], vertex_sol[1], vertex_sol[2], vertex_sol[3]

    if not 1 <= ind_vertex <= 4:
        raise ValueError(f"Invalid vertex index: {ind_vertex}. Must be between 1 and 4.")

    vertex_labels = {1: 'M', 2: 'Mt', 3: 'K', 4: 'Kt'}
    vertex_colors = {1: 'blue', 2: 'green', 3: 'red', 4: 'magenta'}
    col = vertex_colors[ind_vertex]
    vertex_label = vertex_labels[ind_vertex]

    # Plot fracture width
    plt.figure()
    plt.plot(l * xi, w, 'k-', label='Global solution')
    plt.plot(lv[ind_vertex - 1] * xiv, wv[:, ind_vertex - 1], '--', color=col, label=f'Vertex solution ({vertex_label})')
    plt.xlabel('$x$ [m]')
    plt.ylabel('$w$ [m]')
    plt.legend()
    plt.title('Fracture Width Comparison')

    # Plot pressure profile
    plt.figure()
    plt.plot(l * xi, p, 'k-', label='Global solution')
    plt.plot(lv[ind_vertex - 1] * xiv, pv[:, ind_vertex - 1], '--', color=col, label=f'Vertex solution ({vertex_label})')
    plt.xlabel('$x$ [m]')
    plt.ylabel('$p$ [Pa]')
    plt.legend()
    plt.title('Pressure Profile Comparison')