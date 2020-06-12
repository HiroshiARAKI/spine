"""
Artificial Neuron model class
Copyright(c) HiroshiARAKI
"""


class Neuron(object):
    def __init__(self, time: int, dt: float):
        """
        Neuron class constructor
        :param time:
        :param dt:
        """
        self.time = time
        self.dt = dt

    def calc_v(self, data):
        """
        Calculate Membrane Voltage
        :param data:
        :return:
        """
        pass

    def __str__(self):
        return self.__dict__

    def __iter__(self):
        return self.__dict__

    def __getitem__(self, key):
        return self.__dict__[key]
