% Demo script to calculate standard shapes

close all;
clear;
clc;

addpath('fig_show');
addpath('layer_01_standard');


%% 1. Lateral coordinates

x_range = 200e-3;
y_range = 20e-3;
x_num = 201;
y_num = 21;
x1d = linspace(-x_range/2, x_range/2, x_num);
y1d = linspace(-y_range/2, y_range/2, y_num);
[x2d, y2d] = meshgrid(x1d, y1d);

abs_p = 0.3;
abs_q = 30;
theta = 30e-3;


%% 2.1. Convex Ellipsoid (CVXE)

[z2d_quad_sln, z2d_expression] = standard_convex_ellipsoid_height(x2d, y2d, abs_p, abs_q, theta);
fig_compare_2d_map(x1d, y1d, z2d_quad_sln, z2d_expression, 'Convex Ellipsoid');


%% 2.2. Concave Ellipsoid (CCVE)

[z2d_quad_sln, z2d_expression] = standard_concave_ellipsoid_height(x2d, y2d, abs_p, abs_q, theta);
fig_compare_2d_map(x1d, y1d, z2d_quad_sln, z2d_expression, 'Concave Ellipsoid');


%% 3.1. Convex Elliptic Cylinder (CVXEC)

[z2d_quad_sln, z2d_expression] = standard_convex_elliptic_cylinder_height(x2d, abs_p, abs_q, theta);
fig_compare_2d_map(x1d, y1d, z2d_quad_sln, z2d_expression, 'Convex Elliptic Cylinder');

[z1d_quad_sln, z1d_expression] = standard_convex_elliptic_cylinder_height(x1d, abs_p, abs_q, theta);
fig_compare_1d_height(x1d, z1d_quad_sln, z1d_expression, 'Convex Elliptic Cylinder');

sx1d = standard_convex_elliptic_cylinder_xslope(x1d, abs_p, abs_q, theta);
fig_compare_1d_slope(x1d, sx1d, sx1d, 'Convex Elliptic Cylinder');


%% 3.2. Concave Elliptic Cylinder (CCVEC)

[z2d_quad_sln, z2d_expression] = standard_concave_elliptic_cylinder_height(x2d, abs_p, abs_q, theta);
fig_compare_2d_map(x1d, y1d, z2d_quad_sln, z2d_expression, 'Concave Elliptic Cylinder');

[z1d_quad_sln, z1d_expression] = standard_concave_elliptic_cylinder_height(x1d, abs_p, abs_q, theta);
fig_compare_1d_height(x1d, z1d_quad_sln, z1d_expression, 'Concave Elliptic Cylinder');

sx1d = standard_concave_elliptic_cylinder_xslope(x1d, abs_p, abs_q, theta);
fig_compare_1d_slope(x1d, sx1d, sx1d, 'Concave Elliptic Cylinder');


%% 6.1. Convex Hyperboloid (CVXH)

[z2d_quad_sln, z2d_expression] = standard_convex_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta);
fig_compare_2d_map(x1d, y1d, z2d_quad_sln, z2d_expression, 'Convex Hyperboloid');


%% 6.2. Concave Hyperboloid (CCVH)

[z2d_quad_sln, z2d_expression] = standard_concave_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta);
fig_compare_2d_map(x1d, y1d, z2d_quad_sln, z2d_expression, 'Concave Hyperboloid');


%% 7.1. Convex Hyperbolic Cylinder (CVXHC)

[z2d_quad_sln, z2d_expression] = standard_convex_hyperbolic_cylinder_height(x2d, abs_p, abs_q, theta);
fig_compare_2d_map(x1d, y1d, z2d_quad_sln, z2d_expression, 'Convex Hyperbolic Cylinder');

[z1d_quad_sln, z1d_expression] = standard_convex_hyperbolic_cylinder_height(x1d, abs_p, abs_q, theta);
fig_compare_1d_height(x1d, z1d_quad_sln, z1d_expression, 'Convex Hyperbolic Cylinder');

sx1d = standard_convex_hyperbolic_cylinder_xslope(x1d, abs_p, abs_q, theta);
fig_compare_1d_slope(x1d, sx1d, sx1d, 'Convex Hyperbolic Cylinder');


%% 7.2. Concave Hyperbolic Cylinder (CCVHC)

[z2d_quad_sln, z2d_expression] = standard_concave_hyperbolic_cylinder_height(x2d, abs_p, abs_q, theta);
fig_compare_2d_map(x1d, y1d, z2d_quad_sln, z2d_expression, 'Concave Hyperbolic Cylinder');

[z1d_quad_sln, z1d_expression] = standard_concave_hyperbolic_cylinder_height(x1d, abs_p, abs_q, theta);
fig_compare_1d_height(x1d, z1d_quad_sln, z1d_expression, 'Concave Hyperbolic Cylinder');

sx1d = standard_concave_hyperbolic_cylinder_xslope(x1d, abs_p, abs_q, theta);
fig_compare_1d_slope(x1d, sx1d, sx1d, 'Concave Hyperbolic Cylinder');
