"""
LIF (Leaky integrate-and-fire) Neuron model
Copyright(c) HiroshiARAKI
"""
import numpy as np
import matplotlib.pyplot as plt

from .neuron import Neuron


class LIF(Neuron):
    """
    Single Exponential LIF model
    """

    def __init__(self,
                 time: int,
                 dt: float = 1.0,
                 rest=-65,
                 th=-40,
                 ref=3,
                 tc_decay=100,
                 tau=20,
                 **kwargs):
        """
        Initialize Neuron parameters
        :param time:      experimental time
        :param dt:        time step
        :param rest:      resting potential
        :param th:        threshold
        :param ref:       refractory period
        :param tc_decay:  time constance
        :param tau:       single exponential decay
        """
        super().__init__(time, dt)
        self.rest = kwargs.get('rest', rest)
        self.th = kwargs.get('th', th)
        self.ref = kwargs.get('ref', ref)
        self.tc_decay = kwargs.get('tc_decay', tc_decay)
        self.tau = kwargs.get('tau', tau)
        self.monitor = {}

    def calc_v(self, data):
        """
        Calculate Membrane Voltage
        :param data: tuple(spikes[], weight[])
        :return:
        """
        spikes = np.array(data[0])
        weights = np.array(data[1])
        data = [
            spikes[i] * weights[i]
            for i in range(weights.size)
        ]
        time = int(self.time / self.dt)

        data = np.sum(data, 0)
        data = np.convolve(data, self.kernel(np.arange(0, self.time)), 'same')[:time]
        # plt.plot(data)
        # plt.show()
        # exit()

        # initialize
        f_last = 0  # last firing time
        vpeak = 20  # the peak of membrane voltage
        spikes = np.zeros(time)
        v = self.rest  # set to resting voltage

        v_monitor = []  # monitor voltage

        # Core of LIF
        for t in range(time):
            dv = ((self.dt * t) > (f_last + self.ref)) * (-v + self.rest + data[t]) / self.tc_decay
            v = v + self.dt * dv  # calc voltage

            f_last = f_last + (self.dt * t - f_last) * (v >= self.th)  # if fires, memory the firing time
            v = v + (vpeak - v) * (v >= self.th)  # set to peak

            v_monitor.append(v)

            spikes[t] = (v >= self.th) * 1  # set to spike

            v = v + (self.rest - v) * (v >= self.th)  # return to resting voltage

        self.monitor['s'] = spikes
        self.monitor['v'] = v_monitor
        self.monitor['f'] = np.arange(0, self.time, self.dt)[v >= self.th],  # real firing times

        return v_monitor, spikes, self.monitor['f']

    def kernel(self, t):
        """ Kernel: single exponential synaptic filter """
        row_k = np.exp(-t/self.tau)
        v0 = 1. / np.max(row_k)
        return v0 * row_k

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


class DLIF(LIF):

    def __init__(self,
                 time: int,
                 dt: float = 1.0,
                 rest=-65,
                 th=-40,
                 ref=3,
                 tc_decay=100,
                 tau_1: float = 10,
                 tau_2: float = 2.5,
                 **kwargs):
        """

        :param time:
        :param dt:
        :param rest:
        :param th:
        :param ref:
        :param tc_decay:
        :param tau_1:
        :param tau_2:
        :param kwargs:
        """
        super().__init__(time, dt, rest, th, ref, tc_decay, **kwargs)
        self.tau_1 = tau_1
        self.tau_2 = tau_2
        self.monitor = {}

    def calc_v(self, data):
        """
        Calculate Membrane Voltage
        :param data: tuple(spikes[], weight[])
        :return membrane voltage, output spikes, firing times:
        """
        spikes = np.array(data[0])
        weights = np.array(data[1])

        peak = 20  # the peak of membrane voltage
        f_last = -100  # last firing time
        t_ref = int(self.ref / self.dt)  # refractory period [x dt ms]

        v = np.zeros(int(self.time / self.dt)) + self.rest  # all membrane voltage set to resting vol.

        input_spikes = np.array([
            spikes[i] * weights[i]
            for i in range(weights.size)
        ])
        input_spikes = np.sum(input_spikes, 0)
        for t, s in enumerate(input_spikes):
            if s:  # if fires,
                # and be not in refractory period, calculate voltage
                v[t:] += (t > (f_last + t_ref)) * s * self.kernel(np.arange(0, v[t:].size, 1) * self.dt)

            if v[t] >= self.th:
                v[t] = peak
                v[t+1:] = self.rest  # return to resting voltage
                f_last = t  # memory the firing time

        self.monitor = {
            'v': v,
            's': [v >= self.th],  # boolean spike trains
            'f': np.arange(0, self.time, self.dt)[v >= self.th],  # real firing times
        }

        return v, self.monitor['s'], self.monitor['f']

    def kernel(self, t):
        """ Kernel: double exponential synaptic filter """
        row_k = np.exp(-t/self.tau_1) - np.exp(-t/self.tau_2)
        v0 = 1. / np.max(row_k)

        return v0 * row_k

