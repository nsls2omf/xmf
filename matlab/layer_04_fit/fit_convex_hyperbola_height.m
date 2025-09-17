function [z1d_res, z1d_fit, opt_params_struct, opt_params_ci_struct, init_params_struct] = fit_convex_hyperbola_height(x1d, z1d_measured, input_params_struct, opt_or_tol_struct)
% fit_convex_hyperbola_height - Fits a convex hyperbolic cylinder to a 1D height profile
%
%   Inputs:
%       - x1d - 1D x-coordinates (vector)
%       - z1d_measured - 1D height values (vector)
%       - input_params_struct - Structure containing initial parameters for the fit
%       - opt_or_tol_struct - Structure containing optimization or tolerance parameters
%
%   Outputs:
%       - z1d_res - Residuals of the fitted height profile
%       - z1d_fit - Fitted height profile
%       - opt_params_struct - Fitted parameters of the convex hyperbolic cylinder
%       - opt_params_ci_struct - Confidence intervals of the fitted parameters
%       - init_params_struct - Initial parameters used for the fit

y1d = x1d*0;

[z1d_res, z1d_fit, opt_params_struct, opt_params_ci_struct, init_params_struct] = optimize_parameters ...
    ( @generate_1d_height ...
    , @standard_convex_hyperbolic_cylinder_height ...
    , x1d, y1d, z1d_measured, input_params_struct, opt_or_tol_struct);