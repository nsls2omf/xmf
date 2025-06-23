function [v_res, v_fit, params, params_ci] = optimize_parameters(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, params_input, is_opt_structure)
% optimize_parameters provide a convenient way to optimize the surface 
% parameters with measurement results.
%
%    Input:
%        surface_generation_function_handle is function handle for surface
%           generation
%        standard_surface_shape_function_handle is function handle for a 
%           standard surface shape 
%        x is the measured x-coordinate, in unit of [m] as a suggestion
%        y is the measured y-coordinate, in unit of [m] as a suggestion
%        v is the measured slope or height in [rad] or [m] as a suggestion
%        param_input is the p, q, theta, x_i(optional), y_i(optional), 
%           z_i(optional), alpha(optional), beta(optional) and 
%           gamma(optional) target parameters, suggested in unit of 
%           [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
%        is_opt_structure is a structure to set whether optimization is 
%           needed for p, q, theta, x_i, y_i, z_i, alpha, beta, gamma.
%
%    Output:
%        v_res is the residual in [m], if the input x and z are in [m]
%        v_fit is fitting result in [m], if the input x and z are in [m]
%        params is the optimized params in structure
%        params_ci is the confidence intervals of the pamrams.

%   Copyright since 2023 by Lei Huang. All Rights Reserved.
%   E-mail: huanglei0114@gmail.com
%   v1.0.2023.11.19 basic version
%   v1.1.2025.01.20 rename some variables
%   v2.0.2025.03.25 general version

%#ok<*NANMEAN>

% Set parameters...........................................................

% Initial values
param_init = check_input_params(params_input, x, y, v);

% optimization flags
is_opt_vector = check_is_opt(is_opt_structure, surface_generation_function_handle);

% Use NaN to identify the parameters which are required to optimize
param_fix = param_init;
param_fix(is_opt_vector) = nan;
param = param_init(is_opt_vector); % Only optimize parameters required to optimize


% Set optimization options.................................................
opt_options = optimset( ...
    'MaxFunEvals', 1e6 ...
    , 'MaxIter', 1e3 ...
    , 'TolFun', 1e-10 ...
    , 'TolX', 1e-10 ...
    , 'Algorithm','levenberg-marquardt' ... 'trust-region-reflective', 'levenberg-marquardt', 'interior-point'
    , 'Display', 'Iter' ...
    );


% Optimize parameters......................................................

[param_opt, ~, residual, ~, ~, ~, jacobian] ...
    = lsqnonlin(@(param)cost_function_for_optimizaiton(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, param_fix, param), param ...
    , [], [], opt_options);

% Release the result in a structure for better understanding
param_result = param_fix;
param_result(is_opt_vector) = param_opt;

params.p = param_result(1);
params.q = param_result(2);
params.theta = param_result(3);
params.x_i = param_result(4);
params.y_i = param_result(5);
params.z_i = param_result(6);
params.alpha = param_result(7);
params.beta = param_result(8);
params.gamma = param_result(9);


% Calcualte the confidence intervals.......................................

confidence_interval = nlparci(param_opt, residual, 'Jacobian', jacobian);
param_ci_result = nan(size(param_fix, 1), 2);
param_ci_result(is_opt_vector, :) = confidence_interval;

params_ci.p = param_ci_result(1, :);
params_ci.q = param_ci_result(2, :);
params_ci.theta = param_ci_result(3, :);
params_ci.x_i = param_ci_result(4, :);
params_ci.y_i = param_ci_result(5, :);
params_ci.z_i = param_ci_result(6, :);
params_ci.alpha = param_ci_result(7, :);
params_ci.beta = param_ci_result(8, :);
params_ci.gamma = param_ci_result(9, :);


% Recalculate the fitting and residual.....................................

[~, v_fit, v_res] = cost_function_for_optimizaiton(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, param_fix, param_opt);

end




%% Subfunctions

% Check input parameters...................................................
function param_init = check_input_params(params_input, x, y, v)

if isfield(params_input, 'p')
    p = params_input.p; % [m]
else
    error('p value is mandatory.');
end

if isfield(params_input, 'q')
    q = params_input.q; % [m]
else
    error('q value is mandatory.');
end

if isfield(params_input, 'theta')
    theta = params_input.theta; % [rad]
else
    error('theta value is mandatory.');
end

if isfield(params_input, 'x_i')
    x_i = params_input.x_i; % [m]
else
    x_i = nanmean(x(isfinite(v(:)))); % [m]
end

if isfield(params_input, 'y_i')
    y_i = params_input.y_i; % [m]
else
    y_i = nanmean(y(isfinite(v(:)))); % [m]
end

if isfield(params_input, 'z_i')
    z_i = params_input.z_i; % [m] 
else
    z_i = 0; % [m]
end

if isfield(params_input, 'alpha')
    alpha = params_input.alpha; % [rad]
else
    alpha = 0; % [rad]
end

if isfield(params_input, 'beta')
    beta = params_input.beta; % [rad]
else
    beta = 0; % [rad]
end

if isfield(params_input, 'gamma')
    gamma = params_input.gamma; % [rad]
else
    gamma = 0; % [rad]
end

% Initial values
param_init = [p; q; theta; x_i; y_i; z_i; alpha; beta; gamma];

end



% Check optimization flags.................................................
function is_opt_vector = check_is_opt(is_opt_structure, surface_generation_function_handle)

% Default optimization flags
is_opt_vector = false(9, 1);
if isequal(surface_generation_function_handle, @generate_2d_curved_surface_height)
    is_opt_vector(4:end) = true; % x_i, y_i, z_i, alpha, beta, gamma
elseif isequal(surface_generation_function_handle, @generate_2d_cylinder_height)
    is_opt_vector(4) = true; % x_i
    is_opt_vector(6) = true; % z_i
    is_opt_vector(7:9) = true; % alpha, beta, gamma
elseif isequal(surface_generation_function_handle, @generate_1d_height)
    is_opt_vector(4) = true; % x_i
    is_opt_vector(6) = true; % z_i
    is_opt_vector(8) = true; % beta
elseif isequal(surface_generation_function_handle, @generate_1d_slope)
    is_opt_vector(4) = true; % x_i
    is_opt_vector(8) = true; % beta
end

% Update the user defined optimization flags
if isfield(is_opt_structure, 'p'), is_opt_vector(1) = is_opt_structure.p; end
if isfield(is_opt_structure, 'q'), is_opt_vector(2) = is_opt_structure.q; end
if isfield(is_opt_structure, 'theta'), is_opt_vector(3) = is_opt_structure.theta; end
if isfield(is_opt_structure, 'x_i'), is_opt_vector(4) = is_opt_structure.x_i; end
if isfield(is_opt_structure, 'y_i'), is_opt_vector(5) = is_opt_structure.y_i; end
if isfield(is_opt_structure, 'z_i'), is_opt_vector(6) = is_opt_structure.z_i; end
if isfield(is_opt_structure, 'alpha'), is_opt_vector(7) = is_opt_structure.alpha; end
if isfield(is_opt_structure, 'beta'), is_opt_vector(8) = is_opt_structure.beta; end
if isfield(is_opt_structure, 'gamma'), is_opt_vector(9) = is_opt_structure.gamma; end

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
