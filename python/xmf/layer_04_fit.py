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
from scipy.optimize import leastsq
from scipy.linalg import svd, lstsq
import scipy.fftpack as fftpack
from scipy.io import loadmat
from scipy import ndimage, sparse
from scipy.sparse.linalg import lsqr, lsmr, spsolve
from scipy import integrate
import lmfit
import h5py

def standard_quadrics_height(x2d: np.ndarray,
                             y2d: np.ndarray,
                             p: float,
                             q: float,
                             theta: float,
                             return_z2d_expression_as_extra: bool = False):
    """
    The standard quadrics height with (``p``, ``q``, ``theta``)

    Parameters
    ----------
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
        return_z2d_expression_as_extra: `bool`
            If True, return the z2d_expression as well
    Returns
    -------
        z2d_quad_sln: `numpy.ndarray`
            The 2D height map
    """

    def quad_sln(x2d: np.ndarray,
                y2d: np.ndarray,
                p: float,
                q: float,
                theta: float):

        # Parameters
        A = (p+q)**2 - (p-q)**2*np.sin(theta)**2
        B = 2*x2d*(p+q)*(p-q)*np.sin(theta)*np.cos(theta) - 4*p*q*(p+q)*np.sin(theta)
        C = (p+q)**2*(x2d**2*np.sin(theta)**2 + y2d**2)

        # Discriminant
        Delta = B**2 - 4*A*C

        # Check (p, q) conditions
        if (p < 0 and q < 0): # Top (convex) ellipsoid
            z2d_quad_sln = (-B + np.sqrt(Delta))/(2*A)
        elif (p > 0 and q > 0): # Bottom (concave) ellipsoid
            z2d_quad_sln = (-B - np.sqrt(Delta))/(2*A)
        elif (p < 0 and q > 0): # Left hyperboloid
            if (abs(p) <= abs(q)): # Left convex hyperboloid
                z2d_quad_sln = (-B + np.sqrt(Delta))/(2*A)
            else: # Left concave hyperboloid
                z2d_quad_sln = (-B - np.sqrt(Delta))/(2*A)
        elif (p > 0 and q < 0): # Right hyperboloid
            if (abs(p) >= abs(q)): # Right convex hyperboloid
                z2d_quad_sln = (-B + np.sqrt(Delta))/(2*A)
            else: # Right concave hyperboloid
                z2d_quad_sln = (-B - np.sqrt(Delta))/(2*A)

        z2d_quad_sln[Delta<0] = np.nan

        return z2d_quad_sln

    def expression(x2d: np.ndarray,
                              y2d: np.ndarray,
                              p: float,
                              q: float,
                              theta: float):
        if (p*q>0): # Ellipsoid
            z2d_expression = (p+q)*np.sin(theta)*(-x2d*(p-q)*np.cos(theta) + 2*p*q - np.sqrt(-4*p*q*x2d**2 - 4*p*q*(p-q)*x2d*np.cos(theta) + 4*p**2*q**2 - ((p+q)**2-(p-q)**2*np.sin(theta)**2)*y2d**2/np.sin(theta)**2))/((p+q)**2-(p-q)**2*np.sin(theta)**2)
        elif (p*q < 0): # Hyperboloid
            z2d_expression = (p+q)*np.sin(theta)*(-x2d*(p-q)*np.cos(theta) + 2*p*q + np.sqrt(-4*p*q*x2d**2 - 4*p*q*(p-q)*x2d*np.cos(theta) + 4*p**2*q**2 - ((p+q)**2-(p-q)**2*np.sin(theta)**2)*y2d**2/np.sin(theta)**2))/((p+q)**2-(p-q)**2*np.sin(theta)**2)

        z2d_expression[np.imag(z2d_expression)!=0] = np.nan

        return z2d_expression

    z2d_quad_sln = quad_sln(x2d, y2d, p, q, theta)
    
    if return_z2d_expression_as_extra:
        z2d_expression = expression(x2d, y2d, p, q, theta)
        return (z2d_quad_sln, z2d_expression)
    else:
        return z2d_quad_sln


def standard_convex_ellipsoid_height(x2d: np.ndarray,
                                     y2d: np.ndarray,
                                     abs_p: float,
                                     abs_q: float,
                                     theta: float,
                                     return_z2d_expression_as_extra: bool = False):
    """
    The standard 2D convex ellipsoid height with (``abs_p``, ``abs_q``, ``theta``)

    Parameters
    ----------
        x2d: `numpy.ndarray`
            The 2D x coordinates
        y2d: `numpy.ndarray`
            The 2D y coordinates
        abs_p: `float`
            The ``abs_p`` value: the absolute value of the distance between the source and the chief ray intersection
        abs_q: `float`
            The ``abs_q`` value: the absolute value of the distance between the chief ray intersection and the focus
        theta: `float`
            The grazing angle
        return_z2d_expression_as_extra: `bool`
            If True, return the z2d_expression as well
    Returns
    -------
        z2d: `numpy.ndarray`
            The 2D height map
    """

    # Give the sign to p and q based on mirror type
    p = -abs_p
    q = -abs_q
    return standard_quadrics_height(x2d, y2d, p, q, theta, return_z2d_expression_as_extra)
    
    
def standard_concave_ellipsoid_height(x2d: np.ndarray,
                                      y2d: np.ndarray,
                                      abs_p: float,
                                      abs_q: float,
                                      theta: float,
                                      return_z2d_expression_as_extra: bool = False):
    """
    The standard 2D concave ellipsoid height with (``abs_p``, ``abs_q``, ``theta``)

    Parameters
    ----------
        x2d: `numpy.ndarray`
            The 2D x coordinates
        y2d: `numpy.ndarray`
            The 2D y coordinates
        abs_p: `float`
            The ``abs_p`` value: the absolute value of the distance between the source and the chief ray intersection
        abs_q: `float`
            The ``abs_q`` value: the absolute value of the distance between the chief ray intersection and the focus
        theta: `float`
            The grazing angle
        return_z2d_expression_as_extra: `bool`
            If True, return the z2d_expression as well
    Returns
    -------
        z2d: `numpy.ndarray`
            The 2D height map
    """

    # Give the sign to p and q based on mirror type
    p = abs_p
    q = abs_q
    return standard_quadrics_height(x2d, y2d, p, q, theta, return_z2d_expression_as_extra)

def standard_convex_hyperboloid_height(x2d: np.ndarray,
                                       y2d: np.ndarray,
                                       abs_p: float,
                                       abs_q: float,
                                       theta: float,
                                       return_z2d_expression_as_extra: bool = False):
    """
    The standard 2D convex hyperboloid height with (``abs_p``, ``abs_q``, ``theta``)

    Parameters
    ----------
        x2d: `numpy.ndarray`
            The 2D x coordinates
        y2d: `numpy.ndarray`
            The 2D y coordinates
        abs_p: `float`
            The ``abs_p`` value: the absolute value of the distance between the source and the chief ray intersection
        abs_q: `float`
            The ``abs_q`` value: the absolute value of the distance between the chief ray intersection and the focus
        theta: `float`
            The grazing angle
        return_z2d_expression_as_extra: `bool`
            If True, return the z2d_expression as well
    Returns
    -------
        z2d: `numpy.ndarray`
            The 2D height map
    """

    # Give the sign to p and q based on mirror type
    if (abs_p > abs_q):
        p = abs_p
        q = - abs_q
    else:
        p = - abs_p
        q = abs_q

    return standard_quadrics_height(x2d, y2d, p, q, theta, return_z2d_expression_as_extra)

def standard_concave_hyperboloid_height(x2d: np.ndarray,
                                        y2d: np.ndarray,
                                        abs_p: float,
                                        abs_q: float,
                                        theta: float,
                                        return_z2d_expression_as_extra: bool = False):
    """
    The standard 2D concave hyperboloid height with (``abs_p``, ``abs_q``, ``theta``)

    Parameters
    ----------
        x2d: `numpy.ndarray`
            The 2D x coordinates
        y2d: `numpy.ndarray`
            The 2D y coordinates
        abs_p: `float`
            The ``abs_p`` value: the absolute value of the distance between the source and the chief ray intersection
        abs_q: `float`
            The ``abs_q`` value: the absolute value of the distance between the chief ray intersection and the focus
        theta: `float`
            The grazing angle
        return_z2d_expression_as_extra: `bool`
            If True, return the z2d_expression as well
    Returns
    -------
        z2d: `numpy.ndarray`
            The 2D height map
    """

    # Give the sign to p and q based on mirror type
    if (abs_p > abs_q):
        p = - abs_p
        q = abs_q
    else:
        p = abs_p
        q = - abs_q

    return standard_quadrics_height(x2d, y2d, p, q, theta, return_z2d_expression_as_extra)

def standard_quadric_cylinder_height(x: np.ndarray,
                                     p: float,
                                     q: float,
                                     theta: float,
                                     return_z_expression_as_extra: bool = False):
    """
    The standard quadric cylinder height with (``p``, ``q``, ``theta``)

    Parameters
    ----------
        x: `numpy.ndarray`
            The x coordinates
        p: `float`
            The ``p`` value: the distance from the source to the chief ray intersection
        q: `float`
            The ``q`` value: the distance from the chief ray intersection to the focus
        theta: `float`
            The grazing angle
        return_z_expression_as_extra: `bool`
            If True, return the z_expression as well
    Returns
    -------
        z: `numpy.ndarray`
            The height
    """

    # Quadratic solution.......................................................
    def quad_sln(x: np.ndarray,
                 p: float,
                 q: float,
                 theta: float):

        A = (p+q)**2 - (p-q)**2*np.sin(theta)**2
        B = 2*x*(p+q)*(p-q)*np.sin(theta)*np.cos(theta) - 4*p*q*(p+q)*np.sin(theta)
        C = (p+q)**2*(x**2*np.sin(theta)**2)

        # Discriminant
        Delta = B**2 - 4*A*C

        if (p < 0 and q < 0): # Top (convex) elliptic cylinder
            z_quad_sln = (-B + np.sqrt(Delta))/(2*A)
        elif (p > 0 and q > 0): # Bottom (concave) elliptic cylinder
            z_quad_sln = (-B - np.sqrt(Delta))/(2*A)
        elif (p < 0 and q > 0): # Left hyperbolic cylinder
            if (abs(p) <= abs(q)): # Left convex hyperbolic cylinder
                z_quad_sln = (-B + np.sqrt(Delta))/(2*A)
            else: # Left concave hyperbolic cylinder
                z_quad_sln = (-B - np.sqrt(Delta))/(2*A)
        elif (p > 0 and q < 0): # Right hyperbolic cylinder
            if (abs(p) >= abs(q)): # Right convex hyperbolic cylinder
                z_quad_sln = (-B + np.sqrt(Delta))/(2*A)
            else: # Right concave hyperbolic cylinder
                z_quad_sln = (-B - np.sqrt(Delta))/(2*A)

        z_quad_sln[Delta<0] = np.nan

        return z_quad_sln

    # Expression .......................................................
    def expression(x: np.ndarray,
                   p: float,
                   q: float,
                   theta: float):
        if (p*q>0): # Elliptical cylinder
            z_expression = (p+q)*np.sin(theta)*(-x*(p-q)*np.cos(theta) + 2*p*q - np.sqrt(-4*p*q*x**2 - 4*p*q*(p-q)*x*np.cos(theta) + 4*p**2*q**2))/((p+q)**2-(p-q)**2*np.sin(theta)**2)
        elif (p*q < 0): # Hyperbolic cylinder
            z_expression = (p+q)*np.sin(theta)*(-x*(p-q)*np.cos(theta) + 2*p*q + np.sqrt(-4*p*q*x**2 - 4*p*q*(p-q)*x*np.cos(theta) + 4*p**2*q**2))/((p+q)**2-(p-q)**2*np.sin(theta)**2)

        z_expression[np.imag(z_expression)!=0] = np.nan

        return z_expression

    z_quad_sln = quad_sln(x, p, q, theta)
    
    if return_z_expression_as_extra:
        z_expression = expression(x, p, q, theta)
        return (z_quad_sln, z_expression)
    else:
        return z_quad_sln

def standard_convex_elliptic_cylinder_height(x: np.ndarray,
                                             abs_p: float,
                                             abs_q: float,
                                             theta: float,
                                             return_z_expression_as_extra: bool = False):

    """
    The standard convex elliptic cylinder height with (``abs_p``, ``abs_q``, ``theta``)

    Parameters
    ----------
        x: `numpy.ndarray`
            The x coordinates
        abs_p: `float`
            The ``abs_p`` value: the absolute value of the distance between the source and the chief ray intersection
        abs_q: `float`
            The ``abs_q`` value: the absolute value of the distance between the chief ray intersection and the focus
        theta: `float`
            The grazing angle
        return_z_expression_as_extra: `bool`
            If True, return the z_expression as well
    Returns
    -------
        z: `numpy.ndarray`
            The height
    """

    # Give the sign to p and q based on mirror type
    p = -abs_p
    q = -abs_q

    return standard_quadric_cylinder_height(x, p, q, theta, return_z_expression_as_extra)

def standard_concave_elliptic_cylinder_height(x: np.ndarray,
                                              abs_p: float,
                                              abs_q: float,
                                              theta: float,
                                              return_z_expression_as_extra: bool = False):
    """
    The standard convex elliptic cylinder height with (``abs_p``, ``abs_q``, ``theta``)

    Parameters
    ----------
        x: `numpy.ndarray`
            The x coordinates
        abs_p: `float`
            The ``abs_p`` value: the absolute value of the distance between the source and the chief ray intersection
        abs_q: `float`
            The ``abs_q`` value: the absolute value of the distance between the chief ray intersection and the focus
        theta: `float`
            The grazing angle
        return_z_expression_as_extra: `bool`
            If True, return the z_expression as well
    Returns
    -------
        z2d: `numpy.ndarray`
            The 2D height map
    """

    # Give the sign to p and q based on mirror type
    p = abs_p
    q = abs_q

    return standard_quadric_cylinder_height(x, p, q, theta, return_z_expression_as_extra)

def standard_convex_hyperbolic_cylinder_height(x: np.ndarray,
                                               abs_p: float,
                                               abs_q: float,
                                               theta: float,
                                               return_z_expression_as_extra: bool = False):
    """
    The standard 2D convex hyperbolic height with (``abs_p``, ``abs_q``, ``theta``)

    Parameters
    ----------
        x: `numpy.ndarray`
            The 2D x coordinates
        abs_p: `float`
            The ``abs_p`` value: the absolute value of the distance between the source and the chief ray intersection
        abs_q: `float`
            The ``abs_q`` value: the absolute value of the distance between the chief ray intersection and the focus
        theta: `float`
            The grazing angle
        return_z_expression_as_extra: `bool`
            If True, return the z_expression as well
    Returns
    -------
        z2d: `numpy.ndarray`
            The 2D height map
    """
    if abs(abs_p) > abs(abs_q):
        p = abs_p
        q = - abs_q
    else:
        p = - abs_p
        q = abs_q

    return standard_quadric_cylinder_height(x, p, q, theta, return_z_expression_as_extra)

def standard_concave_hyperbolic_cylinder_height(x: np.ndarray,
                                                abs_p: float,
                                                abs_q: float,
                                                theta: float,
                                                return_z_expression_as_extra: bool = False):

    """
    The standard 2D concave hyperbolic height with (``abs_p``, ``abs_q``, ``theta``)

    Parameters
    ----------
        x: `numpy.ndarray`
            The 2D x coordinates
        abs_p: `float`
            The ``abs_p`` value: the absolute value of the distance between the source and the chief ray intersection
        abs_q: `float`
            The ``abs_q`` value: the absolute value of the distance between the chief ray intersection and the focus
        theta: `float`
            The grazing angle
        return_z_expression_as_extra: `bool`
            If True, return the z_expression as well
    Returns
    -------
        z2d: `numpy.ndarray`
            The 2D height map
    """
    if abs(abs_p) > abs(abs_q):
        p = - abs_p
        q = abs_q
    else:
        p = abs_p
        q = - abs_q

    return standard_quadric_cylinder_height(x, p, q, theta, return_z_expression_as_extra)

def standard_quadric_cylinder_xslope(x: np.ndarray,
                              p: float,
                              q: float,
                              theta: float):

    """
    The standard quadric cylinder slope with (``p``, ``q``, ``theta``)

    Parameters
    ----------
        x: `numpy.ndarray`
            The x coordinates
        p: `float`
            The ``p`` value: the distance from the source to the chief ray intersection
        q: `float`
            The ``q`` value: the distance from the chief ray intersection to the focus
        theta: `float`
            The grazing angle
    Returns
    -------
        sx: `numpy.ndarray`
            The x-slope
    """
    if (p*q>0): # Elliptic cylinder
        sx = (p+q)*np.sin(theta)/((p+q)**2-(p-q)**2*np.sin(theta)**2)*(-(p-q)*np.cos(theta) + (2*p*q*x + p*q*(p-q)*np.cos(theta))/np.sqrt(-p*q*x**2 - p*q*(p-q)*x*np.cos(theta) + p**2*q**2))
    elif (p*q<0): # Hyperbolic cylinder
        sx = (p+q)*np.sin(theta)/((p+q)**2-(p-q)**2*np.sin(theta)**2)*(-(p-q)*np.cos(theta) - (2*p*q*x + p*q*(p-q)*np.cos(theta))/np.sqrt(-p*q*x**2 - p*q*(p-q)*x*np.cos(theta) + p**2*q**2))
    sx[np.imag(sx)!=0] = np.nan

    return sx

def standard_convex_elliptic_cylinder_xslope(x: np.ndarray,
                                             abs_p: float,
                                             abs_q: float,
                                             theta: float):

    """
    The standard convex elliptic cylinder x-slope with (``abs_p``, ``abs_q``, ``theta``)

    Parameters
    ----------
        x: `numpy.ndarray`
            The x coordinates
        abs_p: `float`
            The ``abs_p`` value: the absolute value of the distance between the source and the chief ray intersection
        abs_q: `float`
            The ``abs_q`` value: the absolute value of the distance between the chief ray intersection and the focus
        theta: `float`
            The grazing angle
    Returns
    -------
        sx: `numpy.ndarray`
            The x-slope
    """
    p = - abs_p
    q = - abs_q

    sx_expression_quadrics = standard_quadric_cylinder_xslope(x, p, q, theta)
    return sx_expression_quadrics

def standard_concave_elliptic_cylinder_xslope(x: np.ndarray,
                              abs_p: float,
                              abs_q: float,
                              theta: float):

    """
    The standard concave elliptic cylinder x-slope with (``abs_p``, ``abs_q``, ``theta``)

    Parameters
    ----------
        x: `numpy.ndarray`
            The x coordinates
        abs_p: `float`
            The ``abs_p`` value: the absolute value of the distance between the source and the chief ray intersection
        abs_q: `float`
            The ``abs_q`` value: the absolute value of the distance between the chief ray intersection and the focus
        theta: `float`
            The grazing angle
    Returns
    -------
        sx: `numpy.ndarray`
            The x-slope
    """
    p = abs_p
    q = abs_q
    
    sx_expression_quadrics = standard_quadric_cylinder_xslope(x, p, q, theta)
    return sx_expression_quadrics

def standard_convex_hyperbolic_cylinder_xslope(x: np.ndarray,
                              abs_p: float,
                              abs_q: float,
                              theta: float):

    """
    The standard convex hyperbolic cylinder x-slope with (``abs_p``, ``abs_q``, ``theta``)

    Parameters
    ----------
        x: `numpy.ndarray`
            The x coordinates
        abs_p: `float`
            The ``abs_p`` value: the absolute value of the distance between the source and the chief ray intersection
        abs_q: `float`
            The ``abs_q`` value: the absolute value of the distance between the chief ray intersection and the focus
        theta: `float`
            The grazing angle
    Returns
    -------
        sx: `numpy.ndarray`
            The x-slope
    """
    if abs(abs_p) > abs(abs_q):
        p = abs_p
        q = - abs_q
    else:
        p = - abs_p
        q = abs_q

    sx_expression_quadrics = standard_quadric_cylinder_xslope(x, p, q, theta)
    return sx_expression_quadrics

def standard_concave_hyperbolic_cylinder_xslope(x: np.ndarray,
                              abs_p: float,
                              abs_q: float,
                              theta: float):

    """
    The standard concave hyperbolic cylinder x-slope with (``abs_p``, ``abs_q``, ``theta``)

    Parameters
    ----------
        x: `numpy.ndarray`
            The x coordinates
        abs_p: `float`
            The ``abs_p`` value: the absolute value of the distance between the source and the chief ray intersection
        abs_q: `float`
            The ``abs_q`` value: the absolute value of the distance between the chief ray intersection and the focus
        theta: `float`
            The grazing angle
    Returns
    -------
        sx: `numpy.ndarray`
            The x-slope
    """
    if abs(abs_p) > abs(abs_q):
        p = - abs_p
        q = abs_q
    else:
        p = abs_p
        q = - abs_q

    sx_expression_quadrics = standard_quadric_cylinder_xslope(x, p, q, theta)
    return sx_expression_quadrics


def standard_sag_col_diaboloid_height(x2d: np.ndarray,
                                      y2d: np.ndarray,
                                      abs_p: float,
                                      abs_q: float,
                                      theta: float):

    """
    The standard sagittally collimated diaboloid with (``abs_p``, ``abs_q``, ``theta``)

    Parameters
    ----------
        x2d: `numpy.ndarray`
            The x coordinates
        y2d: `numpy.ndarray`
            The y coordinates
        abs_p: `float`
            The ``abs_p`` value: the absolute value of the distance between the source and the chief ray intersection
        abs_q: `float`
            The ``abs_q`` value: the absolute value of the distance between the chief ray intersection and the focus
        theta: `float`
            The grazing angle
    Returns
    -------
        z2d: `numpy.ndarray`
            The 2D height
    """
    
    # Quadratic solution

    A = (abs_p-abs_q)**2*np.cos(theta)**2 + 4*abs_p*abs_q
    B = (abs_p-abs_q)*np.sin(theta)*y2d**2 + (abs_p**2-abs_q**2)*np.sin(2*theta)*x2d - 4*(abs_p+abs_q)*abs_p*abs_q*np.sin(theta)
    C = (abs_p+abs_q)**2*np.sin(theta)**2*x2d**2 - (abs_p+abs_q)*(np.cos(theta)*x2d - abs_q)*y2d**2 - 0.25*y2d**4

    # Discriminant 
    Delta = B**2 - 4*A*C

    z2d = (-B - np.sqrt(Delta))/(2*A)
    z2d[Delta<0] = np.nan  

    return z2d

def standard_tan_col_diaboloid_height(x2d: np.ndarray,
                                      y2d: np.ndarray,
                                      abs_p: float,
                                      abs_q: float,
                                      theta: float):

    """
    The standard tangentially collimated diaboloid with (``abs_p``, ``abs_q``, ``theta``)

    Parameters
    ----------
        x2d: `numpy.ndarray`
            The x coordinates
        y2d: `numpy.ndarray`
            The y coordinates
        abs_p: `float`
            The ``abs_p`` value: the absolute value of the distance between the source and the chief ray intersection
        abs_q: `float`
            The ``abs_q`` value: the absolute value of the distance between the chief ray intersection and the focus
        theta: `float`
            The grazing angle
    Returns
    -------
        z2d: `numpy.ndarray`
            The 2D height
    """
    
    A = - np.cos(theta)**4
    B = 4*(abs_p-abs_q)*np.cos(theta)**2*np.sin(theta) + 4 *np.cos(theta)**3*np.sin(theta)*x2d
    C = 4*abs_q*((abs_p+abs_q)*np.cos(theta)**2 + 4*abs_p*np.sin(theta)**2) + 2*np.cos(theta)*(abs_q - 3*abs_p + (abs_p-3*abs_q)*np.cos(2*theta))*x2d - 6*np.cos(theta)**2*np.sin(theta)**2*x2d**2
    D = -16*abs_p*abs_q*(abs_p+abs_q)*np.sin(theta) + 4*(abs_p+abs_q)*(2*abs_p-abs_q)*np.sin(2*theta)*x2d + 2*(3*abs_p+abs_q+(3*abs_q+abs_p)*np.cos(2*theta))*np.sin(theta)*x2d**2 + 4*np.cos(theta)*np.sin(theta)**3*x2d**3
    E = 4*(abs_p+abs_q)**2*y2d**2 + 4*abs_q*(abs_p+abs_q)*np.sin(theta)**2*x2d**2 - 4*(abs_p+abs_q)*np.cos(theta)*np.sin(theta)**2*x2d**3 - np.sin(theta)**4*x2d**4

    b = B/A
    c = C/A
    d = D/A
    e = E/A

    k = (8*c-3*b**2)/8
    m = (b**3-4*b*c+8*d)/8

    Delta_0 = c**2 - 3*b*d + 12*e
    Delta_1 = 2*c**3 - 9*b*c*d + 27*b**2*e + 27*d**2 - 72*c*e

    mask = Delta_1**2 - 4*Delta_0**3 >= 0

    # Solve the equation
    # Note: the expression of Q in the reference paper was wrong.
    Q = 0.5**(1/3)*(Delta_1 + np.sqrt(Delta_1**2 - 4*Delta_0**3, dtype=complex))**(1/3) 
    S1 = np.real(0.5*np.sqrt((1/3)*(Q + Delta_0/Q) - 2/3*k))

    # Another way to avoid the complex number Q,
    # when Delta_1**2 - 4*Delta_0**3<0
    # Source: https://en.wikipedia.org/wiki/Quartic_function#
    phi = np.arccos(Delta_1 / (2 * np.sqrt(Delta_0**3, dtype=complex)))
    S2 = np.real(0.5*np.sqrt(- 2/3*k + 2/3*np.sqrt(Delta_0, dtype=complex)*np.cos(phi/3), dtype=complex))

    S = mask*S1 + np.logical_not(mask)*S2  
    # S = np.zeros_like(S1)
    # S[mask] = S1[mask]
    # S[np.logical_not(mask)] = S2[np.logical_not(mask)]
    
    z2d = -b/4 - S + 0.5*np.sqrt(-4*S**2 - 2*k + m/S)

    return z2d


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


def iter_generate_height(standard_height_function_handle,
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
        standard_height_function_handle:
            handle of the standard height function
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
            z2d_s = np.real(standard_height_function_handle(x2d_s, y2d_s, p, q, theta)) # 2D curved shape
        except TypeError:
            z2d_s = np.real(standard_height_function_handle(x2d_s, p, q, theta)) # 1D or 2D cylinder
            z2d_s = np.real(standard_height_function_handle(x2d_s, y2d_s, p, q, theta)) # 2D curved shape
        except ValueError:
            z2d_s = np.real(standard_height_function_handle(x2d_s, p, q, theta)) # 1D or 2D cylinder
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


def generate_2d_curved_surface_height(standard_height_function_handle,
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
        standard_height_function_handle:
            handle of the standard height function
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
    z2d = iter_generate_height(standard_height_function_handle, x2d, y2d, p, q, theta, tf, z2d_measured)

    return z2d



def generate_2d_cylinder_height(standard_height_function_handle,
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
        standard_height_function_handle:
            handle of the standard height function
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
    z2d = iter_generate_height(standard_height_function_handle, x2d, y2d, p, q, theta, tf, z2d_measured)

    return z2d

def generate_1d_height(standard_height_function_handle,
                        x1d: np.array,
                        p: float,
                        q: float,
                        theta: float,
                        x_i: float,
                        z_i: float,
                        beta: float,
                        z1d_measured: np.array = None):
    if z1d_measured is None:
        z1d_measured = np.zeros_like(x1d)

    y_i = 0 # No need to consider y-position of the chief ray intersection for cylinders
    alpha = 0 # No need to consider rotation along x-axis for 1D case
    gamma = 0 # No need to consider rotation along z-axis for 1D case
    tf = compose_transformation_matrix(alpha, beta, gamma, x_i, y_i, z_i)

    y1d = np.zeros_like(x1d) # No need to consider y-coordiantes in metrology coordinates
    z1d = iter_generate_height(standard_height_function_handle, x1d, y1d, p, q, theta, tf, z1d_measured)
    return z1d

def generate_1d_slope(standard_slope_function_handle, 
                      x1d: np.array, 
                      p: float, 
                      q: float, 
                      theta: float, 
                      x_i: float, 
                      beta: float):

    x1d = x1d - x_i
    sx1d = standard_slope_function_handle(x1d, p, q, theta)
    sx1d = sx1d + np.tan(beta)
    return sx1d


def optimize_parameters(surface_generation_function_handle, 
                        standard_surface_shape_function_handle, 
                        x: np.array, 
                        y: np.array, 
                        v: np.array, 
                        input_params_dict: dict, 
                        is_opt_dict: dict,
                        is_lmfit: bool = True):
    """
    Basic function to provide a convenient way to optimize the surface parameters with measurement results.

    Parameters
    ----------
        surface_generation_function_handle: `function`
            The function to generate surface (1D or 2D, slope or height)
        standard_surface_shape_function_handle: `function` 
            The function handle for a standard surface shape 
        x: `numpy.ndarray`
            The measured x-coordinate in in unit of [m] as a suggestion
        y: `numpy.ndarray`
            The measured y-coordinate in in unit of [m] as a suggestion
        v: `numpy.ndarray`
            The measured slope or height in [rad] or [m] as a suggestion
        input_params_dict: `dict`
            The ``p``, ``q``, ``theta``, ``x_i``(optional), ``y_i``(optional), 
            ``z_i``(optional), ``alpha``(optional), ``beta``(optional) and 
            ``gamma``(optional) target parameters, suggested in unit of 
            [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
        is_opt_dict: `dict`
            The structure to set whether optimization is needed for 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``.
        is_lmfit: `bool`
            The flag to identify if using lmfit module to implement the optimization.

    Returns
    -------
        v_res:`numpy.ndarray`
            The residual (1D or 2D)
        v_fit: `numpy.ndarray`
            The fitting result (1D or 2D)
        param_opt_dict: `dict`
            The optimized parameters in dictionary
        is_optimized_dict: `dict`
            The dictionary to indicate which parameters are optimized
    """

    # Set parameters...........................................................
    # Check input parameters...................................................
    def check_input_params(input_params_dict, x, y, v):
        if 'p' in input_params_dict:
            p = input_params_dict['p'] # [m]
        else:
            raise ValueError("p value must be in param_inputs.")

        if 'q' in input_params_dict:
            q = input_params_dict['q'] # [m]
        else:
            raise ValueError("q value must be in param_inputs.")

        if 'theta' in input_params_dict:
            theta = input_params_dict['theta'] # [m]
        else:
            raise ValueError("theta value must be in param_inputs.")

        if 'x_i' in input_params_dict:
            x_i = input_params_dict['x_i'] # [m]
        else:
            x_i = np.nanmean(x[np.isfinite(v)]) # [m]

        if 'y_i' in input_params_dict:
            y_i = input_params_dict['y_i'] # [m]
        else:
            y_i = np.nanmean(y[np.isfinite(v)]) # [m]

        if 'z_i' in input_params_dict:
            z_i = input_params_dict['z_i'] # [m]
        else:
            z_i = 0

        if 'alpha' in input_params_dict:
            alpha = input_params_dict['alpha'] # [rad]
        else:
            alpha = 0 # [rad]

        if 'beta' in input_params_dict:
            beta = input_params_dict['beta'] # [rad]
        else:
            beta = 0 # [rad]

        if 'gamma' in input_params_dict:
            gamma = input_params_dict['gamma'] # [rad]
        else:
            gamma = 0 # [rad]

        # Initial values
        param_init = np.array([p, q, theta, x_i, y_i, z_i, alpha, beta, gamma])

        return param_init

    def check_is_opt(is_opt_dict, surface_generation_function_handle): 
        is_opt_vector = np.zeros(9, dtype=bool)

        if surface_generation_function_handle == generate_2d_curved_surface_height:
            is_opt_vector[3:] = True # x_i, y_i, z_i, alpha, beta, gamma
        elif surface_generation_function_handle == generate_2d_cylinder_height:
            is_opt_vector[3] = True # x_i
            is_opt_vector[5] = True # z_i
            is_opt_vector[6:] = True # alpha, beta, gamma
        elif surface_generation_function_handle == generate_1d_height:
            is_opt_vector[3] = True # x_i
            is_opt_vector[5] = True # z_i
            is_opt_vector[7] = True # beta
        elif surface_generation_function_handle == generate_1d_slope:
            is_opt_vector[3] = True # x_i
            is_opt_vector[7] = True # beta

        # Update the user defined optimization flags
        if 'p' in is_opt_dict: is_opt_vector[0] = is_opt_dict['p']
        if 'q' in is_opt_dict: is_opt_vector[1] = is_opt_dict['q']
        if 'theta' in is_opt_dict: is_opt_vector[2] = is_opt_dict['theta']
        if 'x_i' in is_opt_dict: is_opt_vector[3] = is_opt_dict['x_i']
        if 'y_i' in is_opt_dict: is_opt_vector[4] = is_opt_dict['y_i']
        if 'z_i' in is_opt_dict: is_opt_vector[5] = is_opt_dict['z_i']
        if 'alpha' in is_opt_dict: is_opt_vector[6] = is_opt_dict['alpha']
        if 'beta' in is_opt_dict: is_opt_vector[7] = is_opt_dict['beta']
        if 'gamma' in is_opt_dict: is_opt_vector[8] = is_opt_dict['gamma']

        return is_opt_vector

    # Initial values
    param_init = check_input_params(input_params_dict, x, y, v)

    # Optimization flags
    is_opt_vector = check_is_opt(is_opt_dict, surface_generation_function_handle)

    # Use NaN to identify the parameters which are required to optimize
    param_fix = param_init.copy()
    param_fix[is_opt_vector] = np.nan
    param = param_init[is_opt_vector] # Only optimize parameters required to optimize

    # Common cost function for optimization...........................................
    def common_cost_function_for_optimization(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, param_fix, param):
        #
        # param_fix is the list of fixed parameters, and param is the list of
        # parametres to optimize. It is important to have them always in the same
        # order as p, q, theta, x_i, y_i, z_i, alpha, beta, gamma.
        # The optimized parameters are those set as NaN.

        # returns v1d_valid_res, v_fit, v_res

        # Update parameters which need optimization................................
        param_update = param_fix.copy()
        param_update[np.isnan(param_fix)] = param

        # Release the input parameters.............................................
        p, q, theta, x_i, y_i, z_i, alpha, beta, gamma = param_update

        # Generate surface height with (p, q, theta),
        # considering tranformation with x_i, y_i, z_i, alpha, beta, gamma.........
        if surface_generation_function_handle == generate_2d_curved_surface_height:
            v_fit = surface_generation_function_handle(standard_surface_shape_function_handle, x, y, p, q, theta, x_i, y_i, z_i, alpha, beta, gamma, v)
        elif surface_generation_function_handle == generate_2d_cylinder_height:
            v_fit = surface_generation_function_handle(standard_surface_shape_function_handle, x, y, p, q, theta, x_i, z_i, alpha, beta, gamma, v)
        elif surface_generation_function_handle == generate_1d_height:
            v_fit = surface_generation_function_handle(standard_surface_shape_function_handle, x, p, q, theta, x_i, z_i, beta, v)
        elif surface_generation_function_handle == generate_1d_slope:
            v_fit = surface_generation_function_handle(standard_surface_shape_function_handle, x, p, q, theta, x_i, beta)

        # Calculte the valid residual height as the output of the cost function....
        v_res = v - v_fit
        v1d_valid_res = v_res[np.isfinite(v_res)]

        return v1d_valid_res, v_fit, v_res


    if is_lmfit: # fit with lmfit
  
        p, q, theta, x_i, y_i, z_i, alpha, beta, gamma = param_init

        lmfit_pars = lmfit.Parameters()
        if is_opt_vector[0]:
            lmfit_pars.add('p', value=p)
        if is_opt_vector[1]:
            lmfit_pars.add('q', value=q)
        if is_opt_vector[2]:
            lmfit_pars.add('theta', value=theta)
        if is_opt_vector[3]:
            lmfit_pars.add('x_i', value=x_i)
        if is_opt_vector[4]:
            lmfit_pars.add('y_i', value=y_i)
        if is_opt_vector[5]:
            lmfit_pars.add('z_i', value=z_i)
        if is_opt_vector[6]:
            lmfit_pars.add('alpha', value=alpha)
        if is_opt_vector[7]:
            lmfit_pars.add('beta', value=beta)
        if is_opt_vector[8]:
            lmfit_pars.add('gamma', value=gamma)

        def cost_func_for_lmfit(lmfit_pars, x, y, v, param_fix):
            """
            Cost function to use lmfit module

            Parameters
            ----------
                lmfit_pars: `lmfit.Parameters`
                    The parmeters object in lmfit
                measurement_data: `numpy.ndarray`
                    The measurement data.
                param_fix: `numpy.ndarray`
                    The fixed parameters

            Returns
            -------
                valid_res: `numpy.ndarray`
                    The valid residuals
            """

            param_list = []
            if np.isnan(param_fix[0]):
                param_list.append(lmfit_pars['p'])
            if np.isnan(param_fix[1]):
                param_list.append(lmfit_pars['q'])
            if np.isnan(param_fix[2]):
                param_list.append(lmfit_pars['theta'])
            if np.isnan(param_fix[3]):
                param_list.append(lmfit_pars['x_i'])
            if np.isnan(param_fix[4]):
                param_list.append(lmfit_pars['y_i'])
            if np.isnan(param_fix[5]):
                param_list.append(lmfit_pars['z_i'])
            if np.isnan(param_fix[6]):
                param_list.append(lmfit_pars['alpha'])
            if np.isnan(param_fix[7]):
                param_list.append(lmfit_pars['beta'])
            if np.isnan(param_fix[8]):
                param_list.append(lmfit_pars['gamma'])
            param = np.array(param_list)

            # Calculate the valid residuals
            valid_res, _, _ = common_cost_function_for_optimization(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, param_fix, param)
            # print(f"Valid residuals: {valid_res}")
            return valid_res

        mini = lmfit.Minimizer(cost_func_for_lmfit,
                               lmfit_pars, fcn_args=(x, y, v, param_fix))
        result = mini.minimize()
        # print(lmfit.fit_report(result.params))
        # lmfit.report_fit(result.params, min_correl=0.5)

        try:
            ci_95_best_95 = lmfit.conf_interval(mini, result, sigmas=(2,))
            # lmfit.printfuncs.report_ci(ci_95_best_95)
            is_ci = True
        except:
            is_ci = False

        lmfit_param_opt_dict = {}
        str_param_name_list = ['p', 'q', 'theta',
                               'x_i', 'y_i', 'z_i', 
                               'alpha', 'beta', 'gamma']
        # Release the optimized values
        for idx, str_param_name in enumerate(str_param_name_list):
            lmfit_param_opt_dict[str_param_name] = result.params[str_param_name].value if is_opt_vector[idx] else param_fix[idx]


        # Release the confidence interval
        for idx, str_param_name in enumerate(str_param_name_list):
            if is_ci:
                lmfit_param_opt_dict['ci_95_' + str_param_name] = \
                    np.array(ci_95_best_95[str_param_name])[(0, 2), 1] if is_opt_vector[idx] \
                    else np.zeros((2,))
            else:
                lmfit_param_opt_dict['ci_95_' + str_param_name] = np.nan

        # Re-calculate the fitting and residual
        param_opt_list = []
        if np.isnan(param_fix[0]):
            param_opt_list.append(lmfit_param_opt_dict['p'])
        if np.isnan(param_fix[1]):
            param_opt_list.append(lmfit_param_opt_dict['q'])
        if np.isnan(param_fix[2]):
            param_opt_list.append(lmfit_param_opt_dict['theta'])
        if np.isnan(param_fix[3]):
            param_opt_list.append(lmfit_param_opt_dict['x_i'])
        if np.isnan(param_fix[4]):
            param_opt_list.append(lmfit_param_opt_dict['y_i'])
        if np.isnan(param_fix[5]):
            param_opt_list.append(lmfit_param_opt_dict['z_i'])
        if np.isnan(param_fix[6]):
            param_opt_list.append(lmfit_param_opt_dict['alpha'])
        if np.isnan(param_fix[7]):
            param_opt_list.append(lmfit_param_opt_dict['beta'])
        if np.isnan(param_fix[8]):
            param_opt_list.append(lmfit_param_opt_dict['gamma'])
        param_opt = np.array(param_opt_list)

        _, v_fit, v_res = common_cost_function_for_optimization(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, param_fix, param_opt)

        param_opt_dict = lmfit_param_opt_dict

    else: # Fit with scipy.optimize.leastsq()
        
        def cost_func_of_leastsq(param, x, y, v, param_fix):
            """
            Cost function to use scipy.optimize.leastsq module

            Parameters
            ----------
                params_dict: `dict`
                    The parmeters in dict
                measurement_data: `numpy.ndarray`
                    The measurement data.
                param_fix: `numpy.ndarray`
                    The fixed parameters

            Returns
            -------
                valid_res: `numpy.ndarray`
                    The valid residuals
            """

            # Calculate the valid residuals
            valid_res, _, _ = common_cost_function_for_optimization(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, param_fix, param)
            return valid_res


        # Only optimize the parameters which are required
        param = param_init[is_opt_vector] + np.ones_like(param_init[is_opt_vector]) * 1e-6 # Add a small value to the initial parameters

        # Optimize with the least squares method
        para = leastsq(cost_func_of_leastsq, param, args=(x, y, v, param_fix))
        
        # Release the result in a structure for better understanding
        param_result = np.copy(param_fix)
        param_result[is_opt_vector] = para[0]  # Optimization result

        leastsq_param_opt_dict = {}
        str_param_name_list = ['p', 'q', 'theta',
                               'x_i', 'y_i', 'z_i', 
                               'alpha', 'beta', 'gamma']
        # Release the optimized values
        for idx, str_param_name in enumerate(str_param_name_list):
            leastsq_param_opt_dict[str_param_name] = param_result[idx] if is_opt_vector[idx] else param_fix[idx]


        # Re-calculate the fitting and residual
        param_opt_list = []
        if np.isnan(param_fix[0]):
            param_opt_list.append(leastsq_param_opt_dict['p'])
        if np.isnan(param_fix[1]):
            param_opt_list.append(leastsq_param_opt_dict['q'])
        if np.isnan(param_fix[2]):
            param_opt_list.append(leastsq_param_opt_dict['theta'])
        if np.isnan(param_fix[3]):
            param_opt_list.append(leastsq_param_opt_dict['x_i'])
        if np.isnan(param_fix[4]):
            param_opt_list.append(leastsq_param_opt_dict['y_i'])
        if np.isnan(param_fix[5]):
            param_opt_list.append(leastsq_param_opt_dict['z_i'])
        if np.isnan(param_fix[6]):
            param_opt_list.append(leastsq_param_opt_dict['alpha'])
        if np.isnan(param_fix[7]):
            param_opt_list.append(leastsq_param_opt_dict['beta'])
        if np.isnan(param_fix[8]):
            param_opt_list.append(leastsq_param_opt_dict['gamma'])
        param_opt = np.array(param_opt_list)

        _, v_fit, v_res = common_cost_function_for_optimization(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, param_fix, param_opt)
        param_opt_dict = leastsq_param_opt_dict
        
    # Update the flags for optimized parameters
    is_optimized_dict = {}
    is_optimized_dict['p']=True if is_opt_vector[0] else False
    is_optimized_dict['q']=True if is_opt_vector[1] else False  
    is_optimized_dict['theta']=True if is_opt_vector[2] else False
    is_optimized_dict['x_i']=True if is_opt_vector[3] else False
    is_optimized_dict['y_i']=True if is_opt_vector[4] else False
    is_optimized_dict['z_i']=True if is_opt_vector[5] else False
    is_optimized_dict['alpha']=True if is_opt_vector[6] else False
    is_optimized_dict['beta']=True if is_opt_vector[7] else False
    is_optimized_dict['gamma']=True if is_opt_vector[8] else False 
        
    return v_res, v_fit, param_opt_dict, is_optimized_dict
    

def fit_convex_ellipsoid_height(x2d: np.ndarray,
                                  y2d: np.ndarray,
                                  z2d: np.ndarray,
                                  pqtxy: np.ndarray,
                                  is_opt_dict: dict,
                                  is_lmfit: bool = True,
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
        is_opt_dict: `dict`
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
        param_opt_dict: `dict`
            The optimized parameters in dictionary
    """

    return optimize_parameters(generate_2d_curved_surface_height, standard_convex_ellipsoid_height, x2d, y2d, z2d, pqtxy, is_opt_dict, is_lmfit)


def fit_concave_ellipsoid_height(x2d: np.ndarray,
                                  y2d: np.ndarray,
                                  z2d: np.ndarray,
                                  pqtxy: np.ndarray,
                                  is_opt_dict: dict,
                                  is_lmfit: bool = True,
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
        is_opt_dict: `dict`
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
        param_opt_dict: `dict`
            The optimized parameters in dictionary
    """

    return optimize_parameters(generate_2d_curved_surface_height, standard_concave_ellipsoid_height, x2d, y2d, z2d, pqtxy, is_opt_dict, is_lmfit)



def fit_convex_elliptic_cylinder_height(x2d: np.ndarray,
                                  y2d: np.ndarray,
                                  z2d: np.ndarray,
                                  pqtx: np.ndarray,
                                  is_opt_dict: dict,
                                  is_lmfit: bool = True,
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
        is_opt_dict: `dict`
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
        param_opt_dict: `dict`
            The optimized parameters in dictionary
    """

    return optimize_parameters(generate_2d_curved_surface_height, standard_convex_elliptic_cylinder_height, x2d, y2d, z2d, pqtx, is_opt_dict, is_lmfit)



def fit_concave_elliptic_cylinder_height(x2d: np.ndarray,
                                  y2d: np.ndarray,
                                  z2d: np.ndarray,
                                  pqtx: np.ndarray,
                                  is_opt_dict: dict,
                                  is_lmfit: bool = True,
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
        is_opt_dict: `dict`
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
        param_opt_dict: `dict`
            The optimized parameters in dictionary
    """

    return optimize_parameters(generate_2d_curved_surface_height, standard_concave_elliptic_cylinder_height, x2d, y2d, z2d, pqtx, is_opt_dict, is_lmfit)


def fit_convex_ellipse_height(x1d: np.ndarray,
                                z1d: np.ndarray,
                                pqtx: np.ndarray,
                                is_opt_dict: dict,
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
        is_opt_dict: `dict`
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
        param_opt_dict: `dict`
            The optimized parameters in dictionary
    """

    y1d = np.zeros_like(x1d)  # No need to consider y-coordinates in metrology coordinates for 1D case

    return optimize_parameters(generate_1d_height, standard_convex_elliptic_cylinder_height, x1d, y1d, z1d, pqtx, is_opt_dict, is_lmfit)

def fit_concave_ellipse_height(x1d: np.ndarray,
                                z1d: np.ndarray,
                                pqtx: np.ndarray,
                                is_opt_dict: dict,
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
        is_opt_dict: `dict`
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
        param_opt_dict: `dict`
            The optimized parameters in dictionary
    """

    y1d = np.zeros_like(x1d)  # No need to consider y-coordinates in metrology coordinates for 1D case

    return optimize_parameters(generate_1d_height, standard_concave_elliptic_cylinder_height, x1d, y1d, z1d, pqtx, is_opt_dict, is_lmfit)

def fit_convex_ellipse_slope(x1d: np.ndarray,
                              sx1d: np.ndarray,
                              pqtx: np.ndarray,
                              is_opt_dict: dict,
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
        is_opt_dict: `dict`
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
        param_opt_dict: `dict`
            The optimized parameters in dictionary
    """

    y1d = np.zeros_like(x1d)

    return optimize_parameters(generate_1d_slope, standard_convex_elliptic_cylinder_xslope, x1d, y1d, sx1d, pqtx, is_opt_dict, is_lmfit)

def fit_concave_ellipse_slope(x1d: np.ndarray,
                               sx1d: np.ndarray,
                               input_params_dict: dict,
                               is_opt_dict: dict,
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
        is_opt_dict: `dict`
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
        param_opt_dict: `dict`
            The optimized parameters in dictionary
    """

    y1d = np.zeros_like(x1d)  # No need to consider y-coordinates in metrology coordinates for 1D case

    return optimize_parameters(generate_1d_slope, standard_concave_elliptic_cylinder_xslope, x1d, y1d, sx1d, input_params_dict, is_opt_dict, is_lmfit)


def fit_convex_hyperboloid_height(x2d: np.ndarray,
                                  y2d: np.ndarray,
                                  z2d: np.ndarray,
                                  pqtxy: np.ndarray,
                                  is_opt_dict: dict,
                                  is_lmfit: bool = True,
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
        is_opt_dict: `dict`
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
        param_opt_dict: `dict`
            The optimized parameters in dictionary
    """

    return optimize_parameters(generate_2d_curved_surface_height, standard_convex_hyperboloid_height, x2d, y2d, z2d, pqtxy, is_opt_dict, is_lmfit)

def fit_concave_hyperboloid_height(x2d: np.ndarray,
                                    y2d: np.ndarray,
                                    z2d: np.ndarray,
                                    pqtxy: np.ndarray,
                                    is_opt_dict: dict,
                                    is_lmfit: bool = True,
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
        is_opt_dict: `dict`
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
        param_opt_dict: `dict`
            The optimized parameters in dictionary
    """

    return optimize_parameters(generate_2d_curved_surface_height, standard_concave_hyperboloid_height, x2d, y2d, z2d, pqtxy, is_opt_dict, is_lmfit)

def fit_convex_hyperbolic_cylinder_height(x2d: np.ndarray,
                                           y2d: np.ndarray,
                                           z2d: np.ndarray,
                                           pqtxy: np.ndarray,
                                           is_opt_dict: dict,
                                           is_lmfit: bool = True,
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
        is_opt_dict: `dict`
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
        param_opt_dict: `dict`
            The optimized parameters in dictionary
    """

    return  optimize_parameters(generate_2d_cylinder_height, standard_convex_hyperbolic_cylinder_height, x2d, y2d, z2d, pqtxy, is_opt_dict, is_lmfit)

def fit_concave_hyperbolic_cylinder_height(x2d: np.ndarray,
                                           y2d: np.ndarray,
                                           z2d: np.ndarray,
                                           pqtxy: np.ndarray,
                                           is_opt_dict: dict,
                                           is_lmfit: bool = True,
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
        is_opt_dict: `dict`
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
        param_opt_dict: `dict`
            The optimized parameters in dictionary
    """

    return  optimize_parameters(generate_2d_cylinder_height, standard_concave_hyperbolic_cylinder_height, x2d, y2d, z2d, pqtxy, is_opt_dict, is_lmfit)

def fit_convex_hyperbola_height(x1d: np.ndarray,
                                 z1d_measured: np.ndarray,
                                 pqtx: np.ndarray,
                                 is_opt_1d_cylinder_height: dict,
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
        is_opt_dict: `dict`
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
        param_opt_dict: `dict`
            The optimized parameters in dictionary
    """

    y1d = np.zeros_like(x1d)  # No need to consider y-coordinates in metrology coordinates for 1D case

    return optimize_parameters(generate_1d_height, standard_convex_hyperbolic_cylinder_height, x1d, y1d, z1d_measured, pqtx, is_opt_1d_cylinder_height, is_lmfit)

def fit_concave_hyperbola_height(x1d: np.ndarray,
                                  z1d_measured: np.ndarray,
                                  pqtx: np.ndarray,
                                  is_opt_1d_cylinder_height: dict,
                                  is_lmfit: bool = True,
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
        is_opt_dict: `dict`
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
        param_opt_dict: `dict`
            The optimized parameters in dictionary
    """

    y1d = np.zeros_like(x1d)  # No need to consider y-coordinates in metrology coordinates for 1D case

    return optimize_parameters(generate_1d_height, standard_concave_hyperbolic_cylinder_height, x1d, y1d, z1d_measured, pqtx, is_opt_1d_cylinder_height, is_lmfit)

def fit_convex_hyperbola_slope(x1d: np.ndarray,
                                sx1d: np.ndarray,
                                pqtx: np.ndarray,
                                is_opt_dict: dict,
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
        is_opt_dict: `dict`
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
        param_opt_dict: `dict`
            The optimized parameters in dictionary
    """

    y1d = np.zeros_like(x1d)  # No need to consider y-coordinates in metrology coordinates for 1D case

    return optimize_parameters(generate_1d_slope, standard_convex_hyperbolic_cylinder_xslope, x1d, y1d, sx1d, pqtx, is_opt_dict, is_lmfit)

def fit_concave_hyperbola_slope(x1d: np.ndarray,
                                 sx1d: np.ndarray,
                                 pqtx: np.ndarray,
                                 is_opt_dict: dict,
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
        is_opt_dict: `dict`
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
        param_opt_dict: `dict`
            The optimized parameters in dictionary
    """

    y1d = np.zeros_like(x1d)  # No need to consider y-coordinates in metrology coordinates for 1D case

    return optimize_parameters(generate_1d_slope, standard_concave_hyperbolic_cylinder_xslope, x1d, y1d, sx1d, pqtx, is_opt_dict, is_lmfit)
