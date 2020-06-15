import numpy as np


def single_exponential_filter(t: np.ndarray, tau: tuple = (20, )) -> np.ndarray:
    """
    single_exponential_filter(t, tau: tuple = (20, ))

    :param t:    time
    :param tau:  time constant of decay
    :return:     np.ndarray (normalized [0, 1])
    """
    row_k = np.exp(-t / tau[0])
    v0 = 1. / np.max(row_k)
    return v0 * row_k


def double_exponential_filter(t: np.ndarray, tau: tuple = (10, 2.5)) -> np.ndarray:
    """
    double_exponential_filter(t, tau: tuple = (10, 2.5))
    - normalized [0, 1]

    :param t:    time
    :param tau:  time constants of rise and decay
    :return:     np.ndarray (normalized [0, 1])
    """
    row_k = np.exp(-t / tau[0]) - np.exp(-t / tau[1])
    v0 = 1. / np.max(row_k)

    return v0 * row_k

