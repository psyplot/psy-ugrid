# SPDX-FileCopyrightText: 2024 Helmholtz-Zentrum hereon GmbH
#
# SPDX-License-Identifier: LGPL-3.0-only

"""pytest configuration script for psy-ugrid."""

from pathlib import Path
from typing import Callable

import pytest  # noqa: F401


@pytest.fixture
def get_test_file() -> Callable[str, Path]:
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
