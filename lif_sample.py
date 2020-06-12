from spine import LIF, plot_spike_scatter

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    duration = 500  # ms
    dt = 0.1  # time step

    time = int(duration / dt)

    # Input data
    spikes = [np.where(np.random.random(time) > 0.996, 1, 0)
              for _ in range(10)]
    spikes = np.array(spikes)

    # random weights whose size is the same as spikes
    weights = np.random.random(10) + 5.0

    neu = LIF(duration, dt)
    v, s, f = neu.calc_v((spikes, weights))

    # Plot
    t = np.arange(0, duration, dt)

    plt.subplot(2, 1, 1)
    plot_spike_scatter(spikes, duration, dt, title='input spike trains', xlabel=None)

    plt.subplot(2, 1, 2)
    plt.plot(t, v)
    plt.plot(t, np.full_like(t, neu.th), linestyle='dashed')
    plt.ylabel('Membrane Voltage [mV]')
    plt.xlabel('time [ms]')
    plt.xlim(0, duration)

    plt.show()

