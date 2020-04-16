"""
LIF (Leaky integrate-and-fire) Neuron model
Copyright(c) HiroshiARAKI
"""
import numpy as np
import matplotlib.pyplot as plt


class LIF:
    def __init__(self, time: int, dt: float = 1.0, rest=-65, th=-40, ref=3, tc_decay=100):
        """
        Initialize Neuron parameters
        :param time:      experimental time
        :param dt:        time step
        :param rest:      resting potential
        :param th:        threshold
        :param ref:       refractory period
        :param tc_decay:  time constance
        """
        self.time = time
        self.dt = dt
        self.rest = rest
        self.th = th
        self.ref = ref
        self.tc_decay = tc_decay
        self.monitor = {}

    def calc_v(self, i):
        """ simple LIF neuron """
        time = int(self.time / self.dt)

        # initialize
        tlast = 0  # 最後に発火した時刻
        vpeak = 20  # 膜電位のピーク(最大値)
        spikes = np.zeros(time)
        v = self.rest  # 静止膜電位

        v_monitor = []  # monitor voltage

        # Core of LIF
        for t in range(time):
            dv = ((dt * t) > (tlast + self.ref)) * (-v + self.rest + i[t]) / self.tc_decay  # 微小膜電位増加量
            v = v + dt * dv  # 膜電位を計算

            tlast = tlast + (dt * t - tlast) * (v >= self.th)  # 発火したら発火時刻を記録
            v = v + (vpeak - v) * (v >= self.th)  # 発火したら膜電位をピークへ

            v_monitor.append(v)

            spikes[t] = (v >= self.th) * 1  # スパイクをセット

            v = v + (self.rest - v) * (v >= self.th)  # 静止膜電位に戻す

        self.monitor['s'] = spikes
        self.monitor['v'] = v_monitor

        return spikes, v_monitor

    def plot_v(self, save=False, filename='lif.png', **kwargs):
        """
        plot membrane potential
        :param save:
        :param filename:
        :param kwargs:
        :return:
        """
        x = np.arange(0, self.time, self.dt)
        plt.title('LIF Neuron model Simulation')
        plt.plot(x, self.monitor['v'])
        plt.ylabel('V [mV]')
        plt.xlabel('time [ms]')
        if not save:
            plt.show()
        else:
            plt.savefig(filename, dpi=kwargs.get('dpi', 150))
        plt.close()


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
