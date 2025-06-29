function [z1d_res, z1d_fit, params, params_ci] = fit_convex_hyperbola_height(x1d, z1d_measured, input_params_struct, opt_or_tol_struct)
% fit_convex_hyperbola_height provide a convenient way to fit parameters
% from a measured convex hyperbola height.

y1d = x1d*0;

[z1d_res, z1d_fit, params, params_ci] = optimize_parameters ...
    ( @generate_1d_height ...
    , @standard_convex_hyperbolic_cylinder_height ...
    , x1d, y1d, z1d_measured, input_params_struct, opt_or_tol_struct);