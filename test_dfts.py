import numpy as np

from dfts import *


def test_import_dft_two_loop():
    # The test succeeds if the import succeeds and fails
    # if the function is not in dfts yet.
    from dfts import dft_two_loop


def test_import_dft_one_loop():
    # The test succeeds if the import succeeds and fails
    # if the function is not in dfts yet.
    from dfts import dft_one_loop


def test_import_dft():
    # The test succeeds if the import succeeds and fails
    # if the function is not in dfts yet.
    from dfts import dft


def test_length_of_transform_two():
    N = 101
    y = np.zeros(N)
    c = dft_two_loop(y)
    assert len(c) == (N // 2 + 1)
    np.testing.assert_allclose(np.abs(c), y)


def test_length_of_transform_one():
    N = 101
    y = np.zeros(N)
    c = dft_one_loop(y)
    assert len(c) == (N // 2 + 1)
    np.testing.assert_allclose(np.abs(c), y)


def test_length_of_transform_dft():
    N = 101
    y = np.zeros(N)
    c = dft(y)
    assert len(c) == (N // 2 + 1)
    np.testing.assert_allclose(np.abs(c), y)
