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
        
        
        # Surface normal calculation
        dA_dx = 0
        dA_dy = 0
        dB_dx = 2*(p+q)*(p-q)*np.sin(theta)*np.cos(theta)*z2d_quad_sln
        dB_dy = 0
        dC_dx = 2*(p+q)**2*x2d*np.sin(theta)**2
        dC_dy = 2*(p+q)**2*y2d
        
        # Surface normal
        df_dx = dA_dx + dB_dx + dC_dx
        df_dy = dA_dy + dB_dy + dC_dy
        df_dz = 2*A*z2d_quad_sln + B
        
        norm = np.sqrt(df_dx**2 + df_dy**2 + df_dz**2)
        if np.any(norm == 0):
            raise ValueError("The normal vector has zero length, which may indicate a singularity in the surface.")
        nx = df_dx / norm
        ny = df_dy / norm
        nz = df_dz / norm

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
                                      theta: float,
                                      ):

    """
    The standard sagittal collimated diaboloid with (``abs_p``, ``abs_q``, ``theta``)

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

    z_quad_sln = (-B - np.sqrt(Delta))/(2*A)
    z_quad_sln[Delta<0] = np.nan  

    return z_quad_sln


def standard_tan_col_diaboloid_height(x2d: np.ndarray,
                                      y2d: np.ndarray,
                                      abs_p: float,
                                      abs_q: float,
                                      theta: float,
                                      ):

    """
    The standard tangential collimated diaboloid with (``abs_p``, ``abs_q``, ``theta``)

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
    B = 4*(abs_p-abs_q)*np.cos(theta)**2*np.sin(theta) + 4*np.cos(theta)**3*np.sin(theta)*x2d
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