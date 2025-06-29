% Demo script to fit 2D maps

close all;
clear;
clc;

addpath('fig_show');
addpath('layer_01_standard');
addpath('layer_02_generation');
addpath('layer_03_optimization');
addpath('layer_04_fit');


%% 1. Lateral coordinates

x_range = 200e-3;
y_range = 20e-3;
x_num = 201;
y_num = 21;
x1d = linspace(-x_range/2, x_range/2, x_num);
y1d = linspace(-y_range/2, y_range/2, y_num);
[x2d, y2d] = meshgrid(x1d, y1d);

abs_p = 30;
abs_q = 0.3;
theta = 30e-3;

x_i = -1e-3;
y_i = -2e-4;
z_i = 3e-7;
alpha = 2e-6;
beta = 1e-5;
gamma = 0.5e-3;

true_params_struct.p = abs_p;
true_params_struct.q = abs_q;
true_params_struct.theta = theta;
true_params_struct.x_i = x_i;
true_params_struct.y_i = y_i;
true_params_struct.z_i = z_i;
true_params_struct.alpha = alpha;
true_params_struct.beta = beta;
true_params_struct.gamma = gamma;

height_measurement_noise_std = 0.5e-9;
slope_measurement_noise_std = 100e-9;

input_params_struct.p = abs_p;
input_params_struct.q = abs_q;
input_params_struct.theta = theta;

tol_struct.p = 0;
tol_struct.q = 0;
tol_struct.theta = 0;



%% 2.1. Convex Ellipsoid (CVXE)

z2d = generate_2d_curved_surface_height(@standard_convex_ellipsoid_height, x2d, y2d, abs_p, abs_q, theta, x_i, y_i, z_i, alpha, beta, gamma);
z2d_measured = z2d + randn(size(z2d))*height_measurement_noise_std;
[z2d_res, z2d_fit, opt_params_struct, opt_params_ci_struct] = fit_convex_ellipsoid_height(x2d, y2d, z2d_measured, input_params_struct, tol_struct);
fig_show_2d_fitting_maps(x1d, y1d, z2d_measured, z2d_fit, z2d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Convex Ellipsoid');


%% 2.2. Concave Ellipsoid (CCVE)

z2d = generate_2d_curved_surface_height(@standard_concave_ellipsoid_height, x2d, y2d, abs_p, abs_q, theta, x_i, y_i, z_i, alpha, beta, gamma);
z2d_measured = z2d + randn(size(z2d))*height_measurement_noise_std;
[z2d_res, z2d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_ellipsoid_height(x2d, y2d, z2d_measured, input_params_struct, tol_struct);
fig_show_2d_fitting_maps(x1d, y1d, z2d_measured, z2d_fit, z2d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Ellipsoid');


%% 3.1. Convex Elliptic Cylinder (CVXEC)

z2d = generate_2d_cylinder_height(@standard_convex_elliptic_cylinder_height, x2d, y2d, abs_p, abs_q, theta, x_i, z_i, alpha, beta, gamma);
z2d_measured = z2d + randn(size(z2d))*height_measurement_noise_std;
[z2d_res, z2d_fit, opt_params_struct, opt_params_ci_struct] = fit_convex_elliptic_cylinder_height(x2d, y2d, z2d_measured, input_params_struct, tol_struct);
fig_show_2d_fitting_maps(x1d, y1d, z2d_measured, z2d_fit, z2d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Convex Elliptic Cylinder');

z1d = generate_1d_height(@standard_convex_elliptic_cylinder_height, x1d, abs_p, abs_q, theta, x_i, z_i, beta);
z1d_measured = z1d + randn(size(z1d))*height_measurement_noise_std;
[z1d_res, z1d_fit, opt_params_struct, opt_params_ci_struct] = fit_convex_ellipse_height(x1d, z1d_measured, input_params_struct, tol_struct);
fig_show_1d_fitting_height(x1d, z1d_measured, z1d_fit, z1d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Convex Elliptic Cylinder');

sx1d = generate_1d_slope(@standard_convex_elliptic_cylinder_xslope, x1d, abs_p, abs_q, theta, x_i, beta);
sx1d_measured = sx1d + randn(size(sx1d))*slope_measurement_noise_std;
[sx1d_res, sx1d_fit, opt_params_struct, opt_params_ci_struct] = fit_convex_ellipse_slope(x1d, sx1d_measured, input_params_struct, tol_struct);
fig_show_1d_fitting_slopes(x1d, sx1d_measured, sx1d_fit, sx1d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Convex Elliptic Cylinder');


%% 3.2. Concave Elliptic Cylinder (CCVEC)

z2d = generate_2d_cylinder_height(@standard_concave_elliptic_cylinder_height, x2d, y2d, abs_p, abs_q, theta, x_i, z_i, alpha, beta, gamma);
z2d_measured = z2d + randn(size(z2d))*height_measurement_noise_std;
[z2d_res, z2d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_elliptic_cylinder_height(x2d, y2d, z2d_measured, input_params_struct, tol_struct);
fig_show_2d_fitting_maps(x1d, y1d, z2d_measured, z2d_fit, z2d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Elliptic Cylinder');

z1d = generate_1d_height(@standard_concave_elliptic_cylinder_height, x1d, abs_p, abs_q, theta, x_i, z_i, beta);
z1d_measured = z1d + randn(size(z1d))*height_measurement_noise_std;
[z1d_res, z1d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_ellipse_height(x1d, z1d_measured, input_params_struct, tol_struct);
fig_show_1d_fitting_height(x1d, z1d_measured, z1d_fit, z1d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Elliptic Cylinder');

sx1d = generate_1d_slope(@standard_concave_elliptic_cylinder_xslope, x1d, abs_p, abs_q, theta, x_i, beta);
sx1d_measured = sx1d + randn(size(sx1d))*slope_measurement_noise_std;
[sx1d_res, sx1d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_ellipse_slope(x1d, sx1d_measured, input_params_struct, tol_struct);
fig_show_1d_fitting_slopes(x1d, sx1d_measured, sx1d_fit, sx1d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Elliptic Cylinder');


%% 6.1. Convex Hyperboloid (CVXH)

z2d = generate_2d_curved_surface_height(@standard_convex_hyperboloid_height, x2d, y2d, abs_p, abs_q, theta, x_i, y_i, z_i, alpha, beta, gamma);
z2d_measured = z2d + randn(size(z2d))*height_measurement_noise_std;
[z2d_res, z2d_fit, opt_params_struct, opt_params_ci_struct] = fit_convex_hyperboloid_height(x2d, y2d, z2d_measured, input_params_struct, tol_struct);
fig_show_2d_fitting_maps(x1d, y1d, z2d_measured, z2d_fit, z2d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Convex Hyperboloid');


%% 6.2. Concave Hyperboloid (CCVH)

z2d = generate_2d_curved_surface_height(@standard_concave_hyperboloid_height, x2d, y2d, abs_p, abs_q, theta, x_i, y_i, z_i, alpha, beta, gamma);
z2d_measured = z2d + randn(size(z2d))*height_measurement_noise_std;
[z2d_res, z2d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_hyperboloid_height(x2d, y2d, z2d_measured, input_params_struct, tol_struct);
fig_show_2d_fitting_maps(x1d, y1d, z2d_measured, z2d_fit, z2d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Hyperboloid');


%% 7.1. Convex Hyperbolic Cylinder (CVXHC)

z2d = generate_2d_cylinder_height(@standard_convex_hyperbolic_cylinder_height, x2d, y2d, abs_p, abs_q, theta, x_i, z_i, alpha, beta, gamma);
z2d_measured = z2d + randn(size(z2d))*height_measurement_noise_std;
[z2d_res, z2d_fit, opt_params_struct, opt_params_ci_struct] = fit_convex_hyperbolic_cylinder_height(x2d, y2d, z2d_measured, input_params_struct, tol_struct);
fig_show_2d_fitting_maps(x1d, y1d, z2d_measured, z2d_fit, z2d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Convex Hyperbolic Cylinder');

z1d = generate_1d_height(@standard_convex_hyperbolic_cylinder_height, x1d, abs_p, abs_q, theta, x_i, z_i, beta);
z1d_measured = z1d + randn(size(z1d))*height_measurement_noise_std;
[z1d_res, z1d_fit, opt_params_struct, opt_params_ci_struct] = fit_convex_hyperbola_height(x1d, z1d_measured, input_params_struct, tol_struct);
fig_show_1d_fitting_height(x1d, z1d_measured, z1d_fit, z1d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Convex Hyperbolic Cylinder');

sx1d = generate_1d_slope(@standard_convex_hyperbolic_cylinder_xslope, x1d, abs_p, abs_q, theta, x_i, beta);
sx1d_measured = sx1d + randn(size(sx1d))*slope_measurement_noise_std;
[sx1d_res, sx1d_fit, opt_params_struct, opt_params_ci_struct] = fit_convex_hyperbola_slope(x1d, sx1d_measured, input_params_struct, tol_struct);
fig_show_1d_fitting_slopes(x1d, sx1d_measured, sx1d_fit, sx1d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Convex Hyperbolic Cylinder');


%% 7.2. Concave Hyperbolic Cylinder (CCVHC)

z2d = generate_2d_cylinder_height(@standard_concave_hyperbolic_cylinder_height, x2d, y2d, abs_p, abs_q, theta, x_i, z_i, alpha, beta, gamma);
z2d_measured = z2d + randn(size(z2d))*height_measurement_noise_std;
[z2d_res, z2d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_hyperbolic_cylinder_height(x2d, y2d, z2d_measured, input_params_struct, tol_struct);
fig_show_2d_fitting_maps(x1d, y1d, z2d_measured, z2d_fit, z2d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Hyperbolic Cylinder');

z1d = generate_1d_height(@standard_concave_hyperbolic_cylinder_height, x1d, abs_p, abs_q, theta, x_i, z_i, beta);
z1d_measured = z1d + randn(size(z1d))*height_measurement_noise_std;
[z1d_res, z1d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_hyperbola_height(x1d, z1d_measured, input_params_struct, tol_struct);
fig_show_1d_fitting_height(x1d, z1d_measured, z1d_fit, z1d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Convex Hyperbolic Cylinder');

sx1d = generate_1d_slope(@standard_concave_hyperbolic_cylinder_xslope, x1d, abs_p, abs_q, theta, x_i, beta);
sx1d_measured = sx1d + randn(size(sx1d))*slope_measurement_noise_std;
[sx1d_res, sx1d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_hyperbola_slope(x1d, sx1d_measured, input_params_struct, tol_struct);
fig_show_1d_fitting_slopes(x1d, sx1d_measured, sx1d_fit, sx1d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Hyperbolic Cylinder');

