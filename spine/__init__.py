"""
SPINE: SPIking NEuron models simulator

author: HiroshiARAKI
mail:   araki@hirlab.net

Copyright(c) HiroshiARAKI all rights reserved.
"""

from spine.neurons import (
    HodgkinHuxley,
    FitzHughNagumo,
    LIF,
    IF,
)
from .tools import PoissonSpike


__version__ = '2.1'
