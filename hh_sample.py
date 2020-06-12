from spine import HodgkinHuxley

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # init experimental time and time-step
    time = 100
    dt = 0.01

    # create Hodgkin-Huxley Neuron
    neu = HodgkinHuxley(time, dt)

    # Input data (sin curve)
    input_data = np.sin(0.5 * np.arange(0, time, dt))
    input_data = np.where(input_data > 0, 20, -5) + 10 * np.random.rand(int(time/dt))
    input_data_2 = np.cos(0.3 * np.arange(0, time, dt) + 0.5)
    input_data_2 = np.where(input_data_2 > 0, 10, 0)
    input_data += input_data_2

    # calc neuron status
    v, m, n, h = neu.calc_v(input_data)

    # plot
    x = np.arange(0, time, dt)
    plt.subplot(3, 1, 1)
    plt.title('Hodgkin-Huxley Neuron model Simulation')
    plt.plot(x, input_data)
    plt.ylabel('I [μA/cm2]')

    plt.subplot(3, 1, 2)
    plt.plot(x, v)
    plt.ylabel('V [mV]')

    plt.subplot(3, 1, 3)
    plt.plot(x, n, label='n')
    plt.plot(x, m, label='m')
    plt.plot(x, h, label='h')
    plt.xlabel('time [ms]')
    plt.ylabel('Conductance param')
    plt.legend()

    plt.show()
