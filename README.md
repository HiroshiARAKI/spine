# SPINE: Spiking Neuron simulator
![version](https://img.shields.io/badge/version-1.0-blue.svg?style=flat)  
  
![spine](img/spine.png)

  
SPINE is a simple Spiking Neuron simulator.  
[http://spine.hirlab.net](http://spine.hirlab.net) (japanese docs)
 
## Line-up
### LIF: Leaky integrate-and-fire model
```bash
$ cd spine
$ python lif.py
```
![lif](img/lif_1.png)

### Hodgkin-Huxley model
```bash
$ cd spine
$ python hh.py
```
![hh](img/hh_1.png)

### FitzHugh-Nagumo model
```bash
$ cd spine
$ python fhn.py
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

## LICENSE
[MIT LICENSE](LICENSE.txt)  
Copyright (c) 2020 Hiroshi ARAKI