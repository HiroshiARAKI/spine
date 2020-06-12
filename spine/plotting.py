import matplotlib.pyplot as plt
import numpy as np


def plot_spike_scatter(spikes, time, dt, **kwargs):
    """
    Plot spike trains as the scatter by {0,1} spike trains.
    :param spikes:
    :param time:
    :param dt:
    :return:
    """
    t = np.arange(0, time, dt)

    firing_times = [
        t[spike == 1]
        for spike in spikes
    ]

    for i in range(len(spikes)):
        plt.scatter(firing_times[i],
                    [i for _ in firing_times[i]],
                    s=kwargs.get('s', 10),
                    c=kwargs.get('c', 'tab:blue'))
    plt.xlim(0, time)
    plt.yticks([i for i in range(len(firing_times))])

    if kwargs.get('xlabel', '') is not None:
        plt.xlabel('time [ms]')

    if kwargs.get('ylabel', '') is not None:
        plt.ylabel('neuron index')

    if kwargs.get('title') is not None:
        plt.title(kwargs.get('title', ''))
