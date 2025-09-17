function [z2d_res, z2d_fit, opt_params_struct, opt_params_ci_struct, init_params_struct]=fit_convex_hyperboloid_height(x2d, y2d, z2d, input_params_struct, opt_or_tol_struct)
% fit_convex_hyperboloid_height - Fits a convex hyperboloid to a 2D height map
%
%   Inputs:
%       - x2d - 2D x-coordinates (matrix)
%       - y2d - 2D y-coordinates (matrix)
%       - z2d - 2D height values (matrix)
%       - input_params_struct - Structure containing initial parameters for the fit
%       - opt_or_tol_struct - Structure containing optimization or tolerance parameters
%
%   Outputs:
%       - z2d_res - Residuals of the fitted height map
%       - z2d_fit - Fitted height map
%       - opt_params_struct - Fitted parameters of the convex hyperboloid
%       - opt_params_ci_struct - Confidence intervals of the fitted parameters
%       - init_params_struct - Initial parameters used for the fit

[z2d_res, z2d_fit, opt_params_struct, opt_params_ci_struct, init_params_struct] = optimize_parameters ...
    ( @generate_2d_curved_surface_height ...
    , @standard_convex_hyperboloid_height ...
    , x2d, y2d, z2d, input_params_struct, opt_or_tol_struct);