# SPDX-FileCopyrightText: 2024 Helmholtz-Zentrum hereon GmbH
#
# SPDX-License-Identifier: CC0-1.0

"""Setup script for the psy-ugrid package."""
import os

import versioneer
from setuptools import Extension, setup

_USE_CYTHON = os.getenv("USE_CYTHON", "").lower()
USE_CYTHON = bool(_USE_CYTHON) and (
    not _USE_CYTHON.startswith("f") and not _USE_CYTHON.startswith("n")
)

ext = ".pyx" if USE_CYTHON else ".c"


extensions = [
    Extension(
        "psy_ugrid._create_dual_node_mesh",
        sources=[os.path.join("psy_ugrid", "_create_dual_node_mesh" + ext)],
    )
]


if USE_CYTHON:
    from Cython.Build import cythonize

    extensions = cythonize(extensions)


setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    ext_modules=extensions,
)
