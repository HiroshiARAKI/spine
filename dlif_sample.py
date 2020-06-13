from spine import DLIF, PoissonSpike, plot_spike_scatter

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    duration = 500  # ms
    dt = 0.1  # time step
    time = int(duration / dt)

    # create DLIF instance
    neu = DLIF(duration, dt)

    # random spike trains
    spikes = PoissonSpike(np.random.random(10),
                          time=duration,
                          dt=dt).spikes

    # random weights whose size is the same as spikes
    weights = np.random.random(10) + 2.0

    # calc voltage and get results
    # v: membrane voltage
    # s: output spike as boolean list
    # f: firing times
    v, s, f = neu.calc_v((spikes, weights))

    # plotting
    plt.subplot(2, 1, 1)
    plot_spike_scatter(spikes, duration, dt, title='input spike trains', xlabel=None)

    t = np.arange(0, duration, dt)
    plt.subplot(2, 1, 2)
    plt.plot(t, v)
    plt.plot(t, np.full_like(t, neu.th), linestyle='dashed')
    plt.xlim(0, duration)
    plt.xlabel('time [ms]')
    plt.ylabel('Membrane Voltage [mV]')

    plt.show()
