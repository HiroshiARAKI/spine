from spine import Izhikevich
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
    weights = random.U(pre_neurons, 0, 3.0)  # U[0, 3]

    neu = Izhikevich(time=time,
                     dt=dt,
                     tau=(10, 2)  # time constants of filter
                     )

    v, u = neu.calc_v((spikes, weights))

    # Plot
    t = np.arange(0, time, dt)

    plt.figure(figsize=(7, 10))
    plt.subplot(3, 1, 1)
    plot_spike_scatter(spikes, time, dt, title='input spike trains', xlabel=None, s=1)

    plt.subplot(3, 1, 2)
    plt.plot(t, v)
    plt.ylabel('Membrane Voltage $v$ [mV]')
    plt.xlabel('time [ms]')
    plt.xlim(0, time)

    plt.subplot(3, 1, 3)
    plt.plot(t, u)
    plt.ylabel('Recovery variable $u$')
    plt.xlabel('time [ms]')
    plt.xlim(0, time)

    plt.show()

