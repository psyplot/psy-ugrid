.. SPDX-FileCopyrightText: 2024 Helmholtz-Zentrum hereon GmbH
..
.. SPDX-License-Identifier: CC-BY-4.0

.. _installation:

Installation
============

To install the `psy-ugrid` package, we recommend that
you install it from PyPi via::

    pip install psy-ugrid

If you are familiar with building a package with Cython, you can also
install it directly from `the source code repository on Gitlab`_ via::

    USE_CYTHON=true pip install git+https://codebase.helmholtz.cloud/psyplot/psy-ugrid.git

The latter should however only be done if you want to access the development
versions.

.. _the source code repository on Gitlab: https://codebase.helmholtz.cloud/psyplot/psy-ugrid


.. _install-develop:

Installation for development
----------------------------
Please head over to our :ref:`contributing guide <contributing>` for
installation instruction for development.

.. _usage:

Usage
=====

Once installed, the :class:`~psy_ugrid.decoder.UGridDecoder` is automatically
registered within the ``psyplot`` framework. Once you open a UGRID-conform
file, the :class:`~psy_ugrid.decoder.UGridDecoder` will be automatically used
for all variables in the netCDF-file that define a `mesh`. You do not have to
do anything extra.
