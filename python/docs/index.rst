.. xmf_dev documentation master file, created by
   sphinx-quickstart on Tue Jul  1 16:32:05 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

XMF documentation
=====================

Welcome to the XMF documentation!

In this documentation, you will find information about the XMF project, including its modules and functionalities in Python and MATLAB.


Framework:
----------

XMF is a framework for the X-ray mirror surface shape fitting, particularly in the context of convex and concave shapes.

.. image:: _static/mirror_surfaces.png
   :alt: [mirror surfaces]
   :width: 700px
   :align: center
.. centered:: Some typical X-ray mirror surfaces

It provides data analysis and visualization tools for fitting measurement data to various geometric shapes, including elliptic cylinders, hyperbolic cylinders, ellipsoids, and hyperboloids.

.. image:: _static/framework.png
   :alt: [framework]
   :width: 700px
   :align: center
.. centered:: X-ray mirror surface shape fitting framework (XMF)

The framework is composed of four main layers:

1. **Standard shape layer**: Contains the standard mathematical expressions of various geometric shapes.
2. **Surface generation layer**: Implements the algorithms for generating surface shapes in height or slope, by taking into account the rotation and translation of the shapes.
3. **Optimization layer**: Optimize the user-selected fitting parameters.
4. **Function wrapping layer**: Offers convenient functions for working with measurement data for specific geometric shapes.

.. toctree::
   :maxdepth: 2
   :caption: Examples gallery:

   auto_examples/index

Example codes:
--------------

Python example for fitting a concave ellipse slope:

.. code-block:: python

   import xmf

   target_params_dict = {
      'p': p,
      'q': q,
      'theta': theta,
      'x_i': x_i,
      'beta': beta,
   }

   params_input_dict = {
      'p': p,
      'q': q,
      'theta': theta
   }

   opt_dict = {
      'p': False,
      'q': False,
      'theta': False
   }

   sx1d_res, sx1d_fit, opt_params_dict, opt_params_ci_dict, _ = xmf.fit_concave_ellipse_slope(x1d, sx1d_measured, params_input_dict, opt_dict) 
   xmf.fig_show_1d_fitting_slope(x1d, sx1d_measured, sx1d_fit, sx1d_res, target_params_dict, opt_params_dict, opt_params_ci_dict, 'Concave Ellipse Slope') 

MATLAB example for fitting a concave ellipse slope:

.. code-block:: matlab
   
   opt_struct.p = false;
   opt_struct.q = false;
   opt_struct.theta = false;

   [sx1d_res, sx1d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_ellipse_slope(x1d, sx1d_measured, input_params_struct, opt_struct);
   fig_show_1d_fitting_slope(x1d, sx1d_measured, sx1d_fit, sx1d_res, input_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Elliptic Cylinder');

   
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   source/modules
   source/xmf_matlab


Indices and tables
==================
   
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

