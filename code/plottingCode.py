%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import nash
import sympy as sym
sym.init_printing()

def plot_matrix_pair(A, B, subplot_base=121, norm_max=1, norm_min=-1, 
                     colour='grey', plot_poly=True, cfill=False, 
                     save_str="", offset_watermark=False):
    '''Plots a game A vs B to the screen. Polytope Vertacies: 0:cyan, 1:magenta, 2:black, 3:blue'''
    # Create [0,1]^2 plane:
    x_range, y_range = [np.arange(0, 1.1, 0.01)] * 2
    x_grid, y_grid = np.meshgrid(x_range, y_range)
    polytope_eqns = get_polytope_vertex_eqns(A,B)
    game = nash.Game(A, B)
    eqlbria = list(game.support_enumeration())
    num_eqs = len(eqlbria)
    
    # Build the Data for row player:
    row_Z = get_utility_plane(x_grid, y_grid, A)
    # Build the Data for col player:
    col_Z = get_utility_plane(x_grid, y_grid, B)
    #PLOTS
    plt.rcParams['axes.facecolor'] = colour
    #Row: P = {x \in R | x>=0, xB<=1}
    plt.subplot(subplot_base)
    if cfill:
        plt.contourf(x_grid, y_grid, row_Z, 15, cmap='RdYlGn') # Norm is for the coloured lines
    else:
        plt.contour(x_grid, y_grid, row_Z, cmap='RdYlGn', norm=mpl.colors.Normalize(vmin=norm_min, vmax=norm_max)) # Norm is for the coloured lines
    if plot_poly:
        plt.plot(x_range,[1,1]+[0]*(len(x_range)-2),'c-',x_range,[0.01]*len(x_range),'m-')
        plt.plot(x_range,polytope_eqns[2](x_range),'k-',x_range,polytope_eqns[3](x_range),'b-')
    plt.colorbar()
    eqs = ",".join(["{:.1f}".format(eqlbria[n][0][0]) for n in range(num_eqs)])
    plt.title("$u_r$ plane | eq@$x="+eqs+"$")
    plt.xlabel("$x$ for $\sigma_r=(x,1-x)$")
    plt.ylabel("$y$ for $\sigma_c=(y,1-y)$")
    plt.xlim(0,1)
    plt.ylim(0,1)
    if offset_watermark:
        plt.text(0.66, 0.66,'$u_r$', horizontalalignment='center',verticalalignment='center', color='grey', fontsize=40, alpha=0.4)
    else:
        plt.text(0.5, 0.5,'$u_r$', horizontalalignment='center',verticalalignment='center', color='grey', fontsize=40, alpha=0.4)
    
    #Col: Q = {y \in R | Ay<=1, y>=0}
    plt.subplot(subplot_base+1)
    if cfill:
        plt.contourf(x_grid, y_grid, col_Z, 15, cmap='RdYlGn') # Norm is for the coloured lines
    else:
        plt.contour(x_grid, y_grid, col_Z, cmap='RdYlGn', norm=mpl.colors.Normalize(vmin=norm_min, vmax=norm_max)) # Norm is for the coloured lines
    if plot_poly:
        plt.plot(x_range,[1,1]+[0]*(len(x_range)-2),'k-',x_range,[0.01]*len(x_range),'b-')
        plt.plot(x_range,polytope_eqns[0](x_range),'c-',x_range,polytope_eqns[1](x_range),'m-')
    plt.colorbar()
    eqs = ",".join(["{:.1f}".format(eqlbria[n][1][0]) for n in range(num_eqs)])
    plt.title("$u_c$ plane | eq@$y="+eqs+"$")
    plt.xlabel("$x$ for $\sigma_r=(x,1-x)$")
    plt.ylabel("$y$ for $\sigma_c=(y,1-y)$")
    plt.xlim(0,1)
    plt.ylim(0,1)
    if offset_watermark:
        plt.text(0.66, 0.66,'$u_c$', horizontalalignment='center',verticalalignment='center', color='grey', fontsize=40, alpha=0.4)
    else:
        plt.text(0.5, 0.5,'$u_c$', horizontalalignment='center',verticalalignment='center', color='grey', fontsize=40, alpha=0.4)
     
    plt.tight_layout()
    if not save_str == "":
        plt.savefig("img/"+save_str)