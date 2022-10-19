import matplotlib.pyplot as plt
import numpy as np
import math as mt  # the math library to use to get "e" into the formula for k

# i created this function so that my code wouldn't look too long when u are setting the labels and stuff
def set_prop(ax, XString, YString, Title):
    ax.set_xlabel(XString)
    ax.set_ylabel(YString)
    ax.set_title(Title)
    ax.grid()


def reaction_rate(Tf, Tl, Ts=1):
    A = 7 * (10**16)
    E = 1 * (10**5)
    R = 8.314
    t_abs = np.arange(Tf, Tl, Ts)
    f = -E / (R * t_abs)
    k = (
        A * mt.e**f
    )  # the mt here is representing the math library I declared at the very top of the script. the mt produces the "e" value
    c = 1 / t_abs

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.plot(t_abs, k, color="green")
    plt.semilogy(c, k, color="red")

    set_prop(ax1, r"T$\alpha$", "k", r"k versus T$\alpha$")
    set_prop(ax2, r"1/T$\alpha$", "log(k)", r"log(k) versus 1/T$\alpha$")
    return plt.show()


reaction_rate(253, 325)
