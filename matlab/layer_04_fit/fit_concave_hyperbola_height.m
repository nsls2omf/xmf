function [z1d_res, z1d_fit, params, params_ci] = fit_concave_hyperbola_height(x1d, z1d_measured, input_params_struct, opt_or_tol_struct)
% fit_concave_hyperbola_height - Fits a concave hyperbolic cylinder to a 1D height profile
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
%       - params - Fitted parameters of the concave hyperbolic cylinder
%       - params_ci - Confidence intervals of the fitted parameters

y1d = x1d*0;

[z1d_res, z1d_fit, params, params_ci] = optimize_parameters ...
    ( @generate_1d_height ...
    , @standard_concave_hyperbolic_cylinder_height ...
    , x1d, y1d, z1d_measured, input_params_struct, opt_or_tol_struct);