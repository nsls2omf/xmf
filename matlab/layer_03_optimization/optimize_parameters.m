function [v_res, v_fit, opt_params_struct, opt_params_ci_struct, init_params_struct] = optimize_parameters(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, input_params_struct, opt_or_tol_struct)
% optimize_parameters provide a convenient way to optimize the surface 
% parameters from measurement data.
%
%    Input:
%        - surface_generation_function_handle is function handle for surface generation
%        - standard_surface_shape_function_handle is function handle for a standard surface shape
%        - x is the measured x-coordinate, in unit of [m] as a suggestion
%        - y is the measured y-coordinate, in unit of [m] as a suggestion
%        - v is the measured slope or height in [rad] or [m] as a suggestion
%        - input_params_struct contains p, q, theta, x_i(optional), y_i(optional), z_i(optional), alpha(optional), beta(optional) and gamma(optional) target parameters, suggested in unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
%        - opt_or_tol_struct is a structure of optimization flag or tolerance for p, q, theta, x_i, y_i, z_i, alpha, beta, gamma.
%
%    Output:
%        - v_res is the residual in [m], if the input x and z are in [m]
%        - v_fit is fitting result in [m], if the input x and z are in [m]
%        - opt_params_struct is the optimized params in structure
%        - params_ci_struct is the confidence intervals of the parameters.
%        - init_params_struct is the used initial parameters.

%   Copyright since 2023 by Lei Huang. All Rights Reserved.
%   E-mail: huanglei0114@gmail.com
%   v1.0.2023.11.19 basic version
%   v1.1.2025.01.20 rename some variables
%   v2.0.2025.03.25 general version
%   v2.1.2025.06.24 general version with tolerance
%   v2.1.2025.06.27 combine both is_opt and tolerance versions

if islogical(opt_or_tol_struct.p) % Use opt_struct

    [v_res, v_fit, opt_params_struct, opt_params_ci_struct, init_params_struct] ...
        = optimize_parameters_with_opt(surface_generation_function_handle ...
        , standard_surface_shape_function_handle ...
        , x, y, v ...
        , input_params_struct ...
        , opt_or_tol_struct);

else % Use tol_struct

    [v_res, v_fit, opt_params_struct, opt_params_ci_struct, init_params_struct] ...
        = optimize_parameters_with_tol(surface_generation_function_handle ...
        , standard_surface_shape_function_handle ...
        , x, y, v ...
        , input_params_struct ...
        , opt_or_tol_struct);

end