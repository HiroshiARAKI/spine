from spine import FitzHughNagumo

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # init experimental time and time-step
    time = 100
    dt = 0.1

    # create Hodgkin-Huxley Neuron
    neu = FitzHughNagumo(time, dt)

    # Input data (sin curve)
    input_data = np.sin(0.2 * np.arange(0, time, dt))
    input_data = np.where(input_data > 0, 0.8, 0.1)

    v, u = neu.calc_v(input_data)

    # plot
    x = np.arange(0, time, dt)
    plt.subplot(2, 1, 1)
    plt.title('FitzHugh-Nagumo Neuron model Simulation')
    plt.plot(x, input_data)
    plt.ylabel('input')

    plt.subplot(2, 1, 2)
    plt.plot(x, v, label='v: recovery variable')
    plt.plot(x, u, label='u: membrane potential')
    plt.xlabel('time [ms]')

    plt.legend()
    plt.show()
