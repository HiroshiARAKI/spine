from spine import LIF, PoissonSpike
from spine.tools.plotting import plot_spike_scatter

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    duration = 500  # ms
    dt = 0.1  # time step

    time = int(duration / dt)

    # Input data from Poisson Spike Gen.
    spikes = PoissonSpike(np.random.random(10),
                          time=duration,
                          dt=dt).spikes

    # random weights whose size is the same as spikes
    weights = np.random.random(10) + 5.0

    neu = LIF(duration,
              dt,
              k='double',  # use double exponential filter
              tau=(10, 2)  # time constants of filter
              )

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

