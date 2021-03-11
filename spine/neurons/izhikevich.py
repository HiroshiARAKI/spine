import numpy as np
import matplotlib.pyplot as plt

from .neuron import Neuron


class Izhikevich(Neuron):
    def __init__(self,
                 time: int,
                 dt: float = 1.0,
                 a: float = 0.02,
                 b: float = 0.2,
                 c: float = -65,
                 d: float = 8,
                 **kwargs):
        """
        Initialize Neuron parameters
        :param time:    experimental time
        :param dt:      time step
        :param a:       scaling factor for recovery variable 'u'
        :param b:       sensitivity of recovery variable 'u' for membrane voltage 'v'
        :param c:       resting potential
        :param d:       parameter influencing recovery variable 'u'. Bigger 'd', more time taken to recover membrane voltage.
        """
        super().__init__(time, dt)

        self.a = kwargs.get('a', a)
        self.b = kwargs.get('b', b)
        self.c = kwargs.get('c', c)
        self.d = kwargs.get('d', d)
        self.monitor = {
            'v': [],
            'u': [],
        }

    def calc_v(self, data):
        v = self.c
        u = self.d

        spikes = np.array(data[0])
        weights = np.array(data[1])
        data = [
            spikes[i] * weights[i]
            for i in range(weights.size)
        ]
        time = int(self.time / self.dt)

        data = np.sum(data, 0)

        for t in range(time):
            # Calc. u
            du = self.a * (self.b * v - u)
            u += du * self.dt
            self.monitor['u'].append(u)

            # Calc. v
            dv = 0.04 * v ** 2 + 5 * v + 140 - u + data[t]
            v += dv * self.dt
            self.monitor['v'].append(v)

            # Firing calc.
            if v >= 30:
                v = self.c
                u += self.d

        return self.monitor['v'], self.monitor['u']
