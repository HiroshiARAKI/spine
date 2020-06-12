"""
SPINE: SPIking NEuron models simulator

author: HiroshiARAKI
mail:   araki@hirlab.net

Copyright(c) HiroshiARAKI all rights reserved.
"""

from .lif import LIF, DLIF
from .hh import HodgkinHuxley
from .fhn import FitzHughNagumo
from .poisson_generator import PoissonSpike

from .layer import Layer

from .plotting import plot_spike_scatter

__version__ = '1.3'
