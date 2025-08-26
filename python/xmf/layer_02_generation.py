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

import types
import numpy as np


def compose_transformation_matrix(alpha: float,
                                    beta: float,
                                    gamma: float,
                                    x_i: float,
                                    y_i: float,
                                    z_i: float):
    """
    The standard concave hyperbolic cylinder x-slope with (``abs_p``, ``abs_q``, ``theta``)

    Parameters
    ----------
        alpha: `float`
            The angle around x-axis
        beta: `float`
            The angle around y-axis
        gamma: `float`
            The angle around z-axis
        x_i: `float`
            x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
        y_i: `float`
            y-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the y-position of chief ray intersection in metrology coordinates
        z_i: `float`
            z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
    Returns
    -------
        T: `numpy.ndarray`
            The x-slope"
    """

    R_x = np.array([1, 0, 0, 0, np.cos(alpha), -np.sin(alpha), 0, np.sin(alpha), np.cos(alpha)]).reshape(3, 3)
    R_y = np.array([np.cos(beta), 0, np.sin(beta), 0, 1, 0, -np.sin(beta), 0, np.cos(beta)]).reshape(3, 3)
    R_z = np.array([np.cos(gamma), -np.sin(gamma), 0, np.sin(gamma), np.cos(gamma), 0, 0, 0, 1]).reshape(3, 3)
    R = R_z @ R_y @ R_x

    t = np.array([x_i, y_i, z_i]).reshape(3, 1)

    Rt = np.hstack((R, t))
    T = np.vstack((Rt, [0, 0, 0, 1]))

    return T


def iter_generate_height(standard_height_function,
                          x2d: np.ndarray,
                          y2d: np.ndarray,
                          p: float,
                          q: float,
                          theta: float,
                          tf: np.ndarray,
                          z2d_measured: np.ndarray = None,
                          thr_rms_dxy: float = 1e-9):


    """
    The height generation with iterations(``p``, ``q``, ``theta``,  ``thr_rms_dxy``)

    Parameters
    ----------
        standard_height_function:
            The standard height function
        x2d: `numpy.ndarray`
            The 2D x coordinates
        y2d: `numpy.ndarray`
            The 2D y coordinates
        p: `float`
            The ``p`` value: the distance from the source to the chief ray intersection
        q: `float`
            The ``q`` value: the distance from the chief ray intersection to the focus
        theta: `float`
            The grazing angle
        tf: `numpy.ndarray`
            The transformation matrix
        z2d_measured: `numpy.ndarray`
            The measured height map
        thr_rms_dxy: `float`
            The threshold of RMS
    Returns
    -------
        z2d: `numpy.ndarray`
            The height map
    """

    if z2d_measured is None:
        z2d_measured = np.zeros(x2d.shape)

    # Initialization
    z2d = z2d_measured
    rms_dxy = np.inf

    # Use while loop to make sure the transformation makes sense as
    # (x2d_s, y2d_s, z2d_s) --- tf ---> (x2d, y2d, z2d) and
    # (x2d, y2d, z2d) --- tf^{-1} ---> (x2d_s, y2d_s, z2d_s)
    while rms_dxy > thr_rms_dxy:

        # Points in metrology coordinates
        m = np.vstack((x2d.flatten(), y2d.flatten(), z2d.flatten(), np.ones(z2d.size)))
        # Transform back to standard mirror coordinates
        m_s = np.linalg.inv(tf) @ m # X_m = tansform * X_s

        # Use standard function to generate shape in standard mirror coordinates
        x2d_s = m_s[0].reshape(x2d.shape)
        y2d_s = m_s[1].reshape(y2d.shape)

        try:
            z2d_s = np.real(standard_height_function(x2d_s, y2d_s, p, q, theta)) # 2D curved shape
        except ValueError:
            z2d_s = np.real(standard_height_function(x2d_s, p, q, theta)) # 1D or 2D cylinder
        except:
            raise

        s = np.vstack((x2d_s.flatten(), y2d_s.flatten(), z2d_s.flatten(), np.ones(z2d_s.size)))

        # Transform to metrology coodinates to update the shape
        s_m = tf @ s # X_m = tansform * X_s
        x2d_s_in_m = s_m[0].reshape(x2d.shape)
        y2d_s_in_m = s_m[1].reshape(y2d.shape)
        z2d = s_m[2].reshape(z2d.shape)

        # Check and update the distances in lateral coordiantes
        dx2d = x2d - x2d_s_in_m
        dy2d = y2d - y2d_s_in_m
        rms_dxy = np.sqrt(np.nanmean((dx2d.flatten()**2 + dy2d.flatten()**2)))

    return z2d


def generate_2d_curved_surface_height(standard_height_function: types.FunctionType,
                                        x2d: np.ndarray,
                                        y2d: np.ndarray,
                                        p: float,
                                        q: float,
                                        theta: float,
                                        x_i: float,
                                        y_i: float,
                                        z_i: float,
                                        alpha: float,
                                        beta: float,
                                        gamma: float,
                                        z2d_measured: np.ndarray = None):

    """
    Geneate 2D curved surface height map with (``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``)

    Parameters
    ----------
        standard_height_function: `function`
            The standard height function
        x2d: `numpy.ndarray`
            The 2D x coordinates
        y2d: `numpy.ndarray`
            The 2D y coordinates
        p: `float`
            The ``p`` value: the distance from the source to the chief ray intersection
        q: `float`
            The ``q`` value: the distance from the chief ray intersection to the focus
        theta: `float`
            The grazing angle
        alpha: `float`
            The angle around x-axis
        beta: `float`
            The angle around y-axis
        gamma: `float`
            The angle around z-axis
        x_i: `float`
            x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
        y_i: `float`
            y-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the y-position of chief ray intersection in metrology coordinates
        z_i: `float`
            z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
        z2d_measured: `numpy.ndarray`
            The measured height map

    Returns
    -------
        z2d: `numpy.ndarray`
            The height map
    """

    if z2d_measured is None:
        z2d_measured = np.zeros(x2d.shape)

    tf = compose_transformation_matrix(alpha, beta, gamma, x_i, y_i, z_i)
    z2d = iter_generate_height(standard_height_function, x2d, y2d, p, q, theta, tf, z2d_measured)

    return z2d



def generate_2d_cylinder_height(standard_height_function: types.FunctionType,
                                x2d: np.ndarray,
                                y2d: np.ndarray,
                                p: float,
                                q: float,
                                theta: float,
                                x_i: float,
                                z_i: float,
                                alpha: float,
                                beta: float,
                                gamma: float,
                                z2d_measured: np.ndarray = None):

    """
    Geneate 2D cylinder surface height map with (``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``)


    Parameters
    ----------
        standard_height_function: `function`
            The standard height function
        x2d: `numpy.ndarray`
            The 2D x coordinates
        y2d: `numpy.ndarray`
            The 2D y coordinates
        p: `float`
            The ``p`` value: the distance from the source to the chief ray intersection
        q: `float`
            The ``q`` value: the distance from the chief ray intersection to the focus
        theta: `float`
            The grazing angle
        alpha: `float`
            The angle around x-axis
        beta: `float`
            The angle around y-axis
        gamma: `float`
            The angle around z-axis
        x_i: `float`
            x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
        z_i: `float`
            z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
        z2d_measured: `numpy.ndarray`
            The measured height map

    Returns
    -------
        z2d: `numpy.ndarray`
            The height map
    """

    if z2d_measured is None:
        z2d_measured = np.zeros(x2d.shape)

    y_i = 0 # No need to consider y-position of the chief ray intersection for cylinders
    tf = compose_transformation_matrix(alpha, beta, gamma, x_i, y_i, z_i)
    z2d = iter_generate_height(standard_height_function, x2d, y2d, p, q, theta, tf, z2d_measured)

    return z2d

def generate_1d_height(standard_height_function: types.FunctionType,
                        x1d: np.array,
                        p: float,
                        q: float,
                        theta: float,
                        x_i: float,
                        z_i: float,
                        beta: float,
                        z1d_measured: np.array = None):
    """
    Geneate 1D height map with (``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``)


    Parameters
    ----------
        standard_height_function: `function`
            The standard height function
        x1d: `numpy.ndarray`
            The 1D x coordinates
        p: `float`
            The ``p`` value: the distance from the source to the chief ray intersection
        q: `float`
            The ``q`` value: the distance from the chief ray intersection to the focus
        theta: `float`
            The grazing angle
        alpha: `float`
            The angle around x-axis
        beta: `float`
            The angle around y-axis
        gamma: `float`
            The angle around z-axis
        x_i: `float`
            x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
        z_i: `float`
            z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
        z1d_measured: `numpy.ndarray`
            The measured height map

    Returns
    -------
        z1d: `numpy.ndarray`
            The height map
    """
    
    if z1d_measured is None:
        z1d_measured = np.zeros_like(x1d)

    y_i = 0 # No need to consider y-position of the chief ray intersection for cylinders
    alpha = 0 # No need to consider rotation along x-axis for 1D case
    gamma = 0 # No need to consider rotation along z-axis for 1D case
    tf = compose_transformation_matrix(alpha, beta, gamma, x_i, y_i, z_i)

    y1d = np.zeros_like(x1d) # No need to consider y-coordiantes in metrology coordinates
    z1d = iter_generate_height(standard_height_function, x1d, y1d, p, q, theta, tf, z1d_measured)
    return z1d

def generate_1d_slope(standard_slope_function: types.FunctionType, 
                      x1d: np.array, 
                      p: float, 
                      q: float, 
                      theta: float, 
                      x_i: float, 
                      beta: float):
    """
    Generate 1D slope map with (``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``)

    Parameters
    ----------
        standard_slope_function: `function`
            The standard slope function
        x1d: `numpy.ndarray`
            The 1D x coordinates
        p: `float`
            The ``p`` value: the distance from the source to the chief ray intersection
        q: `float`
            The ``q`` value: the distance from the chief ray intersection to the focus
        theta: `float`
            The grazing angle
        alpha: `float`
            The angle around x-axis
        beta: `float`
            The angle around y-axis
        gamma: `float`
            The angle around z-axis
        x_i: `float`
            x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
        sx1d_measured: `numpy.ndarray`
            The measured slope map

    Returns
    -------
        sx1d: `numpy.ndarray`
            The slope map
    """

    x1d = x1d - x_i
    sx1d = standard_slope_function(x1d, p, q, theta)
    sx1d = sx1d - np.tan(beta) # Note: the direction of beta
    return sx1d

