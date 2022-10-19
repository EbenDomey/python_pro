import numpy as np
import matplotlib.pyplot as plt


def density(tf_1, tf_2, tf_c):
    tf = np.arange(tf_1, tf_2, tf_c)
    tc = (5 / 9) * (tf - 32)
    rho = (
        (5.5289 * 10**-8 * tc)
        - (8.5016 * 10**-6 * tc * 2)
        + (6.5622 * 10**-5 * tc)
        + 0.99987
    )
    plt.figure(figsize=[10, 5])
    plt.plot(tc, rho, marker="x")
    plt.xlabel("Temperature($^0C$)")
    plt.ylabel("Density($g/cm^3$)")
    plt.title("Density vrs Temperature")
    plt.grid()
    return plt.show()


density(32, 93.2, 3.6)
