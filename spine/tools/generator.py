import numpy as np
import matplotlib.pyplot as plt


class PoissonSpike:
    def __init__(self, data, time=500, dt=0.1, max_freq=128, min_freq=0):
        """
        Generate Poisson spike trains
        :param data:
        :param time:
        :param dt:
        :param max_freq:
        :param min_freq
        """
        data = np.array(data).reshape(-1)
        self.data = (data - np.min(data.min())) / (np.max(data) - np.min(data)) if data.size != 1 else data
        self.time = time
        self.dt = dt

        self.max_freq = max_freq
        self.freq_data = self.data * (max_freq - min_freq) + min_freq
        self.norm_data = 1000. / (self.freq_data + 1e-10)

        fires = [
            np.cumsum(np.random.poisson(cell / dt, (int(time / cell + 1)))) * dt
            for cell in self.norm_data
        ]
        self.fires = np.array(fires, dtype=object)

        self.spikes = np.zeros((data.shape[0], int(time/dt)))

        for s, f in zip(self.spikes, self.fires):
            f = f[f < time]  # round
            s[np.array(f/dt, dtype=int)] = 1    # {0,1} spikes

        self.monitor = {
            's': self.spikes,
            'f': self.fires,
        }

    def plot_spikes(self):
        """
        Plot spike trains as a Raster plot
        :return:
        """
        plt.title('Spike firing timing')
        for i, s in enumerate(self.fires):
            plt.scatter(s, [i for _ in range(len(s))], s=1.0, c='tab:blue')
        plt.xlim(0, self.time)
        plt.ylabel('pixel index')
        plt.xlabel('time [ms]')