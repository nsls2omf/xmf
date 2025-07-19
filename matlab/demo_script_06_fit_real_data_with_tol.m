% Demo script to fit real data with tolerance parameters

close all;
clear;
clc;

addpath('fig_show');
addpath('layer_01_standard');
addpath('layer_02_generation');
addpath('layer_03_optimization');
addpath('layer_04_fit');

% Set the pathname for real data
mat_data_pn = fullfile('..', 'real_data');


%% 1. Concave elliptic cylinder slope and height profiles 

mat_data_fn = 'sample_01_concave_elliptic_cylinder_slope.mat';
ffn = fullfile(mat_data_pn, mat_data_fn);
data = load(ffn);

x1d = data.x1d;
sx1d_measured = data.sx1d;
z1d_measured = calculate_1d_height_from_slope(sx1d_measured, x1d);
z1d_measured = remove_1d_tilt(x1d, z1d_measured);
input_params_struct = data.params_target;


%% 1.1. Concave elliptic cylinder slope 

% Parameter selection 1.....................................................

tol_struct.p = 0;
tol_struct.q = 0;
tol_struct.theta = 0;

[sx1d_res, sx1d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_ellipse_slope(x1d, sx1d_measured, input_params_struct, tol_struct);
fig_show_1d_fitting_slope(x1d, sx1d_measured, sx1d_fit, sx1d_res, input_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Elliptic Cylinder');


% Parameter selection 2.....................................................

tol_struct.p = 0;
tol_struct.q = 0;
tol_struct.theta = Inf;

[sx1d_res, sx1d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_ellipse_slope(x1d, sx1d_measured, input_params_struct, tol_struct);
fig_show_1d_fitting_slope(x1d, sx1d_measured, sx1d_fit, sx1d_res, input_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Elliptic Cylinder');


%% 1.2. Concave elliptic cylinder height

input_params_struct.z_i = 0;

% Parameter selection 1.....................................................

tol_struct.p = 0;
tol_struct.q = 0;
tol_struct.theta = 0;

[z1d_res, z1d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_ellipse_height(x1d, z1d_measured, input_params_struct, tol_struct);
fig_show_1d_fitting_height(x1d, z1d_measured, z1d_fit, z1d_res, input_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Elliptic Cylinder');


% Parameter selection 2.....................................................

tol_struct.p = 0;
tol_struct.q = 0;
tol_struct.theta = Inf;

[z1d_res, sx1d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_ellipse_height(x1d, z1d_measured, input_params_struct, tol_struct);
fig_show_1d_fitting_height(x1d, z1d_measured, z1d_fit, z1d_res, input_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Elliptic Cylinder');


%% 2. Concave hyperbolic cylinder height map

mat_data_fn = 'sample_02_concave_hyperbolic_cylinder_height_map.mat';
ffn = fullfile(mat_data_pn, mat_data_fn);
data = load(ffn);

x2d = data.x2d;
x1d = x2d(1, :);
y2d = data.y2d;
y1d = y2d(:, 1);
z2d_measured = data.z2d;
input_params_struct = data.params_target;

tol_struct.p = 0;
tol_struct.q = 0;
tol_struct.theta = 0;

[z2d_res, z2d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_hyperbolic_cylinder_height(x2d, y2d, z2d_measured, input_params_struct, tol_struct);
fig_show_2d_fitting_map(x1d, y1d, z2d_measured, z2d_fit, z2d_res, input_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Hyperbolic Cylinder');


%% 3. Concave ellipsoid height map

mat_data_fn = 'sample_03_concave_ellipsoid_height_map.mat';
ffn = fullfile(mat_data_pn, mat_data_fn);
data = load(ffn);

x2d = data.x2d;
x1d = x2d(1, :);
y2d = data.y2d;
y1d = y2d(:, 1);
z2d_measured = data.z2d;
input_params_struct = data.params_target;

tol_struct.p = 0;
tol_struct.q = 0;
tol_struct.theta = 0;
tol_struct.y_i = [-1e-3, 1e-3];

[z2d_res, z2d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_ellipsoid_height(x2d, y2d, z2d_measured, input_params_struct, tol_struct);
fig_show_2d_fitting_map(x1d, y1d, z2d_measured, z2d_fit, z2d_res, input_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Ellipsoid');


%% 4. Concave hyperboloid height map

mat_data_fn = 'sample_04_concave_hyperboloid_height_map.mat';
ffn = fullfile(mat_data_pn, mat_data_fn);
data = load(ffn);

x2d = data.x2d;
x1d = x2d(1, :);
y2d = data.y2d;
y1d = y2d(:, 1);
z2d_measured = data.z2d;
input_params_struct = data.params_target;

tol_struct.p = 0;
tol_struct.q = 0;
tol_struct.theta = 0;
tol_struct.y_i = [-1e-3, 1e-3];

[z2d_res, z2d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_hyperboloid_height(x2d, y2d, z2d_measured, input_params_struct, tol_struct);
fig_show_2d_fitting_map(x1d, y1d, z2d_measured, z2d_fit, z2d_res, input_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Hyperboloid');

