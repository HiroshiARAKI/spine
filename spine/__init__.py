"""
SPINE: SPIking NEuron models simulator

author: HiroshiARAKI
mail:   araki@hirlab.net

Copyright(c) HiroshiARAKI all rights reserved.
"""

from .lif import LIF
from .hh import HodgkinHuxley
from .fhn import FitzHughNagumo
from .poisson_generator import PoissonSpike

from .layer import Layer

__version__ = '1.2'
