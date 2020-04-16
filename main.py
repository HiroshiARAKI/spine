""" Example code """

from spine import HodgkinHuxley
import numpy as np


if __name__ == '__main__':

    neu = HodgkinHuxley(time=100, dt=0.01)

    input_data = np.sin(0.5 * np.arange(0, neu.time, neu.dt))
    input_data = np.where(input_data > 0, 20, -5) + 10 * np.random.rand(int(neu.time / neu.dt))

    neu.calc_v(input_data)

    neu.plot_monitor(save=True, filename='img/hh_2.png')
