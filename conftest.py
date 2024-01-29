# SPDX-FileCopyrightText: 2024 Helmholtz-Zentrum hereon GmbH
#
# SPDX-License-Identifier: LGPL-3.0-only

"""pytest configuration script for psy-ugrid."""

from itertools import cycle
from pathlib import Path
from typing import Any, Callable, List

import pytest  # noqa: F401


@pytest.fixture
def get_test_file() -> Callable[[str], Path]:
    """Fixture to get the path to a test file."""

    def get_file(basename: str) -> Path:
        """Get a file in the test folder

        Parameters
        ----------
        basename : str
            The basename of the file, relative to the tests folder

        Returns
        -------
        Path
            The path to the file relative to the working directory
        """
        test_folder = Path(__file__).parent / "tests"
        return test_folder / basename

    return get_file


@pytest.fixture
def same_upon_permutation() -> Callable[[List, List], bool]:
    """Get a comparison operator for two lists acknowledging the boundaries.

    This fixture compares two lists that can be wrapped at the boundaries.
    """

    def compare(test: List, ref: List, missing_value: Any = -999) -> bool:
        """Check if the order of the elements are the same.

        This function is true, if the order of the elements are the same,
        independent on the location of the boundary. I.e. the following
        comparison results in a true condition::

            assert compare([6, 4, 5, 8, 1], [1, 6, 4, 5, 8])
        """

        def get_next(ref):
            ref.pop(0)
            ref.append(next(it))
            return ref

        # remove missing values
        if missing_value in test:
            test = test[: test.index(missing_value)]
        if missing_value in ref:
            ref = ref[: ref.index(missing_value)]

        if len(test) != len(ref):
            return False

        it = cycle(list(ref))
        # make a copy of the reference as we will modify it
        ref = list(ref)

        return any(test == get_next(ref) for i in range(len(ref)))

    return compare
