from spine import LIF

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    duration = 500  # ms
    dt = 0.1  # time step

    time = int(duration / dt)

    # Input data
    input_data_1 = 10 * np.sin(0.1 * np.arange(0, duration, dt)) + 50
    input_data_2 = -10 * np.cos(0.05 * np.arange(0, duration, dt)) - 10

    # 足し合わせ
    input_data = input_data_1 + input_data_2

    neu = LIF(duration, dt)
    spikes, voltage = neu.calc_v(input_data)

    # Plot
    plt.subplot(2, 2, 1)
    plt.ylabel('Input 1')
    plt.plot(np.arange(0, duration, dt), input_data_1)

    plt.subplot(2, 2, 2)
    plt.ylabel('Input 2')
    plt.plot(np.arange(0, duration, dt), input_data_2)

    plt.subplot(2, 2, 3)
    plt.ylabel('Membrane Voltage')
    plt.xlabel('time [ms]')
    plt.plot(np.arange(0, duration, dt), voltage)

    plt.subplot(2, 2, 4)
    plt.ylabel('Output')
    plt.xlabel('time [ms]')
    plt.plot(np.arange(0, duration, dt), spikes)
    plt.show()
