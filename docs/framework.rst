
Framework
==========

XMF is a framework for the X-ray mirror surface shape fitting, particularly in the context of convex and concave shapes.

.. image:: _static/mirror_surfaces.png
   :alt: [mirror surfaces]
   :width: 700px
   :align: center
   :target: none
.. centered:: Some typical X-ray mirror surfaces

It provides data analysis and visualization tools for fitting measurement data to various geometric shapes, including elliptic cylinders, hyperbolic cylinders, ellipsoids, and hyperboloids.

.. image:: _static/framework.png
   :alt: [framework]
   :width: 700px
   :align: center
   :target: none
.. centered:: X-ray mirror surface shape fitting framework (XMF)

The framework is composed of four main layers:

- **Layer 1: Standard shape from expressions**. Contains the standard mathematical expressions of various geometric shapes.
- **Layer 2: Surface generation**. Implements the algorithms for generating surface shapes in height or slope, by taking into account the rotation and translation of the shapes.
- **Layer 3: Optimization**. Optimize the user-selected fitting parameters.
- **Layer 4: Function wrapper**. Offers convenient functions for working with measurement data for specific geometric shapes.
