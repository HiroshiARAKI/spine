"""
Spike Generator based on Poisson Distribution.
Copyright(c) HiroshiARAKI
"""
import numpy as np
import matplotlib.pyplot as plt


class PoissonSpike:
    def __init__(self, data, time=300, dt=0.1, max_freq=128):
        """
        Generate Poisson spike trains
        :param data:
        :param time:
        :param dt:
        :param max_freq:
        """
        self.data = np.array(data).reshape(-1)
        self.time = time
        self.dt = dt

        self.max_freq = max_freq
        self.freq_data = self.data * max_freq
        self.norm_data = 1000. / self.freq_data

        spikes = [
            np.cumsum(np.random.poisson(cell, (int(self.time / cell + 1))))
            for cell in self.norm_data
        ]
        self.spikes = np.array(spikes)

    def plot_spikes(self):
        """
        Plot spike trains as a Raster plot
        :return:
        """
        plt.title('Spike firing timing')
        for i, s in enumerate(self.spikes):
            plt.scatter(s, [i for _ in range(len(s))], s=1.0, c='tab:blue')
        plt.xlim(0, self.time)
        plt.ylabel('pixel index')
        plt.xlabel('time [ms]')


if __name__ == '__main__':
    ps = PoissonSpike(np.random.random((10, 10)))
    ps.plot_spikes()
    plt.show()
