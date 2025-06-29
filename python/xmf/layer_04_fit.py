# Copyright (c) 2025 Racheal Xu, Lei Huang
#
# Lei Huang
# huanglei0114gmail.com
#
# All rights reserved
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np

from xmf.layer_01_standard import (
    standard_convex_ellipsoid_height,
    standard_concave_ellipsoid_height,
    standard_convex_elliptic_cylinder_height,
    standard_concave_elliptic_cylinder_height,
    standard_convex_elliptic_cylinder_xslope,
    standard_concave_elliptic_cylinder_xslope,
    standard_convex_hyperboloid_height,
    standard_concave_hyperboloid_height,
    standard_convex_hyperbolic_cylinder_height,
    standard_concave_hyperbolic_cylinder_height,
    standard_convex_hyperbolic_cylinder_xslope,
    standard_concave_hyperbolic_cylinder_xslope,
)

from xmf.layer_02_generation import (
    generate_1d_height,
    generate_1d_slope,
    generate_2d_curved_surface_height,
    generate_2d_cylinder_height,
)

from xmf.layer_03_optimization import optimize_parameters

def fit_convex_ellipsoid_height(x2d: np.ndarray,
                                  y2d: np.ndarray,
                                  z2d: np.ndarray,
                                  pqtxy: np.ndarray,
                                  opt_dict: dict,
                                ):
    """
    Fit the convex ellipsoid parameters from a measured height map.

    Parameters
    ----------
        x2d: `numpy.ndarray`
            The x coordinate in the suggested unit of [m]
        y2d: `numpy.ndarray`
            The y coordinate in the suggested unit of [m]
        z2d: `numpy.ndarray`
            The z coordinate in the suggested unit of [m]
        pqtxy: `numpy.ndarray`
            The the ``p``, ``q``, ``theta``, ``x_i``(optional), and ``y_i``(optional) target
            parameters, in the suggested unit of [m] [m] [rad] [m]
        opt_dict: `dict`
            Set whether a parameter to be optimized, 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``
            in the suggested unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_lmfit: `bool`
            The flag to identify if using lmfit module to fit
    Returns
    -------
        z2d_residual: `numpy.ndarray`
            The height residual after the best fit.
        z2d_fit: `numpy.ndarray`
            The fitted height
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
    """

    return optimize_parameters(generate_2d_curved_surface_height, standard_convex_ellipsoid_height, x2d, y2d, z2d, pqtxy, opt_dict)


def fit_concave_ellipsoid_height(x2d: np.ndarray,
                                  y2d: np.ndarray,
                                  z2d: np.ndarray,
                                  pqtxy: np.ndarray,
                                  opt_dict: dict,
                                ):
    """
    Fit the concave ellipsoid parameters from a measured height map.

    Parameters
    ----------
        x2d: `numpy.ndarray`
            The x coordinate in the suggested unit of [m]
        y2d: `numpy.ndarray`
            The y coordinate in the suggested unit of [m]
        z2d: `numpy.ndarray`
            The z coordinate in the suggested unit of [m]
        pqtxy: `numpy.ndarray`
            The the ``p``, ``q``, ``theta``, ``x_i``(optional), and ``y_i``(optional) target
            parameters, in the suggested unit of [m] [m] [rad] [m]
        opt_dict: `dict`
            Set whether a parameter to be optimized, 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``
            in the suggested unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_lmfit: `bool`
            The flag to identify if using lmfit module to fit
    Returns
    -------
        z2d_residual: `numpy.ndarray`
            The height residual after the best fit.
        z2d_fit: `numpy.ndarray`
            The fitted height
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
    """

    return optimize_parameters(generate_2d_curved_surface_height, standard_concave_ellipsoid_height, x2d, y2d, z2d, pqtxy, opt_dict)



def fit_convex_elliptic_cylinder_height(x2d: np.ndarray,
                                  y2d: np.ndarray,
                                  z2d: np.ndarray,
                                  pqtx: np.ndarray,
                                  opt_dict: dict,
                                ):
    """
    Fit the convex elliptic cylinder parameters from a measured height map.

    Parameters
    ----------
        x2d: `numpy.ndarray`
            The x coordinate in the suggested unit of [m]
        y2d: `numpy.ndarray`
            The y coordinate in the suggested unit of [m]
        z2d: `numpy.ndarray`
            The z coordinate in the suggested unit of [m]
        pqtx: `numpy.ndarray`
            The the ``p``, ``q``, ``theta``, ``x_i`` (optional) target
            parameters, in the suggested unit of [m] [m] [rad] [m]
        opt_dict: `dict`
            Set whether a parameter to be optimized, 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``
            in the suggested unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_lmfit: `bool`
            The flag to identify if using lmfit module to fit
    Returns
    -------
        z2d_residual: `numpy.ndarray`
            The height residual after the best fit.
        z2d_fit: `numpy.ndarray`
            The fitted height
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
    """

    return optimize_parameters(generate_2d_curved_surface_height, standard_convex_elliptic_cylinder_height, x2d, y2d, z2d, pqtx, opt_dict)



def fit_concave_elliptic_cylinder_height(x2d: np.ndarray,
                                  y2d: np.ndarray,
                                  z2d: np.ndarray,
                                  pqtx: np.ndarray,
                                  opt_dict: dict,
                                ):
    """
    Fit the concave elliptic cylinder parameters from a measured height map.

    Parameters
    ----------
        x2d: `numpy.ndarray`
            The x coordinate in the suggested unit of [m]
        y2d: `numpy.ndarray`
            The y coordinate in the suggested unit of [m]
        z2d: `numpy.ndarray`
            The z coordinate in the suggested unit of [m]
        pqtx: `numpy.ndarray`
            The the ``p``, ``q``, ``theta``, ``x_i`` (optional) target
            parameters, in the suggested unit of [m] [m] [rad] [m]
        opt_dict: `dict`
            Set whether a parameter to be optimized, 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``
            in the suggested unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_lmfit: `bool`
            The flag to identify if using lmfit module to fit
    Returns
    -------
        z2d_residual: `numpy.ndarray`
            The height residual after the best fit.
        z2d_fit: `numpy.ndarray`
            The fitted height
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
    """

    return optimize_parameters(generate_2d_curved_surface_height, standard_concave_elliptic_cylinder_height, x2d, y2d, z2d, pqtx, opt_dict)


def fit_convex_ellipse_height(x1d: np.ndarray,
                                z1d: np.ndarray,
                                pqtx: np.ndarray,
                                opt_dict: dict,
                                is_lmfit: bool = True,
                                ):
    """
    Fit the convex ellipse parameters from a measured height profile.

    Parameters
    ----------
        x1d: `numpy.ndarray`
            The x coordinate in the suggested unit of [m]
        z1d: `numpy.ndarray`
            The z coordinate in the suggested unit of [m]
        pqtx: `numpy.ndarray`
            The the ``p``, ``q``, ``theta``, ``x_i`` (optional) target
            parameters, in the suggested unit of [m] [m] [rad] [m]
        opt_dict: `dict`
            Set whether a parameter to be optimized, 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``
            in the suggested unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_lmfit: `bool`
            The flag to identify if using lmfit module to fit
    Returns
    -------
        z1d_residual: `numpy.ndarray`
            The height residual after the best fit.
        z1d_fit: `numpy.ndarray`
            The fitted height
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
    """

    y1d = np.zeros_like(x1d)  # No need to consider y-coordinates in metrology coordinates for 1D case

    return optimize_parameters(generate_1d_height, standard_convex_elliptic_cylinder_height, x1d, y1d, z1d, pqtx, opt_dict)

def fit_concave_ellipse_height(x1d: np.ndarray,
                                z1d: np.ndarray,
                                pqtx: np.ndarray,
                                opt_dict: dict,
                                is_lmfit: bool = True,
                                ):
    """
    Fit the concave ellipse parameters from a measured height profile.

    Parameters
    ----------
        x1d: `numpy.ndarray`
            The x coordinate in the suggested unit of [m]
        z1d: `numpy.ndarray`
            The z coordinate in the suggested unit of [m]
        pqtx: `numpy.ndarray`
            The the ``p``, ``q``, ``theta``, ``x_i`` (optional) target
            parameters, in the suggested unit of [m] [m] [rad] [m]
        opt_dict: `dict`
            Set whether a parameter to be optimized, 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``
            in the suggested unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_lmfit: `bool`
            The flag to identify if using lmfit module to fit
    Returns
    -------
        z1d_residual: `numpy.ndarray`
            The height residual after the best fit.
        z1d_fit: `numpy.ndarray`
            The fitted height
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
    """

    y1d = np.zeros_like(x1d)  # No need to consider y-coordinates in metrology coordinates for 1D case

    return optimize_parameters(generate_1d_height, standard_concave_elliptic_cylinder_height, x1d, y1d, z1d, pqtx, opt_dict)

def fit_convex_ellipse_slope(x1d: np.ndarray,
                              sx1d: np.ndarray,
                              pqtx: np.ndarray,
                              opt_dict: dict,
                              is_lmfit: bool = True,
                              ):
    """
    Fit the convex ellipse parameters from a measured slope profile.

    Parameters
    ----------
        x1d: `numpy.ndarray`
            The x coordinate in the suggested unit of [m]
        sx1d: `numpy.ndarray`
            The measured slope in the suggested unit of [m/m]
        pqtx: `numpy.ndarray`
            The the ``p``, ``q``, ``theta``, ``x_i`` (optional) target
            parameters, in the suggested unit of [m] [m] [rad] [m]
        opt_dict: `dict`
            Set whether a parameter to be optimized, 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``
            in the suggested unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_lmfit: `bool`
            The flag to identify if using lmfit module to fit
    Returns
    -------
        z1d_residual: `numpy.ndarray`
            The height residual after the best fit.
        sx1d_fit: `numpy.ndarray`
            The fitted slope
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
    """

    y1d = np.zeros_like(x1d)

    return optimize_parameters(generate_1d_slope, standard_convex_elliptic_cylinder_xslope, x1d, y1d, sx1d, pqtx, opt_dict)

def fit_concave_ellipse_slope(x1d: np.ndarray,
                               sx1d: np.ndarray,
                               input_params_dict: dict,
                               opt_dict: dict,
                               is_lmfit: bool = True,
                               ):
    """
    Fit the concave ellipse parameters from a measured slope profile.

    Parameters
    ----------
        x1d: `numpy.ndarray`
            The x coordinate in the suggested unit of [m]
        sx1d: `numpy.ndarray`
            The measured slope in the suggested unit of [m/m]
        pqtx: `numpy.ndarray`
            The the ``p``, ``q``, ``theta``, ``x_i`` (optional) target
            parameters, in the suggested unit of [m] [m] [rad] [m]
        opt_dict: `dict`
            Set whether a parameter to be optimized, 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``
            in the suggested unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_lmfit: `bool`
            The flag to identify if using lmfit module to fit
    Returns
    -------
        z1d_residual: `numpy.ndarray`
            The height residual after the best fit.
        sx1d_fit: `numpy.ndarray`
            The fitted slope
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
    """

    y1d = np.zeros_like(x1d)  # No need to consider y-coordinates in metrology coordinates for 1D case

    return optimize_parameters(generate_1d_slope, standard_concave_elliptic_cylinder_xslope, x1d, y1d, sx1d, input_params_dict, opt_dict)


def fit_convex_hyperboloid_height(x2d: np.ndarray,
                                  y2d: np.ndarray,
                                  z2d: np.ndarray,
                                  pqtxy: np.ndarray,
                                  opt_dict: dict,
                                ):
    """
    Fit the convex hyperboloid parameters from a measured height map.

    Parameters
    ----------
        x2d: `numpy.ndarray`
            The x coordinate in the suggested unit of [m]
        y2d: `numpy.ndarray`
            The y coordinate in the suggested unit of [m]
        z2d: `numpy.ndarray`
            The z coordinate in the suggested unit of [m]
        pqtxy: `numpy.ndarray`
            The the ``p``, ``q``, ``theta``, ``x_i``(optional), and ``y_i``(optional) target
            parameters, in the suggested unit of [m] [m] [rad] [m]
        opt_dict: `dict`
            Set whether a parameter to be optimized, 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``
            in the suggested unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_lmfit: `bool`
            The flag to identify if using lmfit module to fit
    Returns
    -------
        z2d_residual: `numpy.ndarray`
            The height residual after the best fit.
        z2d_fit: `numpy.ndarray`
            The fitted height
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
    """

    return optimize_parameters(generate_2d_curved_surface_height, standard_convex_hyperboloid_height, x2d, y2d, z2d, pqtxy, opt_dict)

def fit_concave_hyperboloid_height(x2d: np.ndarray,
                                    y2d: np.ndarray,
                                    z2d: np.ndarray,
                                    pqtxy: np.ndarray,
                                    opt_dict: dict,
                                      ):
    """
    Fit the concave hyperboloid parameters from a measured height map.

    Parameters
    ----------
        x2d: `numpy.ndarray`
            The x coordinate in the suggested unit of [m]
        y2d: `numpy.ndarray`
            The y coordinate in the suggested unit of [m]
        z2d: `numpy.ndarray`
            The z coordinate in the suggested unit of [m]
        pqtxy: `numpy.ndarray`
            The the ``p``, ``q``, ``theta``, ``x_i``(optional), and ``y_i``(optional) target
            parameters, in the suggested unit of [m] [m] [rad] [m]
        opt_dict: `dict`
            Set whether a parameter to be optimized, 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``
            in the suggested unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_lmfit: `bool`
            The flag to identify if using lmfit module to fit
    Returns
    -------
        z2d_residual: `numpy.ndarray`
            The height residual after the best fit.
        z2d_fit: `numpy.ndarray`
            The fitted height
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
    """

    return optimize_parameters(generate_2d_curved_surface_height, standard_concave_hyperboloid_height, x2d, y2d, z2d, pqtxy, opt_dict)

def fit_convex_hyperbolic_cylinder_height(x2d: np.ndarray,
                                           y2d: np.ndarray,
                                           z2d: np.ndarray,
                                           pqtxy: np.ndarray,
                                           opt_dict: dict,
                                                    ):
    """
    Fit the convex hyperbolic cylinder parameters from a measured height map.

    Parameters
    ----------
        x2d: `numpy.ndarray`
            The x coordinate in the suggested unit of [m]
        y2d: `numpy.ndarray`
            The y coordinate in the suggested unit of [m]
        z2d: `numpy.ndarray`
            The z coordinate in the suggested unit of [m]
        pqtx: `numpy.ndarray`
            The the ``p``, ``q``, ``theta``, ``x_i`` (optional) target
            parameters, in the suggested unit of [m] [m] [rad] [m]
        opt_dict: `dict`
            Set whether a parameter to be optimized, 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``
            in the suggested unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_lmfit: `bool`
            The flag to identify if using lmfit module to fit
    Returns
    -------
        z2d_residual: `numpy.ndarray`
            The height residual after the best fit.
        z2d_fit: `numpy.ndarray`
            The fitted height
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
    """

    return  optimize_parameters(generate_2d_cylinder_height, standard_convex_hyperbolic_cylinder_height, x2d, y2d, z2d, pqtxy, opt_dict)

def fit_concave_hyperbolic_cylinder_height(x2d: np.ndarray,
                                           y2d: np.ndarray,
                                           z2d: np.ndarray,
                                           pqtxy: np.ndarray,
                                           opt_dict: dict,
                                                    ):
    """
    Fit the concave hyperbolic cylinder parameters from a measured height map.

    Parameters
    ----------
        x2d: `numpy.ndarray`
            The x coordinate in the suggested unit of [m]
        y2d: `numpy.ndarray`
            The y coordinate in the suggested unit of [m]
        z2d: `numpy.ndarray`
            The z coordinate in the suggested unit of [m]
        pqtx: `numpy.ndarray`
            The the ``p``, ``q``, ``theta``, ``x_i`` (optional) target
            parameters, in the suggested unit of [m] [m] [rad] [m]
        opt_dict: `dict`
            Set whether a parameter to be optimized, 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``
            in the suggested unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_lmfit: `bool`
            The flag to identify if using lmfit module to fit
    Returns
    -------
        z2d_residual: `numpy.ndarray`
            The height residual after the best fit.
        z2d_fit: `numpy.ndarray`
            The fitted height
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
    """

    return  optimize_parameters(generate_2d_cylinder_height, standard_concave_hyperbolic_cylinder_height, x2d, y2d, z2d, pqtxy, opt_dict)

def fit_convex_hyperbola_height(x1d: np.ndarray,
                                 z1d_measured: np.ndarray,
                                 pqtx: np.ndarray,
                                 opt_1d_cylinder_height: dict,
                                 is_lmfit: bool = True,
                                 ):
    """
    Fit the convex hyperbola parameters from a measured height profile.

    Parameters
    ----------
        x1d: `numpy.ndarray`
            The x coordinate in the suggested unit of [m]
        z1d: `numpy.ndarray`
            The z coordinate in the suggested unit of [m]
        pqtx: `numpy.ndarray`
            The the ``p``, ``q``, ``theta``, ``x_i`` (optional) target
            parameters, in the suggested unit of [m] [m] [rad] [m]
        opt_dict: `dict`
            Set whether a parameter to be optimized, 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``
            in the suggested unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_lmfit: `bool`
            The flag to identify if using lmfit module to fit
    Returns
    -------
        z1d_residual: `numpy.ndarray`
            The height residual after the best fit.
        z1d_fit: `numpy.ndarray`
            The fitted height
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
    """

    y1d = np.zeros_like(x1d)  # No need to consider y-coordinates in metrology coordinates for 1D case

    return optimize_parameters(generate_1d_height, standard_convex_hyperbolic_cylinder_height, x1d, y1d, z1d_measured, pqtx, opt_1d_cylinder_height)

def fit_concave_hyperbola_height(x1d: np.ndarray,
                                  z1d_measured: np.ndarray,
                                  pqtx: np.ndarray,
                                  opt_1d_cylinder_height: dict,
                                  ):
    """
    Fit the concave hyperbola parameters from a measured height profile.

    Parameters
    ----------
        x1d: `numpy.ndarray`
            The x coordinate in the suggested unit of [m]
        z1d: `numpy.ndarray`
            The z coordinate in the suggested unit of [m]
        pqtx: `numpy.ndarray`
            The the ``p``, ``q``, ``theta``, ``x_i`` (optional) target
            parameters, in the suggested unit of [m] [m] [rad] [m]
        opt_dict: `dict`
            Set whether a parameter to be optimized, 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``
            in the suggested unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_lmfit: `bool`
            The flag to identify if using lmfit module to fit
    Returns
    -------
        z1d_residual: `numpy.ndarray`
            The height residual after the best fit.
        z1d_fit: `numpy.ndarray`
            The fitted height
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
    """

    y1d = np.zeros_like(x1d)  # No need to consider y-coordinates in metrology coordinates for 1D case

    return optimize_parameters(generate_1d_height, standard_concave_hyperbolic_cylinder_height, x1d, y1d, z1d_measured, pqtx, opt_1d_cylinder_height)

def fit_convex_hyperbola_slope(x1d: np.ndarray,
                                sx1d: np.ndarray,
                                pqtx: np.ndarray,
                                opt_dict: dict,
                                is_lmfit: bool = True,
                                ):
    """
    Fit the convex hyperbola parameters from a measured slope profile.

    Parameters
    ----------
        x1d: `numpy.ndarray`
            The x coordinate in the suggested unit of [m]
        sx1d: `numpy.ndarray`
            The measured slope in the suggested unit of [m/m]
        pqtx: `numpy.ndarray`
            The the ``p``, ``q``, ``theta``, ``x_i`` (optional) target
            parameters, in the suggested unit of [m] [m] [rad] [m]
        opt_dict: `dict`
            Set whether a parameter to be optimized, 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``
            in the suggested unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_lmfit: `bool`
            The flag to identify if using lmfit module to fit
    Returns
    -------
        z1d_residual: `numpy.ndarray`
            The height residual after the best fit.
        sx1d_fit: `numpy.ndarray`
            The fitted slope
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
    """

    y1d = np.zeros_like(x1d)  # No need to consider y-coordinates in metrology coordinates for 1D case

    return optimize_parameters(generate_1d_slope, standard_convex_hyperbolic_cylinder_xslope, x1d, y1d, sx1d, pqtx, opt_dict)

def fit_concave_hyperbola_slope(x1d: np.ndarray,
                                 sx1d: np.ndarray,
                                 pqtx: np.ndarray,
                                 opt_dict: dict,
                                 is_lmfit: bool = True,
                                 ):
    """
    Fit the concave hyperbola parameters from a measured slope profile.

    Parameters
    ----------
        x1d: `numpy.ndarray`
            The x coordinate in the suggested unit of [m]
        sx1d: `numpy.ndarray`
            The measured slope in the suggested unit of [m/m]
        pqtx: `numpy.ndarray`
            The the ``p``, ``q``, ``theta``, ``x_i`` (optional) target
            parameters, in the suggested unit of [m] [m] [rad] [m]
        opt_dict: `dict`
            Set whether a parameter to be optimized, 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``
            in the suggested unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_lmfit: `bool`
            The flag to identify if using lmfit module to fit
    Returns
    -------
        z1d_residual: `numpy.ndarray`
            The height residual after the best fit.
        sx1d_fit: `numpy.ndarray`
            The fitted slope
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
    """

    y1d = np.zeros_like(x1d)  # No need to consider y-coordinates in metrology coordinates for 1D case

    return optimize_parameters(generate_1d_slope, standard_concave_hyperbolic_cylinder_xslope, x1d, y1d, sx1d, pqtx, opt_dict)
