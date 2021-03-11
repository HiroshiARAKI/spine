from .functions import single_exponential_filter, double_exponential_filter
from .generator import PoissonSpike
from .plotting import plot_spike_scatter
from .random import R, U, N, P

kernel = {
    'single': single_exponential_filter,
    'double': double_exponential_filter,
}
