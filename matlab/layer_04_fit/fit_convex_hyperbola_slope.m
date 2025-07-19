function [sx1d_res, sx1d_fit, params, params_ci] = fit_convex_hyperbola_slope(x1d, sx1d_measured, input_params_struct, opt_or_tol_struct)
% fit_convex_hyperbola_slope - Fits a convex hyperbolic cylinder to a 1D slope profile
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
%       - params - Fitted parameters of the convex hyperbolic cylinder
%       - params_ci - Confidence intervals of the fitted parameters

y1d = x1d*0;

[sx1d_res, sx1d_fit, params, params_ci] = optimize_parameters ...
    ( @generate_1d_slope ...
    , @standard_convex_hyperbolic_cylinder_xslope ...
    , x1d, y1d, sx1d_measured, input_params_struct, opt_or_tol_struct);