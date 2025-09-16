function [z2d_res, z2d_fit, params, params_ci]=fit_tan_col_diaboloid_height(x2d, y2d, z2d, input_params_structure, opt_or_tol_structure)
% fit_tan_col_diaboloid_height - Fits a tangential collimating diaboloid to a 2D height map
%   
%   Inputs:
%       - x2d - 2D x-coordinates (matrix)
%       - y2d - 2D y-coordinates (matrix)
%       - z2d - 2D height values (matrix)
%       - input_params_structure - Structure containing initial parameters for the fit
%       - opt_or_tol_structure - Structure containing optimization or tolerance parameters
%
%   Outputs:
%       - z2d_res - Residuals of the fitted height map
%       - z2d_fit - Fitted height map
%       - params - Fitted parameters of the tangential collimating diaboloid
%       - params_ci - Confidence intervals of the fitted parameters

[z2d_res, z2d_fit, params, params_ci] = optimize_parameters ...
    ( @generate_2d_curved_surface_height ...
    , @standard_tan_col_diaboloid_height ...
    , x2d, y2d, z2d, input_params_structure, opt_or_tol_structure);