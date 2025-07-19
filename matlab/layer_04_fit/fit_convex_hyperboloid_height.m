function [z2d_res, z2d_fit, params, params_ci]=fit_convex_hyperboloid_height(x2d, y2d, z2d, input_params_struct, opt_or_tol_struct)
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
%       - params - Fitted parameters of the convex hyperboloid
%       - params_ci - Confidence intervals of the fitted parameters

[z2d_res, z2d_fit, params, params_ci] = optimize_parameters ...
    ( @generate_2d_curved_surface_height ...
    , @standard_convex_hyperboloid_height ...
    , x2d, y2d, z2d, input_params_struct, opt_or_tol_struct);