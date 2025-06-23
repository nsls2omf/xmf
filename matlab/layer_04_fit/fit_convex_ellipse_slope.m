function [sx1d_res, sx1d_fit, params, params_ci] = fit_convex_ellipse_slope(x1d, sx1d_measured, pqtx, is_opt_1d_cylinder_slope)
% fit_convex_ellipse_slope provide a convenient way to fit parameters
% from a measured convex ellipse slope.

y1d = x1d*0;

[sx1d_res, sx1d_fit, params, params_ci] = optimize_parameters ...
    ( @generate_1d_slope ...
    , @standard_convex_elliptic_cylinder_xslope ...
    , x1d, y1d, sx1d_measured, pqtx, is_opt_1d_cylinder_slope);