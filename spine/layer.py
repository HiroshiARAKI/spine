"""
The classes to create a Layer
Copyright(c) HiroshiARAKI
"""

from .hh import HodgkinHuxley
from .fhn import FitzHughNagumo
from .lif import LIF


RED = '\033[31m'
END = '\033[0m'


models = {
    'hh': HodgkinHuxley,
    'fhn': FitzHughNagumo,
    'lif': LIF,
    'hodgkin-huxley': HodgkinHuxley,
    'fitzhugh-nagumo': FitzHughNagumo,
}


model_name = {
    'hh': 'Hodgkin-Huxley',
    'fhn': 'FitzHugh-Nagumo',
    'lif': 'LIF',
    'hodgkin-huxley': 'Hodgkin-Huxley',
    'fitzhugh-nagumo': 'FitzHugh-Nagumo',
}


class Layer:
    def __init__(self, n: int = 10, model: str = 'HH', name: str = None, time: int = 100, dt: float = 0.01, **kwargs):
        """
        Construct a layer
        :param n:
        :param model:
        :param name:
        :param time:
        :param dt:
        :param kwargs:
        """
        if not model.lower() in models:
            print('{}Oops. The model name you gave is not correct.'.format(RED))
            print('The models you can give are ... ')
            for key in models:
                print(' - ' + key)
            print(END)
            exit(-1)

        self.n = n
        self.model = model
        if name is None:
            name = '{}-layer'.format(model)

        self.name = name
        self.neurons = [
            models[model.lower()](time=time, dt=dt, **kwargs) for _ in range(n)
        ]
        self.monitor = {}
        print('{}Constructed a Layer, [{}]!'.format(RED, name))
        print(' - Neuron: \t{}'.format(model_name[model.lower()]))
        print(' - # of Neu.:\t{} {}'.format(n, END))

    def calc_v(self, i):
        v_monitor = []
        for j, neu in enumerate(self.neurons):
            v = neu.calc_v(i[j])[0]
            v_monitor.append(v)

        self.monitor['v'] = v_monitor

        return v_monitor

