#!/usr/local/bin/python3.5

"""
Program: efields.py
This program is a skeleton for plotting electric fields. It works by
superimposing point charges to create a discrete distribution which can be taken
as continuous in the limit that the distance between charges is small.
Several functions show how this can be done to create some typical distributions.
All of the sample distributions will be saved as a pdf file in the working
directory.
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def mkcharge(ax, ay, q, x, y):
    """
    Function: mkcharge()
    This function creates a point charge of magnitude q at position (ax,ay).
    """
    Ex = q*(x-ax) / ((x-ax)**2 + (y-ay)**2)**(1.5)
    Ey = q*(y-ay) / ((x-ax)**2 + (y-ay)**2)**(1.5)
    if q > 0:
        ch_point = Circle((ax,ay), q*0.03, color='b', alpha=0.6)
    else:
        ch_point = Circle((ax,ay), q*0.03, color='r', alpha=0.6)
    lout = [Ex, Ey, ch_point]
    # get current axis and add cirle to plot
    plt.gcf().gca().add_artist(ch_point)
    return lout


def boxes():
    plt.figure(figsize=(10, 7))
    x = np.linspace(-2, 2, 32)
    y = np.linspace(-1.5, 1.5, 24)
    x, y = np.meshgrid(x, y)
    # Make as many charges as you want
    E1 = mkcharge(-1, -1, -1, x, y)
    E2 = mkcharge(-1, 1, 1, x, y)
    E3 = mkcharge(1, 1, -1, x, y)
    E4 = mkcharge(1, -1, 1, x, y)
    E5 = mkcharge(-0.5, -0.5, -1, x, y)
    E6 = mkcharge(-0.5, 0.5, 1, x, y)
    E7 = mkcharge(0.5, 0.5, -1, x, y)
    E8 = mkcharge(0.5, -0.5, 1, x, y)
    # Superposition to get total field
    Ex = E1[0] + E2[0] + E3[0] + E4[0] + E5[0] + E6[0] + E7[0] + E8[0]
    Ey = E1[1] + E2[1] + E3[1] + E4[1] + E5[1] + E6[1] + E7[1] + E8[1]
    #streamplot(x, y, Ex/sqrt(Ex**2+Ey**2), Ey/sqrt(Ex**2+Ey**2), color='k', density=0.6)
    plt.quiver(x, y, Ex/sqrt(Ex**2+Ey**2), Ey/sqrt(Ex**2+Ey**2), pivot='middle', headwidth=2, headlength=3)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.show()


def dipole(a):
    """Function: dipole()
    Plot the electric field lines of two point charges seperated by a distance 2*a"""
    plt.figure(figsize=(20, 14))
    xlim = (a+2); ylim = (a+2)
    plt.axes = plt.gca()
    plt.axes.set_xlim([-xlim,xlim])
    plt.axes.set_ylim([-ylim,ylim])
    x = np.linspace(-xlim, xlim, 60)
    y = np.linspace(-ylim, ylim, 60)
    x, y = np.meshgrid(x, y)
    E1 = mkcharge(0, a, 1, x, y)
    E2 = mkcharge(0, -a, -1, x, y)
    Ex = E1[0] + E2[0]
    Ey = E1[1] + E2[1]
    color = np.log(np.sqrt(np.abs(Ex) + np.abs(Ey)))
    plt.streamplot(x, y, Ex/np.sqrt(Ex**2+Ey**2), Ey/np.sqrt(Ex**2+Ey**2), color=color, linewidth=1, cmap=plt.cm.inferno, density=2, arrowstyle='->', arrowsize=1.5)
    #color = u + v
    #streamplot(x, y, Ex/sqrt(Ex**2+Ey**2), Ey/sqrt(Ex**2+Ey**2), color=color, linewidth=1, cmap=plt.cm.seismic, density=2, arrowstyle='->', arrowsize=1.5)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.savefig('electric_dipole.pdf', transparent=True, bbox_inches='tight', pad_inches=0)


def capacitor(a):
    plt.figure(figsize=(20, 14), dpi=80)
    xlim = (a+2); ylim = (a+2)
    plt.axes = plt.gca()
    plt.axes.set_xlim([-xlim,xlim])
    plt.axes.set_ylim([-ylim,ylim])
    x = np.linspace(-xlim, xlim, 60)
    y = np.linspace(-ylim, ylim, 60)
    x, y = np.meshgrid(x, y)
    Lx = []
    Ly = []
    Ex = 0
    Ey = 0
    for m in range(-30,30):
        EFt = mkcharge(0.015*m, a, -1, x, y)
        Lx.append(EFt[0])
        Ly.append(EFt[1])
    for n in range(-30,30):
        EFb = mkcharge(0.015*n, -a, 1, x, y)
        Lx.append(EFb[0])
        Ly.append(EFb[1])
    for xelem in Lx:
        Ex += xelem
    for yelem in Ly:
        Ey += yelem
    color = np.log(np.sqrt(np.abs(Ex) + np.abs(Ey)))
    plt.streamplot(x, y, Ex/np.sqrt(Ex**2+Ey**2), Ey/np.sqrt(Ex**2+Ey**2), color=color, linewidth=1, cmap=plt.cm.inferno, density=2, arrowstyle='->', arrowsize=1.5)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.savefig('capacitor.pdf', transparent=True, bbox_inches='tight', pad_inches=0)


def planes(r, theta):
    """Function: Planes(r, theta)
    Plot two intersecting planes using n point charges superimposed, where the planes have length
    2*r and are separated by an angle theta (in degrees)."""
    plt.figure(figsize=(20, 14))
    n=30
    d = 0.03
    xlim = n*d*r + 1; ylim = n*d*r +1
    plt.axes = plt.gca()
    plt.axes.set_xlim([-xlim,xlim])
    plt.axes.set_ylim([-ylim,ylim])
    x = np.linspace(-xlim, xlim, 100)
    y = np.linspace(-ylim, ylim, 100)
    x, y = np.meshgrid(x, y)
    lboxx = []
    lboxy = []
    Ex = 0
    Ey = 0
    trad = theta*np.pi/180
    a = 0
    b = 0
    c = 0
    for l in range(1,n+1):
        a += d*r*np.cos(trad)
        b += d*r*np.sin(trad)
        c += d*r
        E1 = mkcharge( -c, 0, 1, x, y)
        E2 = mkcharge( c, 0, 1, x, y)
        E3 = mkcharge( a, b, -1, x, y)
        E4 = mkcharge( -a, -b, -1, x, y)
        lboxx.append(E1[0])
        lboxx.append(E2[0])
        lboxx.append(E3[0])
        lboxx.append(E4[0])
        lboxy.append(E1[1])
        lboxy.append(E2[1])
        lboxy.append(E3[1])
        lboxy.append(E4[1])
    for xelem in lboxx:
        Ex += xelem
    for yelem in lboxy:
        Ey += yelem
    color = np.log(np.sqrt(np.abs(Ex) + np.abs(Ey)))
    plt.streamplot(x, y, Ex/np.sqrt(Ex**2+Ey**2), Ey/np.sqrt(Ex**2+Ey**2), color=color, linewidth=1, cmap=plt.cm.inferno, density=2, arrowstyle='->', arrowsize=1.5)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.savefig('electric_planes.pdf', transparent=True, bbox_inches='tight', pad_inches=0)


def quadrupole(a):
    """Function: quadrupole(a)
    Plot the electric field lines of two antiparallel dipoles were the horizontal and vertical
    distance between charges is 2*a."""
    plt.figure(figsize=(20, 14))
    xlim = (a+5); ylim = (a+5)
    plt.axes = plt.gca()
    plt.axes.set_xlim([-xlim,xlim])
    plt.axes.set_ylim([-ylim,ylim])
    x = np.linspace(-xlim, xlim, 100)
    y = np.linspace(-ylim, ylim, 100)
    x, y = np.meshgrid(x, y)
    E1 = mkcharge(a, a, 1, x, y)
    E2 = mkcharge(a, -a, -1, x, y)
    E3 = mkcharge(-a, a, -1, x, y)
    E4 = mkcharge(-a, -a, +1, x, y)
    Ex = E1[0] + E2[0] + E3[0] + E4[0]
    Ey = E1[1] + E2[1] + E3[1] + E4[1]
    color = np.log(np.sqrt(Ex**2 + Ey**2))
    #streamplot(x, y, Ex/sqrt(Ex**2+Ey**2), Ey/sqrt(Ex**2+Ey**2), color=color, linewidth=1, cmap=plt.cm.inferno, density=3.5, minlength=0.11, arrowstyle='->', arrowsize=1.5)
    plt.streamplot(x, y, Ex/np.sqrt(Ex**2+Ey**2), Ey/np.sqrt(Ex**2+Ey**2), color=color, linewidth=1, cmap=plt.cm.inferno, density=3.5, arrowstyle='->', arrowsize=1.5)
    #color = u + v
    #streamplot(x, y, Ex/sqrt(Ex**2+Ey**2), Ey/sqrt(Ex**2+Ey**2), color=color, linewidth=1, cmap=plt.cm.seismic, density=2, arrowstyle='->', arrowsize=1.5)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.savefig('electric_quadrupole.pdf', transparent=True, bbox_inches='tight', pad_inches=0)


def octupole(a):
    """Function: octupole(a)"""
    plt.figure(figsize=(20, 14))
    xlim = (a+5); ylim = (a+5)
    plt.axes = plt.gca()
    plt.axes.set_xlim([-xlim,xlim])
    plt.axes.set_ylim([-ylim,ylim])
    x = np.linspace(-xlim, xlim, 100)
    y = np.linspace(-ylim, ylim, 100)
    x, y = np.meshgrid(x, y)
    # RR
    E1 = mkcharge(a+2*a, a, -1, x, y)
    E2 = mkcharge(a+2*a, -a, 1, x, y)
    # R
    E5 = mkcharge(a, a, 1, x, y)
    E6 = mkcharge(a, -a, -1, x, y)
    # L
    E7 = mkcharge(-a, a, -1, x, y)
    E8 = mkcharge(-a, -a, 1, x, y)
    # LL
    E3 = mkcharge(-(a+2*a), a, 1, x, y)
    E4 = mkcharge(-(a+2*a), -a, -1, x, y)
    Ex = E1[0] + E2[0] + E3[0] + E4[0] + E5[0] + E6[0] + E7[0] + E8[0]
    Ey = E1[1] + E2[1] + E3[1] + E4[1] + E5[1] + E6[1] + E7[1] + E8[1]
    #color = log(sqrt(abs(Ex) + abs(Ey)+2))
    color = np.log(np.sqrt(Ex**2 + Ey**2))
    plt.streamplot(x, y, Ex/np.sqrt(Ex**2+Ey**2), Ey/np.sqrt(Ex**2+Ey**2), color=color, linewidth=1, cmap=plt.cm.inferno, density=3.5, arrowstyle='->', arrowsize=1.5)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.savefig('electric_octupole.pdf', transparent=True, bbox_inches='tight', pad_inches=0)


def demo():
    """
    Function: demo()
    This function computes and plots 5 distributions.
    WARNING - This takes some time to run! It's slow!
    """
    dipole(0.5)
    quadrupole(1)
    octupole(1)
    capacitor(0.5)
    planes(1,75)

# note: add any functions at this point which you wish to run with the program,
# otherwise import efields into the python console and run functions as desired
