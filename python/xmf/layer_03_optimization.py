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
from scipy.optimize import least_squares

from xmf.layer_02_generation import (
    generate_1d_height,
    generate_1d_slope,
    generate_2d_curved_surface_height,
    generate_2d_cylinder_height,
)

def optimize_parameters(surface_generation_function_handle, 
                        standard_surface_shape_function_handle, 
                        x: np.array, 
                        y: np.array, 
                        v: np.array, 
                        input_params_dict: dict, 
                        opt_or_tol_dict: dict,
                        ):
    """
    Basic function to provide a convenient way to optimize the surface parameters.

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
        opt_or_tol_dict: `dict`
            The structure to set whether optimization is needed for 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``.

    Returns
    -------
        v_res: `numpy.ndarray`
            The residual (1D or 2D)
        v_fit: `numpy.ndarray`
            The fitting result (1D or 2D)
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
        init_params: `numpy.ndarray`
            The used initial parameters.
    """

    if isinstance(opt_or_tol_dict['p'], bool): # Use opt_dict

        v_res, v_fit, opt_params_dict, opt_params_ci_dict, init_params = optimize_parameters_with_opt(
            surface_generation_function_handle,
            standard_surface_shape_function_handle,
            x, y, v,
            input_params_dict,
            opt_or_tol_dict)

    else:  # Use tol_dict

        v_res, v_fit, opt_params_dict, opt_params_ci_dict, init_params = optimize_parameters_with_tol(
            surface_generation_function_handle,
            standard_surface_shape_function_handle,
            x, y, v,
            input_params_dict,
            opt_or_tol_dict)
        
    return v_res, v_fit, opt_params_dict, opt_params_ci_dict, init_params


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
    init_params = np.array([p, q, theta, x_i, y_i, z_i, alpha, beta, gamma])

    return init_params


def optimize_parameters_with_opt(surface_generation_function_handle, 
                                 standard_surface_shape_function_handle, 
                                 x: np.array, 
                                 y: np.array, 
                                 v: np.array, 
                                 input_params_dict: dict, 
                                 opt_dict: dict,
                                 ):
    """
    Basic function to provide a convenient way to optimize the surface parameters with optimization flag.

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
        opt_dict: `dict`
            The structure to set whether optimization is needed for 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``.

    Returns
    -------
        v_res:`numpy.ndarray`
            The residual (1D or 2D)
        v_fit: `numpy.ndarray`
            The fitting result (1D or 2D)
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
        init_params: `numpy.ndarray`
            The used initial parameters.
    """ 

    def check_opt_dict(opt_dict, surface_generation_function_handle): 
        
        opt_vector = np.zeros(9, dtype=bool)

        if surface_generation_function_handle == generate_2d_curved_surface_height:
            opt_vector[3:] = True # x_i, y_i, z_i, alpha, beta, gamma
        elif surface_generation_function_handle == generate_2d_cylinder_height:
            opt_vector[3] = True # x_i
            opt_vector[5] = True # z_i
            opt_vector[6:] = True # alpha, beta, gamma
        elif surface_generation_function_handle == generate_1d_height:
            opt_vector[3] = True # x_i
            opt_vector[5] = True # z_i
            opt_vector[7] = True # beta
        elif surface_generation_function_handle == generate_1d_slope:
            opt_vector[3] = True # x_i
            opt_vector[7] = True # beta

        # Update the user defined optimization flags
        if 'p' in opt_dict: opt_vector[0] = opt_dict['p']
        if 'q' in opt_dict: opt_vector[1] = opt_dict['q']
        if 'theta' in opt_dict: opt_vector[2] = opt_dict['theta']
        if 'x_i' in opt_dict: opt_vector[3] = opt_dict['x_i']
        if 'y_i' in opt_dict: opt_vector[4] = opt_dict['y_i']
        if 'z_i' in opt_dict: opt_vector[5] = opt_dict['z_i']
        if 'alpha' in opt_dict: opt_vector[6] = opt_dict['alpha']
        if 'beta' in opt_dict: opt_vector[7] = opt_dict['beta']
        if 'gamma' in opt_dict: opt_vector[8] = opt_dict['gamma']

        return opt_vector

    # Initial values
    init_params = check_input_params(input_params_dict, x, y, v)

    # Optimization flags
    opt_vector = check_opt_dict(opt_dict, surface_generation_function_handle)

    # Use NaN to identify the parameters which are required to optimize
    param_fix = init_params.copy()
    param_fix[opt_vector] = np.nan
    param = init_params[opt_vector] # Only optimize parameters required to optimize

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
        
    def cost_func_of_least_squares(param, x, y, v, param_fix):
        """
        Cost function to use scipy.optimize.least_squares module

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
    param = init_params[opt_vector] + np.ones_like(init_params[opt_vector]) * 1e-6 # Add a small value to the initial parameters

    # Optimize with the least squares method
    result = least_squares(cost_func_of_least_squares, param, args=(x, y, v, param_fix), method='lm')
    
    # Re-calculate the fitting and residual
    param_opt = result.x
    _, v_fit, v_res = common_cost_function_for_optimization(surface_generation_function_handle, 
                                                            standard_surface_shape_function_handle, 
                                                            x, y, v, param_fix, param_opt)
    
    # Release the result in a structure for better understanding
    param_result = np.copy(param_fix)
    param_result[opt_vector] = result.x # Optimization result

    def calculate_ci_95(result):
        
        # Step 1: Extract information
        J = result.jac                      # Jacobian matrix (m x n)
        residuals = result.fun             # residual vector (m,)
        n_params = len(result.x)           # number of parameters
        dof = max(1, len(residuals) - n_params)  # degrees of freedom

        # Step 2: Estimate residual variance
        s_sq = np.sum(residuals**2) / dof

        # Step 3: Estimate parameter covariance matrix
        pcov = np.linalg.inv(J.T @ J) * s_sq

        # Step 4: Standard deviation (1σ) of each parameter
        perr = np.sqrt(np.diag(pcov))

        # Step 5: Compute 95.45% confidence intervals (±2σ)
        ci_lower = result.x - 2 * perr
        ci_upper = result.x + 2 * perr
        ci = np.vstack((ci_lower, ci_upper)).T  # Shape (n_params, 2)
        return ci
    
    # Get 95% confidence intervals
    param_ci_result = np.zeros((param_fix.size, 2))
    param_ci_result[opt_vector] = calculate_ci_95(result)


    str_param_name_list = ['p', 'q', 'theta',
                            'x_i', 'y_i', 'z_i', 
                            'alpha', 'beta', 'gamma']
    opt_params_dict = {}
    opt_params_ci_dict = {}
    # Release the optimized values
    for idx, str_param_name in enumerate(str_param_name_list):
        opt_params_dict[str_param_name] = param_result[idx] if opt_vector[idx] else param_fix[idx]
        opt_params_ci_dict[str_param_name] = param_ci_result[idx] if opt_vector[idx] else np.full(2, np.nan)
        
    return v_res, v_fit, opt_params_dict, opt_params_ci_dict, init_params


def optimize_parameters_with_tol(surface_generation_function_handle, 
                                 standard_surface_shape_function_handle, 
                                 x: np.array, 
                                 y: np.array, 
                                 v: np.array, 
                                 input_params_dict: dict, 
                                 tol_dict: dict,
                                 ):
    """
    Basic function to provide a convenient way to optimize the surface parameters with tolerances.

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
        tol_dict: `dict`
            The structure to set the tolerances for 
            ``p``, ``q``, ``theta``, ``x_i``, ``y_i``, ``z_i``, ``alpha``, ``beta``, ``gamma``.

    Returns
    -------
        v_res:`numpy.ndarray`
            The residual (1D or 2D)
        v_fit: `numpy.ndarray`
            The fitting result (1D or 2D)
        opt_params_dict: `dict`
            The optimized parameters in dictionary
        opt_params_ci_dict: `dict`
            The confidence intervals of the optimized parameters in dictionary
        init_params: `numpy.ndarray`
            The used initial parameters.
    """

    def check_tol_dict(tol_dict, surface_generation_function_handle): 
        
        opt_vector = np.zeros(9, dtype=bool)

        if surface_generation_function_handle == generate_2d_curved_surface_height:
            opt_vector[3:] = True # x_i, y_i, z_i, alpha, beta, gamma
        elif surface_generation_function_handle == generate_2d_cylinder_height:
            opt_vector[3] = True # x_i
            opt_vector[5] = True # z_i
            opt_vector[6:] = True # alpha, beta, gamma
        elif surface_generation_function_handle == generate_1d_height:
            opt_vector[3] = True # x_i
            opt_vector[5] = True # z_i
            opt_vector[7] = True # beta
        elif surface_generation_function_handle == generate_1d_slope:
            opt_vector[3] = True # x_i
            opt_vector[7] = True # beta

        keys = ['p', 'q', 'theta', 'x_i', 'y_i', 'z_i', 'alpha', 'beta', 'gamma']
        tol_vector = np.zeros((9, 2))

        def unify_tol_struct_format(tol_dict, str_key, is_opt):
            unified_tol_dict = tol_dict.copy()
            # If the field exists
            if str_key in unified_tol_dict:
                val = unified_tol_dict[str_key]
                if np.isscalar(val):
                    unified_tol_dict[str_key] = np.array([-1, 1]) * val
                else:
                    assert np.size(val) <= 2
                    unified_tol_dict[str_key] = np.array(val)
            else:
                if is_opt:
                    unified_tol_dict[str_key] = np.array([-np.inf, np.inf])
                else:
                    unified_tol_dict[str_key] = np.array([0, 0])
            return unified_tol_dict
        # Check the tolerance structure and unify the format
        for num in range(9):
            # Unify the tolerance structure format as two boundaries
            unified_tol_dict = unify_tol_struct_format(tol_dict, keys[num], opt_vector[num])
            # Update the user defined optimization flags
            opt_vector[num] = not np.all(np.array(unified_tol_dict[keys[num]]) == 0)
            # Update the tolerance vector
            tol_vector[num, :] = unified_tol_dict[keys[num]]

        return opt_vector, tol_vector

    # Initial values
    init_params = check_input_params(input_params_dict, x, y, v)

    # Optimization flags
    opt_vector, tol_vector = check_tol_dict(tol_dict, surface_generation_function_handle)

    # Use NaN to identify the parameters which are required to optimize
    param_fix = init_params.copy()
    param_fix[opt_vector] = np.nan
    param = init_params[opt_vector] # Only optimize parameters required to optimize

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
        
    def cost_func_of_least_squares(param, x, y, v, param_fix):
        """
        Cost function to use scipy.optimize.least_squares module

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
    param = init_params[opt_vector] + np.ones_like(init_params[opt_vector]) * 1e-6 # Add a small value to the initial parameters

    # Determine the lower and upper boundaries
    lb = param + tol_vector[opt_vector, 0]
    ub = param + tol_vector[opt_vector, 1]

    # Optimize with the least squares method
    result = least_squares(cost_func_of_least_squares, param, bounds=[lb, ub], args=(x, y, v, param_fix), method='lm')

    # Re-calculate the fitting and residual
    param_opt = result.x
    _, v_fit, v_res = common_cost_function_for_optimization(surface_generation_function_handle, 
                                                            standard_surface_shape_function_handle, 
                                                            x, y, v, param_fix, param_opt)
    
    # Release the result in a structure for better understanding
    param_result = np.copy(param_fix)
    param_result[opt_vector] = result.x # Optimization result

    def calculate_ci_95(result):
        
        # Step 1: Extract information
        J = result.jac                     # Jacobian matrix (m x n)
        residuals = result.fun             # residual vector (m,)
        n_params = len(result.x)           # number of parameters
        dof = max(1, len(residuals) - n_params)  # degrees of freedom

        # Step 2: Estimate residual variance
        s_sq = np.sum(residuals**2) / dof

        # Step 3: Estimate parameter covariance matrix
        pcov = np.linalg.inv(J.T @ J) * s_sq

        # Step 4: Standard deviation (1σ) of each parameter
        perr = np.sqrt(np.diag(pcov))

        # Step 5: Compute 95.45% confidence intervals (±2σ)
        ci_lower = result.x - 2 * perr
        ci_upper = result.x + 2 * perr
        ci = np.vstack((ci_lower, ci_upper)).T  # Shape (n_params, 2)
        return ci
    
    # Get 95% confidence intervals
    param_ci_result = np.zeros((param_fix.size, 2))
    param_ci_result[opt_vector] = calculate_ci_95(result)


    # Release the optimized values
    str_param_name_list = ['p', 'q', 'theta',
                           'x_i', 'y_i', 'z_i', 
                           'alpha', 'beta', 'gamma']
    opt_params_dict = {}
    opt_params_ci_dict = {}
    for idx, str_param_name in enumerate(str_param_name_list):
        opt_params_dict[str_param_name] = param_result[idx] if opt_vector[idx] else param_fix[idx]
        opt_params_ci_dict[str_param_name] = param_ci_result[idx] if opt_vector[idx] else np.full(2, np.nan)
        
    return v_res, v_fit, opt_params_dict, opt_params_ci_dict, init_params
