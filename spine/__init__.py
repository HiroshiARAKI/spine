"""
SPINE: SPIking NEuron models simulator

author: HiroshiARAKI
mail:   araki@hirlab.net

Copyright(c) HiroshiARAKI all rights reserved.
"""

from spine.neurons import (
    HodgkinHuxley,
    FitzHughNagumo,
    Izhikevich,
    LIF,
    IF,
)
from . import tools

from .network import Network

__version__ = '3.0'
