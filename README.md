# SPINE: Spiking Neuron simulator
![python](https://img.shields.io/badge/python-3.x-blueviolet.svg?style=flat)
![version](https://img.shields.io/badge/version-1.3-blue.svg?style=flat)  
  
<p align="center"><img width="50%" src="img/spine.png"/></p>
  
SPINE is a simple Spiking Neuron simulator.  
[http://spine.hirlab.net](http://spine.hirlab.net) (japanese docs)  
 (2020.06.12 update: Added Double Exponential LIF and a plotting function)
 
## Line-up
### LIF: Leaky integrate-and-fire model
1. Single Exponential
    ```shell script
    $ python lif_sample.py
    ```
    ![lif](img/slif.png)

2. Double Exponential
    ```shell script
    $ python dlif_sample.py
    ```
    ![dlif](img/dlif.png)

### Hodgkin-Huxley model
```shell script
$ python hh_sample.py
```
![hh](img/hh_1.png)

### FitzHugh-Nagumo model
```shell script
$ python fhn_sample.py
```
![fhn](img/fhn.png)

## Example
```python
from spine import HodgkinHuxley
import numpy as np


if __name__ == '__main__':

    neu = HodgkinHuxley(time=100, dt=0.01)

    input_data = np.sin(0.5 * np.arange(0, neu.time, neu.dt))
    input_data = np.where(input_data > 0, 20, -5) + 10 * np.random.rand(int(neu.time / neu.dt))

    neu.calc_v(input_data)

    neu.plot_monitor()
```
![hh2](img/hh_2.png)

## Example 2
You can simulate neurons' activities as a layer.
```python
# LIF model
from spine import Layer
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    time = 500
    dt = 0.1

    layer = Layer(n=10, model='lif', time=time, dt=dt)

    input_data = [
        np.where(np.sin(np.random.rand() * np.arange(0, time, dt) + o) > 0, 100, -5) for o in range(10)
    ]

    input_data = np.array(input_data)
    v = layer.calc_v(input_data)

    print(np.array(v).shape)

    for i, d in enumerate(v):
        plt.subplot(10, 1, i+1)
        plt.plot(np.arange(0, time, dt), d)
        plt.ylabel(i)

    plt.xlabel('time [ms]')
    plt.show()

```
![layer1](img/layer_lif.png)

## Generate Poisson Spike train
```python
from spine import PoissonSpike
import numpy as np
import matplotlib.pyplot as plt

ps = PoissonSpike(np.random.random((10, 10)))
ps.plot_spikes()
plt.show()
```
![poisson](img/poisson.png)

## LICENSE
[MIT LICENSE](LICENSE.txt)  
Copyright (c) 2020 Hiroshi ARAKI