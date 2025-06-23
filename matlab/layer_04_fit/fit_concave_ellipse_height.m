function [z1d_res, z1d_fit, params, params_ci] = fit_concave_ellipse_height(x1d, z1d_measured, pqtx, is_opt_1d_cylinder_height)
% fit_concave_ellipse_height provide a convenient way to fit parameters
% from a measured concave ellipse height.

y1d = x1d*0;

[z1d_res, z1d_fit, params, params_ci] = optimize_parameters ...
    ( @generate_1d_height ...
    , @standard_concave_elliptic_cylinder_height ...
    , x1d, y1d, z1d_measured, pqtx, is_opt_1d_cylinder_height);