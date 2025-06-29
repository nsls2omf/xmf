function [sx1d_res, sx1d_fit, params, params_ci] = fit_concave_ellipse_slope(x1d, sx1d_measured, input_params_struct, opt_or_tol_struct)
% fit_concave_ellipse_xslope provide a convenient way to fit parameters
% from a measured concave ellipse slope.

y1d = x1d*0;

[sx1d_res, sx1d_fit, params, params_ci] = optimize_parameters ...
    ( @generate_1d_slope ...
    , @standard_concave_elliptic_cylinder_xslope ...
    , x1d, y1d, sx1d_measured, input_params_struct, opt_or_tol_struct);