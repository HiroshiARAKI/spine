"""
FitzHugh-Nagumo Neuron model
Copyright(c) HiroshiARAKI
"""
import numpy as np
import matplotlib.pyplot as plt


class FitzHughNagumo:
    def __init__(self, time, dt, a=0.7, b=0.8, c=10, **kwargs):
        """
        Initialize Neuron parameters
        :param time:
        :param dt:
        :param a:
        :param b:
        :param c:
        """
        self.time = time
        self.dt = dt
        self.a = kwargs.get('a', a)
        self.b = kwargs.get('b', b)
        self.c = kwargs.get('c', c)
        self.monitor = {}

    def calc_v(self, i, v0=0, u0=0):
        """ compute membrane potential """
        v_monitor = []
        u_monitor = []

        v = v0
        u = u0

        time = int(self.time / self.dt)

        for t in range(time):
            u += self.du(u, v, i[t])
            v += self.dv(u, v)

            v_monitor.append(v)
            u_monitor.append(u)

        self.monitor['v'] = v_monitor
        self.monitor['u'] = u_monitor

        return v_monitor, u_monitor

    def du(self, u, v, i):
        return self.c * (u - u**3 / 3. - v + i) * self.dt

    def dv(self, u, v):
        return (u - self.b * v + self.a) * self.dt

    def plot_v(self, save=False, filename='fhn.png', **kwargs):
        """
        plot membrane potential
        :param save:
        :param filename:
        :param kwargs:
        :return:
        """
        x = np.arange(0, self.time, self.dt)
        plt.title('FitzHugh-Nagumo Neuron model Simulation')
        plt.plot(x, self.monitor['v'], label='v: recovery variable')
        plt.plot(x, self.monitor['u'], label='u: membrane potential')
        plt.xlabel('time [ms]')
        if not save:
            plt.show()
        else:
            plt.savefig(filename, dpi=kwargs.get('dpi', 150))
        plt.close()


if __name__ == '__main__':
    # init experimental time and time-step
    time = 100
    dt = 0.1

    # create Hodgkin-Huxley Neuron
    neu = FitzHughNagumo(time, dt)

    # Input data (sin curve)
    input_data = np.sin(0.2 * np.arange(0, time, dt))
    input_data = np.where(input_data > 0, 0.8, 0.1)

    v, u = neu.calc_v(input_data)

    # plot
    x = np.arange(0, time, dt)
    plt.subplot(2, 1, 1)
    plt.title('FitzHugh-Nagumo Neuron model Simulation')
    plt.plot(x, input_data)
    plt.ylabel('input')

    plt.subplot(2, 1, 2)
    plt.plot(x, v, label='v: recovery variable')
    plt.plot(x, u, label='u: membrane potential')
    plt.xlabel('time [ms]')

    plt.legend()
    plt.show()
