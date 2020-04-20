"""
Hodgkin-Huxley Neuron model
Copyright(c) HiroshiARAKI
"""
import numpy as np
import matplotlib.pyplot as plt


class HodgkinHuxley:
    def __init__(self, time, dt, rest=-65.,
                 Cm=1.0, gNa=120., gK=36., gl=0.3, ENa=50., EK=-77., El=-54.387,
                 n=0.32, m=0.05, h=0.6, **kwargs):
        """
        Initialize Neuron parameters
        :param time: experimental time
        :param dt:   time step
        :param rest: resting potential
        :param Cm:   membrane capacity
        :param gNa:  Na+ channel conductance
        :param gK:   K+ channel conductance
        :param gl:   other (Cl) channel conductance
        :param ENa:  Na+ equilibrium potential
        :param EK:   K+ equilibrium potential
        :param El:   other (Cl) equilibrium potentials
        :param n:    Conductance param
        :param m:    Conductance param
        :param h:    Conductance param
        """
        self.time = time
        self.dt = dt
        self.rest = kwargs.get('rest', rest)
        self.Cm = kwargs.get('Cm', Cm)
        self.gNa = kwargs.get('gNa', gNa)
        self.gK = kwargs.get('gK', gK)
        self.gl = kwargs.get('gl', gl)
        self.ENa = kwargs.get('ENa', ENa)
        self.EK = kwargs.get('EK', EK)
        self.El = kwargs.get('El', El)
        self.n = kwargs.get('n', n)
        self.m = kwargs.get('m', m)
        self.h = kwargs.get('h', h)
        self.monitor = {}

    def calc_v(self, i):
        """ compute membrane potential """

        # initialize parameters
        v = self.rest
        n = self.n
        m = self.m
        h = self.h

        v_monitor = []
        n_monitor = []
        m_monitor = []
        h_monitor = []

        time = int(self.time / self.dt)

        # update time
        for t in range(time):
            # calc channel gating kinetics
            n += self.dn(v, n)
            m += self.dm(v, m)
            h += self.dh(v, h)

            # calc tiny membrane potential
            dv = (i[t] -
                  self.gK * n**4 * (v - self.EK) -         # K+ current
                  self.gNa * m**3 * h * (v - self.ENa) -   # Na+ current
                  self.gl * (v - self.El)) / self.Cm       # other current

            # calc new membrane potential
            v += dv * self.dt

            # record
            v_monitor.append(v)
            n_monitor.append(n)
            m_monitor.append(m)
            h_monitor.append(h)

        self.monitor['v'] = v_monitor
        self.monitor['n'] = n_monitor
        self.monitor['m'] = m_monitor
        self.monitor['h'] = h_monitor

        return v_monitor, n_monitor, m_monitor, h_monitor

    def dn(self, v, n):
        return (self.alpha_n(v) * (1 - n) - self.beta_n(v) * n) * self.dt

    def dm(self, v, m):
        return (self.alpha_m(v) * (1 - m) - self.beta_m(v) * m) * self.dt

    def dh(self, v, h):
        return (self.alpha_h(v) * (1 - h) - self.beta_h(v) * h) * self.dt

    def alpha_n(self, v):
        return 0.01 * (10 - (v - self.rest)) / (np.exp((10 - (v - self.rest))/10) - 1)

    def alpha_m(self, v):
        return 0.1 * (25 - (v - self.rest)) / (np.exp((25 - (v - self.rest))/10) - 1)

    def alpha_h(self, v):
        return 0.07 * np.exp(-(v - self.rest) / 20)

    def beta_n(self, v):
        return 0.125 * np.exp(-(v - self.rest) / 80)

    def beta_m(self, v):
        return 4 * np.exp(-(v - self.rest) / 18)

    def beta_h(self, v):
        return 1 / (np.exp((30 - (v - self.rest))/10) + 1)

    def plot_monitor(self, save=False, filename='hh.png', **kwargs):
        """
        plot membrane potential and conductance parameters
        :param save:
        :param filename:
        :param kwargs:
        :return:
        """
        x = np.arange(0, self.time, self.dt)
        plt.subplot(2, 1, 1)
        plt.title('Hodgkin-Huxley Neuron model Simulation')
        plt.plot(x, self.monitor['v'])
        plt.ylabel('V [mV]')
        plt.subplot(2, 1, 2)
        plt.plot(x, self.monitor['n'], label='n')
        plt.plot(x, self.monitor['m'], label='m')
        plt.plot(x, self.monitor['h'], label='h')
        plt.xlabel('time [ms]')
        plt.ylabel('Conductance param')
        plt.legend()
        if not save:
            plt.show()
        else:
            plt.savefig(filename, dpi=kwargs.get('dpi', 150))
        plt.close()


if __name__ == '__main__':
    # init experimental time and time-step
    time = 100
    dt = 0.01

    # create Hodgkin-Huxley Neuron
    neu = HodgkinHuxley(time, dt)

    # Input data (sin curve)
    input_data = np.sin(0.5 * np.arange(0, time, dt))
    input_data = np.where(input_data > 0, 20, -5) + 10 * np.random.rand(int(time/dt))
    input_data_2 = np.cos(0.3 * np.arange(0, time, dt) + 0.5)
    input_data_2 = np.where(input_data_2 > 0, 10, 0)
    input_data += input_data_2

    # calc neuron status
    v, m, n, h = neu.calc_v(input_data)

    # plot
    x = np.arange(0, time, dt)
    plt.subplot(3, 1, 1)
    plt.title('Hodgkin-Huxley Neuron model Simulation')
    plt.plot(x, input_data)
    plt.ylabel('I [μA/cm2]')

    plt.subplot(3, 1, 2)
    plt.plot(x, v)
    plt.ylabel('V [mV]')

    plt.subplot(3, 1, 3)
    plt.plot(x, n, label='n')
    plt.plot(x, m, label='m')
    plt.plot(x, h, label='h')
    plt.xlabel('time [ms]')
    plt.ylabel('Conductance param')
    plt.legend()

    plt.show()

