function [sx1d_res, sx1d_fit, opt_params_struct, opt_params_ci_struct, init_params_struct] = fit_concave_ellipse_slope(x1d, sx1d_measured, input_params_struct, opt_or_tol_struct)
% fit_concave_ellipse_slope - Fits a concave elliptic cylinder to a 1D slope profile
%
%   Inputs:
%       - x1d - 1D x-coordinates (vector)
%       - sx1d_measured - 1D slope values (vector)
%       - input_params_struct - Structure containing initial parameters for the fit
%       - opt_or_tol_struct - Structure containing optimization or tolerance parameters
%
%   Outputs:
%       - sx1d_res - Residuals of the fitted slope profile
%       - sx1d_fit - Fitted slope profile
%       - opt_params_struct - Fitted parameters of the concave elliptic cylinder
%       - opt_params_ci_struct - Confidence intervals of the fitted parameters
%       - init_params_struct - Structure containing initial parameters used for the fit

y1d = x1d*0;

[sx1d_res, sx1d_fit, opt_params_struct, opt_params_ci_struct, init_params_struct] = optimize_parameters ...
    ( @generate_1d_slope ...
    , @standard_concave_elliptic_cylinder_xslope ...
    , x1d, y1d, sx1d_measured, input_params_struct, opt_or_tol_struct);