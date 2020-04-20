""" Example code """
from spine import Layer
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    time = 200
    dt = 0.01

    # Construct a layer
    layer = Layer(n=10, model='hh', time=time, dt=dt)

    # Random Square waves as input data
    input_data = [
        np.where(np.sin(np.random.rand() * np.arange(0, time, dt) + o) > 0, 20, -5) for o in range(10)
    ]

    input_data = np.array(input_data)

    # calc membrane potentials
    v = layer.calc_v(input_data)

    # plot
    for i, d in enumerate(v):
        plt.subplot(10, 1, i+1)
        plt.plot(np.arange(0, time, dt), d)
        plt.ylabel(i)

    plt.xlabel('time [ms]')
    plt.show()


