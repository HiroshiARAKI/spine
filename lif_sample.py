from spine import LIF
from spine.tools import PoissonSpike, plot_spike_scatter, random

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    time = 500  # ms
    dt = 0.5  # time step

    pre_neurons = 100

    # Input data from Poisson Spike Gen.
    spikes = PoissonSpike(np.random.random(pre_neurons),
                          time=time,
                          dt=dt).spikes

    # random weights whose size is the same as spikes
    weights = random.U(pre_neurons, -0.05, 0.1)  # U[-0.05, 0.1]

    neu = LIF(time=time,
              dt=dt,
              tau=(10, 2)  # time constants of filter
              )

    v, s, f = neu.calc_v((spikes, weights))

    # Plot
    t = np.arange(0, time, dt)

    plt.subplot(2, 1, 1)
    plot_spike_scatter(spikes, time, dt, title='input spike trains', xlabel=None)

    plt.subplot(2, 1, 2)
    plt.plot(t, v)
    plt.plot(t, np.full_like(t, neu.th), linestyle='dashed')
    plt.ylabel('Membrane Voltage [mV]')
    plt.xlabel('time [ms]')
    plt.xlim(0, time)

    plt.show()

