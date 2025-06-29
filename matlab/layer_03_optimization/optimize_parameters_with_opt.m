function [v_res, v_fit, opt_params_struct, opt_params_ci_struct, init_params] = optimize_parameters_with_opt(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, input_params_struct, opt_struct)
% optimize_parameters provide a convenient way to optimize the surface 
% parameters from measurement data.
%
%    Input:
%        surface_generation_function_handle is function handle for surface
%           generation
%        standard_surface_shape_function_handle is function handle for a 
%           standard surface shape 
%        x is the measured x-coordinate, in unit of [m] as a suggestion
%        y is the measured y-coordinate, in unit of [m] as a suggestion
%        v is the measured slope or height in [rad] or [m] as a suggestion
%        input_params_struct contains p, q, theta, x_i(optional), 
%           y_i(optional), z_i(optional), alpha(optional), beta(optional)  
%           and gamma(optional) target parameters, suggested in unit of 
%           [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
%        opt_struct is a structure to set whether optimization is 
%           needed for p, q, theta, x_i, y_i, z_i, alpha, beta, gamma.
%
%    Output:
%        v_res is the residual in [m], if the input x and z are in [m]
%        v_fit is fitting result in [m], if the input x and z are in [m]
%        opt_params_struct is the optimized params in structure
%        opt_params_ci_struct is the confidence intervals of the pamrams
%        init_params contains the used initial parameters.

%   Copyright since 2023 by Lei Huang. All Rights Reserved.
%   E-mail: huanglei0114@gmail.com
%   v1.0.2023.11.19 basic version
%   v1.1.2025.01.20 rename some variables
%   v2.0.2025.03.25 general version


% Set parameters...........................................................

% Initial values
init_params = check_input_params(input_params_struct, x, y, v);

% optimization flags
opt_vector = check_opt_struct(opt_struct, surface_generation_function_handle);

% Use NaN to identify the parameters which are required to optimize
fix_params = init_params;
fix_params(opt_vector) = nan;
params = init_params(opt_vector); % Only optimize parameters required to optimize


% Set optimization options.................................................
opt_options = optimset( ...
    'MaxFunEvals', 1e6 ...
    , 'MaxIter', 1e2 ...
    , 'TolFun', 1e-14 ...
    , 'TolX', 1e-16 ...
    , 'Algorithm', 'levenberg-marquardt' ... 'trust-region-reflective', 'levenberg-marquardt', 'interior-point'
    , 'Display', 'none' ...
    );


% Optimize parameters......................................................
lb = [];
ub = [];
[opt_params, ~, residual, ~, ~, ~, jacobian] ...
    = lsqnonlin(@(params)cost_function_for_optimizaiton(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, fix_params, params), params ...
    , lb, ub, opt_options);

% Release the result in a structure for better understanding
params_result = fix_params;
params_result(opt_vector) = opt_params;

opt_params_struct.p = params_result(1);
opt_params_struct.q = params_result(2);
opt_params_struct.theta = params_result(3);
opt_params_struct.x_i = params_result(4);
opt_params_struct.y_i = params_result(5);
opt_params_struct.z_i = params_result(6);
opt_params_struct.alpha = params_result(7);
opt_params_struct.beta = params_result(8);
opt_params_struct.gamma = params_result(9);


% Calcualte the confidence intervals.......................................

confidence_interval = nlparci(opt_params, residual, 'Jacobian', jacobian);
params_ci_result = nan(size(fix_params, 1), 2);
params_ci_result(opt_vector, :) = confidence_interval;

opt_params_ci_struct.p = params_ci_result(1, :);
opt_params_ci_struct.q = params_ci_result(2, :);
opt_params_ci_struct.theta = params_ci_result(3, :);
opt_params_ci_struct.x_i = params_ci_result(4, :);
opt_params_ci_struct.y_i = params_ci_result(5, :);
opt_params_ci_struct.z_i = params_ci_result(6, :);
opt_params_ci_struct.alpha = params_ci_result(7, :);
opt_params_ci_struct.beta = params_ci_result(8, :);
opt_params_ci_struct.gamma = params_ci_result(9, :);


% Recalculate the fitting and residual.....................................

[~, v_fit, v_res] = cost_function_for_optimizaiton(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, fix_params, opt_params);

end




%% Subfunctions

% Check input parameters...................................................
function init_params = check_input_params(input_params_struct, x, y, v)

if isfield(input_params_struct, 'p')
    p = input_params_struct.p; % [m]
else
    error('p value is mandatory.');
end

if isfield(input_params_struct, 'q')
    q = input_params_struct.q; % [m]
else
    error('q value is mandatory.');
end

if isfield(input_params_struct, 'theta')
    theta = input_params_struct.theta; % [rad]
else
    error('theta value is mandatory.');
end

if isfield(input_params_struct, 'x_i')
    x_i = input_params_struct.x_i; % [m]
else
    x_i = mean(x(isfinite(v(:))), "omitnan"); % [m]
end

if isfield(input_params_struct, 'y_i')
    y_i = input_params_struct.y_i; % [m]
else
    y_i = mean(y(isfinite(v(:))), "omitnan"); % [m]
end

if isfield(input_params_struct, 'z_i')
    z_i = input_params_struct.z_i; % [m] 
else
    z_i = 0; % [m]
end

if isfield(input_params_struct, 'alpha')
    alpha = input_params_struct.alpha; % [rad]
else
    alpha = 0; % [rad]
end

if isfield(input_params_struct, 'beta')
    beta = input_params_struct.beta; % [rad]
else
    beta = 0; % [rad]
end

if isfield(input_params_struct, 'gamma')
    gamma = input_params_struct.gamma; % [rad]
else
    gamma = 0; % [rad]
end

% Initial values
init_params = [p; q; theta; x_i; y_i; z_i; alpha; beta; gamma];

end



% Check optimization flags.................................................
function opt_vector = check_opt_struct(opt_struct, surface_generation_function_handle)

% Default optimization flags
opt_vector = false(9, 1);
if isequal(surface_generation_function_handle, @generate_2d_curved_surface_height)
    opt_vector(4:end) = true; % x_i, y_i, z_i, alpha, beta, gamma
elseif isequal(surface_generation_function_handle, @generate_2d_cylinder_height)
    opt_vector(4) = true; % x_i
    opt_vector(6) = true; % z_i
    opt_vector(7:9) = true; % alpha, beta, gamma
elseif isequal(surface_generation_function_handle, @generate_1d_height)
    opt_vector(4) = true; % x_i
    opt_vector(6) = true; % z_i
    opt_vector(8) = true; % beta
elseif isequal(surface_generation_function_handle, @generate_1d_slope)
    opt_vector(4) = true; % x_i
    opt_vector(8) = true; % beta
end

% Update the user defined optimization flags
if isfield(opt_struct, 'p'), opt_vector(1) = opt_struct.p; end
if isfield(opt_struct, 'q'), opt_vector(2) = opt_struct.q; end
if isfield(opt_struct, 'theta'), opt_vector(3) = opt_struct.theta; end
if isfield(opt_struct, 'x_i'), opt_vector(4) = opt_struct.x_i; end
if isfield(opt_struct, 'y_i'), opt_vector(5) = opt_struct.y_i; end
if isfield(opt_struct, 'z_i'), opt_vector(6) = opt_struct.z_i; end
if isfield(opt_struct, 'alpha'), opt_vector(7) = opt_struct.alpha; end
if isfield(opt_struct, 'beta'), opt_vector(8) = opt_struct.beta; end
if isfield(opt_struct, 'gamma'), opt_vector(9) = opt_struct.gamma; end

end





% Cost function for optimizaiton...........................................
function [v1d_valid_res, v_fit, v_res] = cost_function_for_optimizaiton(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, param_fix, param)
%
% param_fix is the list of fixed parameters, and param is the list of
% parametres to optimize. It is important to have them always in the same
% order as p, q, theta, x_i, y_i, z_i, alpha, beta, gamma.
% The optimized parameters are those set as NaN.

% Update parameters which need optimization................................
param_update = param_fix;
param_update(isnan(param_fix)) = param;

% Release the input parameters.............................................
p = param_update(1);
q = param_update(2);
theta = param_update(3);
x_i = param_update(4);
y_i = param_update(5);
z_i = param_update(6);
alpha = param_update(7);
beta = param_update(8);
gamma = param_update(9);

% Generate surface height with (p, q, theta),
% considering tranformation with x_i, y_i, z_i, alpha, beta, gamma.........
if isequal(surface_generation_function_handle, @generate_2d_curved_surface_height)
    v_fit = surface_generation_function_handle(standard_surface_shape_function_handle, x, y, p, q, theta, x_i, y_i, z_i, alpha, beta, gamma, v);
elseif isequal(surface_generation_function_handle, @generate_2d_cylinder_height)
    v_fit = surface_generation_function_handle(standard_surface_shape_function_handle, x, y, p, q, theta, x_i, z_i, alpha, beta, gamma, v);
elseif isequal(surface_generation_function_handle, @generate_1d_height)
    v_fit = surface_generation_function_handle(standard_surface_shape_function_handle, x, p, q, theta, x_i, z_i, beta, v);
elseif isequal(surface_generation_function_handle, @generate_1d_slope)
    v_fit = surface_generation_function_handle(standard_surface_shape_function_handle, x, p, q, theta, x_i, beta);
end

% Calculte the valid residual height as the output of the cost function....
v_res = v - v_fit;
v1d_valid_res = v_res(isfinite(v_res));

end
