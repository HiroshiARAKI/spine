# SPINE: Spiking Neuron simulator
![python](https://img.shields.io/badge/python-3.x-blueviolet.svg?style=flat)
![version](https://img.shields.io/badge/version-2.1-blue.svg?style=flat)  
  
<p align="center"><img width="50%" src="img/spine.png"/></p>
  
SPINE is a simple Spiking Neuron simulator.  
Documentation is   
[http://spine.hirlab.net](http://spine.hirlab.net) (japanese docs)  
or  
please refer to `***_sample.py`.
 
## Line-up
### IF: integrate-and-fire model
```python
from spine import IF
neu = IF(time=300,
         dt=0.1,
         k='double',  # use double exponential filter
         tau=(10, 2)  # time constants of filter
         )
```
* Example
   ```shell script
    $ python if_sample.py
    ``` 
    ![doubleIF](img/dif.png)
### LIF: Leaky integrate-and-fire model
```python
from spine import LIF
neu = LIF(time=300,
          dt=0.1,
          k='double',  # use double exponential filter
          tau=(10, 2)  # time constants of filter
          )
```
* Example
    ```shell script
    $ python lif_sample.py
    ```
    ![doubleLIF](img/dlif.png)

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

## Generate Poisson Spike train and a plotting function
```python
from spine import PoissonSpike
from spine.tools.plotting import plot_spike_scatter

import numpy as np
import matplotlib.pyplot as plt

spikes = PoissonSpike(np.random.random((10, 10)), time=300, dt=0.1).spikes
plot_spike_scatter(spikes, time=300, dt=0.1)
plt.title('Spike firing timing')
plt.show()
```
![poisson](img/poisson.png)

## LICENSE
[MIT LICENSE](LICENSE.txt)  
Copyright (c) 2020 Hiroshi ARAKI