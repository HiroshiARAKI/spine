"""
LIF (Leaky integrate-and-fire) Neuron model
Copyright(c) HiroshiARAKI
"""
import numpy as np
import matplotlib.pyplot as plt

from .neuron import Neuron
from ..tools import kernel


class LIF(Neuron):
    """
    LIF: leaky integrate-and-fire model
    """

    def __init__(self,
                 time: int,
                 dt: float = 1.0,
                 rest=-65,
                 th=-40,
                 ref=3,
                 tc_decay=100,
                 k='single',
                 tau: tuple = (20, ),
                 **kwargs):
        """
        Initialize Neuron parameters
        :param time:      experimental time
        :param dt:        time step
        :param rest:      resting potential
        :param th:        threshold
        :param ref:       refractory period
        :param tc_decay:  time constance
        :param k:         kernel {'single', 'double'}
        :param tau:       exponential decays as tuple(tau_1 ,tau_2) or float
        """
        super().__init__(time, dt)

        if k not in ['single', 'double']:
            print('The kernel is selected "single".')
            k = 'single'

        self.rest = kwargs.get('rest', rest)
        self.th = kwargs.get('th', th)
        self.ref = kwargs.get('ref', ref)
        self.tc_decay = kwargs.get('tc_decay', tc_decay)
        self.monitor = {}

        self.kernel = kernel[kwargs.get('k', k)]  # default: single exp filter
        self.tau = tau if type(tau) is tuple else (tau, )

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
        data = np.convolve(data,
                           self.kernel(np.arange(0, self.time, self.dt),
                                       self.tau)
                           )[0:time]

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


class IF(LIF):
    """
    IF: integrate-and-fire model
    """
    def __init__(self,
                 time: int,
                 dt: float = 1.0,
                 rest=-65,
                 th=-40,
                 ref=3,
                 k='single',
                 tau: tuple = (20, ),
                 **kwargs):
        """
        Initialize Neuron parameters
        :param time:
        :param dt:
        :param rest:
        :param th:
        :param ref:
        :param k:
        :param tau:
        :param kwargs:
        """
        super().__init__(time=time,
                         dt=dt,
                         rest=rest,
                         th=th,
                         ref=ref,
                         k=k,
                         tau=tau,
                         **kwargs)

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
                v[t:] += (t > (f_last + t_ref)) * s * self.kernel(np.arange(0, v[t:].size, 1) * self.dt, self.tau)

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

