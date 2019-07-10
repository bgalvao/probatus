import numpy as np
import pytest
from pyrisk.binning.binning import simple_bins, quantile_bins


def test_simple_bins():
    x = [1, 2, 1]
    bins = 3
    res = simple_bins(x, bins)
    assert (np.array_equal(res[0], np.array([2, 0, 1]))) and (
        np.array_equal(np.round(res[1]), np.round(np.array([1., 1.33333333, 1.66666667, 2.]))))


def test_quantile_bins():
    bins = 4
    x = np.random.normal(0, 1, size=100)
    counts, boundaries = quantile_bins(x, bins)
    assert sum(counts) == len(x)
    assert boundaries[0] == min(x)
    assert boundaries[-1] == max(x)
    assert counts[0] == pytest.approx(len(x) / bins, abs=1)
    assert np.std(counts) == pytest.approx(0, abs=1)