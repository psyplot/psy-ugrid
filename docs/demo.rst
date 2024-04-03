.. SPDX-FileCopyrightText: 2024 Helmholtz-Zentrum hereon GmbH
..
.. SPDX-License-Identifier: CC-BY-4.0

.. _demo:

Demo
====

We will demonstrate how ``psy-ugrid`` can be used to visualize unstructured
data on it's native grid. We will use two demo files here:

- :download:`one with a triangular grid <simple_triangular_grid_si0.nc>`
- :download:`one with a grid that contains triangles and quadriliterals <simple_flexible_grid_si0.nc>`

.. ipython::

    In [1]: import psyplot.project as psy
       ...:
       ...: psy.rcParams["plotter.plot2d.cmap"] = "viridis"

    In [1]: ds_triangular = psy.open_dataset("simple_triangular_grid_si0.nc")
       ...: ds_triangular

    In [2]: ds_flexible = psy.open_dataset("simple_flexible_grid_si0.nc")
       ...: ds_flexible

The ugrid decoder automatically realized the ``mesh`` attributes in some of the
variables and therefore already assigned some coordinates for the netCDF
variables that hold the connectivity information.

Variables that hold a ``mesh`` attribute (such as the variable ``Mesh2_fcvar``
in these datasets) automatically use the :class:`~psy_ugrid.decoder.UGRIDDecoder`

.. ipython::

    In [3]: ds_triangular.Mesh2_fcvar.psy.decoder

.. _demo-face:

Visualization of face variables
-------------------------------
According to the UGRID conventions, variables can either represent a node in
the mesh, a face or an edge. Very often, however, the netCDF files only contain
the so-called face-node-connectivty, i.e. the information on how the faces
look like. The decoder of the ``psy-ugrid`` package is able to decode this
information and generate polygons that can then be visualized by plotmethods
of the psyplot plugin `psy-simple` or `psy-maps`:

.. ipython::

    @savefig docs_triangular_face.png width=4in
    In [4]: ds_triangular.psy.plot.plot2d(name="Mesh2_fcvar")

This even works out of the box for files, where we have mixed triangular and
quadriliteral faces:

.. ipython::

    @savefig docs_triangular_face.png width=4in
    In [5]: ds_flexible.psy.plot.plot2d(name="Mesh2_fcvar")

.. _demo-node:

Visualization of node and edge variables
----------------------------------------
As soon as a variable is defined on a node or edge variable, ``psy-ugrid``
computes the dual mesh by deriving the `face-edge-connectivity` and more. We
implemented a very efficient cython-based algorithm to do so, even for large
files. The derived polygons for this so-called dual mesh are then used for
visualizing the data.

.. ipython::

    @savefig docs_triangular_node.png width=4in
    In [6]: ds_triangular.psy.plot.plot2d(name="Mesh2_ndvar")

And again, this even works out of the box for files, where we have mixed triangular and
quadriliteral faces:

.. ipython::

    @savefig docs_triangular_node.png width=4in
    In [7]: ds_flexible.psy.plot.plot2d(name="Mesh2_ndvar")
