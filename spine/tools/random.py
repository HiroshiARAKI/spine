import numpy as np


def R(size_: int = 1):
    """
    [0, 1] Uniform Distribution
    :param size_:
    :return:
    """
    return np.random.random(size_)


def U(size_: int = 1, min_: float = -1, max_: float = 1):
    """
    Uniform Distribution
    :param size_:
    :param min_:
    :param max_:
    :return:
    """
    return np.random.uniform(min_, max_, size_)


def N(size_: int = 1, mean_: float = 0, std_: float = 1):
    """
    Normal Distribution
    :param size_:
    :param mean_:
    :param std_:
    :return:
    """
    return np.random.normal(mean_, std_, size_)


def P(size_: int = 1, lam_: float = 0.5):
    """
    Poisson Distribution
    :param size_:
    :param lam_:
    :return:
    """
    return np.random.poisson(lam_, size_)