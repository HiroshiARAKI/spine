from .plotting import plot_spike_scatter
from .preprocess import PoissonSpike

from .functions import single_exponential_filter, double_exponential_filter

kernel = {
    'single': single_exponential_filter,
    'double': double_exponential_filter,
}
