% Demo script to generate shapes

close all;
clear;
clc;

addpath('fig_show');
addpath('layer_01_standard');
addpath('layer_02_generation');


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

abs_q_t = 0.3;
abs_q_s = 0.6;

x_i = 0*-1e-3;
y_i = 0*-2e-4;
z_i = 0*3e-7;
alpha = 0*2e-6;
beta = 0*1e-5;
gamma = 0.5e-3;


%% 2.1. Convex Ellipsoid (CVXE)

z2d_standard = standard_convex_ellipsoid_height(x2d, y2d, abs_p, abs_q, theta);
z2d = generate_2d_curved_surface_height(@standard_convex_ellipsoid_height, x2d, y2d, abs_p, abs_q, theta, x_i, y_i, z_i, alpha, beta, gamma);
fig_compare_2d_map(x1d, y1d, z2d, z2d_standard, 'Convex Ellipsoid');


%% 2.2. Concave Ellipsoid (CCVE)

z2d_standard = standard_concave_ellipsoid_height(x2d, y2d, abs_p, abs_q, theta);
z2d = generate_2d_curved_surface_height(@standard_concave_ellipsoid_height, x2d, y2d, abs_p, abs_q, theta, x_i, y_i, z_i, alpha, beta, gamma);
fig_compare_2d_map(x1d, y1d, z2d, z2d_standard, 'Concave Ellipsoid');


%% 3.1. Convex Elliptic Cylinder (CVXEC)

z2d_standard = standard_convex_elliptic_cylinder_height(x2d, abs_p, abs_q, theta);
z2d = generate_2d_cylinder_height(@standard_convex_elliptic_cylinder_height, x2d, y2d, abs_p, abs_q, theta, x_i, z_i, alpha, beta, gamma);
fig_compare_2d_map(x1d, y1d, z2d, z2d_standard, 'Convex Elliptic Cylinder');

z1d_standard = standard_convex_elliptic_cylinder_height(x1d, abs_p, abs_q, theta);
z1d = generate_1d_height(@standard_convex_elliptic_cylinder_height, x1d, abs_p, abs_q, theta, x_i, z_i, beta);
fig_compare_1d_height(x1d, z1d, z1d_standard, 'Convex Elliptic Cylinder');

sx1d_standard = standard_convex_elliptic_cylinder_xslope(x1d, abs_p, abs_q, theta);
sx1d = generate_1d_slope(@standard_convex_elliptic_cylinder_xslope, x1d, abs_p, abs_q, theta, x_i, beta);
fig_compare_1d_slope(x1d, sx1d, sx1d_standard, 'Convex Elliptic Cylinder');


%% 3.2. Concave Elliptic Cylinder (CCVEC)

z2d_standard = standard_concave_elliptic_cylinder_height(x2d, abs_p, abs_q, theta);
z2d = generate_2d_cylinder_height(@standard_concave_elliptic_cylinder_height, x2d, y2d, abs_p, abs_q, theta, x_i, z_i, alpha, beta, gamma);
fig_compare_2d_map(x1d, y1d, z2d, z2d_standard, 'Concave Elliptic Cylinder');

z1d_standard = standard_concave_elliptic_cylinder_height(x1d, abs_p, abs_q, theta);
z1d = generate_1d_height(@standard_concave_elliptic_cylinder_height, x1d, abs_p, abs_q, theta, x_i, z_i, beta);
fig_compare_1d_height(x1d, z1d, z1d_standard, 'Concave Elliptic Cylinder');

sx1d_standard = standard_concave_elliptic_cylinder_xslope(x1d, abs_p, abs_q, theta);
sx1d = generate_1d_slope(@standard_concave_elliptic_cylinder_xslope, x1d, abs_p, abs_q, theta, x_i, beta);
fig_compare_1d_slope(x1d, sx1d, sx1d_standard, 'Concave Elliptic Cylinder');


%% 6.1. Convex Hyperboloid (CVXH)

z2d_standard = standard_convex_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta);
z2d = generate_2d_curved_surface_height(@standard_convex_hyperboloid_height, x2d, y2d, abs_p, abs_q, theta, x_i, y_i, z_i, alpha, beta, gamma);
fig_compare_2d_map(x1d, y1d, z2d, z2d_standard, 'Convex Hyperboloid');


%% 6.2. Concave Hyperboloid (CCVH)

z2d_standard = standard_concave_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta);
z2d = generate_2d_curved_surface_height(@standard_concave_hyperboloid_height, x2d, y2d, abs_p, abs_q, theta, x_i, y_i, z_i, alpha, beta, gamma);
fig_compare_2d_map(x1d, y1d, z2d, z2d_standard, 'Concave Hyperboloid');


%% 7.1. Convex Hyperbolic Cylinder (CVXHC)

z2d_standard = standard_convex_hyperbolic_cylinder_height(x2d, abs_p, abs_q, theta);
z2d = generate_2d_cylinder_height(@standard_convex_hyperbolic_cylinder_height, x2d, y2d, abs_p, abs_q, theta, x_i, z_i, alpha, beta, gamma);
fig_compare_2d_map(x1d, y1d, z2d, z2d_standard, 'Convex Hyperbolic Cylinder');

z1d_standard = standard_convex_hyperbolic_cylinder_height(x1d, abs_p, abs_q, theta);
z1d = generate_1d_height(@standard_convex_hyperbolic_cylinder_height, x1d, abs_p, abs_q, theta, x_i, z_i, beta);
fig_compare_1d_height(x1d, z1d, z1d_standard, 'Convex Hyperbolic Cylinder');

sx1d_standard = standard_convex_hyperbolic_cylinder_xslope(x1d, abs_p, abs_q, theta);
sx1d = generate_1d_slope(@standard_convex_hyperbolic_cylinder_xslope, x1d, abs_p, abs_q, theta, x_i, beta);
fig_compare_1d_slope(x1d, sx1d, sx1d_standard, 'Convex Hyperbolic Cylinder');


%% 7.2. Concave Hyperbolic Cylinder (CCVHC)

z2d_standard = standard_concave_hyperbolic_cylinder_height(x2d, abs_p, abs_q, theta);
z2d = generate_2d_cylinder_height(@standard_concave_hyperbolic_cylinder_height, x2d, y2d, abs_p, abs_q, theta, x_i, z_i, alpha, beta, gamma);
fig_compare_2d_map(x1d, y1d, z2d, z2d_standard, 'Concave Hyperbolic Cylinder');

z1d_standard = standard_concave_hyperbolic_cylinder_height(x1d, abs_p, abs_q, theta);
z1d = generate_1d_height(@standard_concave_hyperbolic_cylinder_height, x1d, abs_p, abs_q, theta, x_i, z_i, beta);
fig_compare_1d_height(x1d, z1d, z1d_standard, 'Concave Hyperbolic Cylinder');

sx1d_standard = standard_concave_hyperbolic_cylinder_xslope(x1d, abs_p, abs_q, theta);
sx1d = generate_1d_slope(@standard_concave_hyperbolic_cylinder_xslope, x1d, abs_p, abs_q, theta, x_i, beta);
fig_compare_1d_slope(x1d, sx1d, sx1d_standard, 'Concave Hyperbolic Cylinder');


%% 8.1. Sagittal Collimating Diaboloid (SCD)

z2d_standard = standard_sag_col_diaboloid_height(x2d, y2d, abs_p, abs_q_t, theta);
z2d = generate_2d_curved_surface_height(@standard_sag_col_diaboloid_height, x2d, y2d, abs_p, abs_q_t, theta, x_i, y_i, z_i, alpha, beta, gamma);
fig_compare_2d_map(x1d, y1d, z2d, z2d_standard, 'Sagittal Collimating Diaboloid');


%% 8.2. Tangential Collimating Diaboloid (TCD)

z2d_standard = standard_tan_col_diaboloid_height(x2d, y2d, abs_p, abs_q_s, theta);
z2d = generate_2d_curved_surface_height(@standard_tan_col_diaboloid_height,x2d, y2d, abs_p, abs_q_s, theta, x_i, y_i, z_i, alpha, beta, gamma);
fig_compare_2d_map(x1d, y1d, z2d, z2d_standard, 'Tangential Collimating Diaboloid');
