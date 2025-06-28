function [v_res, v_fit, opt_params_structure, params_ci_structure, init_params] = optimize_parameters_with_tol(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, input_params_structure, tol_structure)
% optimize_parameters_with_tol provide a convenient way to optimize the  
% surface parameters with tolerance from the measurement data.
%
%    Input:
%        surface_generation_function_handle is function handle for surface
%           generation
%        standard_surface_shape_function_handle is function handle for a 
%           standard surface shape 
%        x is the measured x-coordinate, in unit of [m] as a suggestion
%        y is the measured y-coordinate, in unit of [m] as a suggestion
%        v is the measured slope or height in [rad] or [m] as a suggestion
%        input_params_structure contains p, q, theta, x_i(optional), 
%           y_i(optional), z_i(optional), alpha(optional), beta(optional)  
%           and gamma(optional) target parameters, suggested in unit of 
%           [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
%        tol_structure is a structure to set the tolerance values for 
%           p, q, theta, x_i, y_i, z_i, alpha, beta, gamma.
%
%    Output:
%        v_res is the residual in [m], if the input x and z are in [m]
%        v_fit is fitting result in [m], if the input x and z are in [m]
%        opt_params_structure is the optimized params in structure
%        params_ci_structure is the confidence intervals of the pamrams
%        init_params contains the used initial parameters.

%   Copyright since 2023 by Lei Huang. All Rights Reserved.
%   E-mail: huanglei0114@gmail.com
%   v1.0.2023.11.19 basic version
%   v1.1.2025.01.20 rename some variables
%   v2.0.2025.03.25 general version
%   v2.1.2025.06.24 general version with tolerance


% Set parameters...........................................................

% Initial values
init_params = check_input_params_structure(input_params_structure, x, y, v);

% Tolerance values
[is_opt_vector, tol_vector] = check_tol_structure(tol_structure, surface_generation_function_handle);

% Use NaN to identify the parameters which are required to optimize
fix_params = init_params;
fix_params(is_opt_vector) = nan;
params = init_params(is_opt_vector); % Only optimize parameters required to optimize

% Determine the lower and upper boundaries
lb = params + tol_vector(is_opt_vector, 1);
ub = params + tol_vector(is_opt_vector, 2);

% Set optimization options.................................................
opt_options = optimset( ...
    'MaxFunEvals', 1e6 ...
    , 'MaxIter', 1e2 ...
    , 'TolFun', 1e-14 ...
    , 'TolX', 1e-16 ...
    , 'Algorithm','levenberg-marquardt' ... 'trust-region-reflective', 'levenberg-marquardt', 'interior-point'
    , 'Display', 'Iter' ...
    );


% Optimize parameters......................................................
[opt_params, ~, residual, ~, ~, ~, jacobian] ...
    = lsqnonlin(@(params)cost_function_for_optimizaiton(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, fix_params, params), params ...
    , lb, ub, opt_options);

singular_vals = svd(jacobian);
cond_number = max(singular_vals) / min(singular_vals);
fprintf('Condition number: %.2e\n', cond_number);

% Release the result in a structure for better understanding
params_result = fix_params;
params_result(is_opt_vector) = opt_params;

opt_params_structure.p = params_result(1);
opt_params_structure.q = params_result(2);
opt_params_structure.theta = params_result(3);
opt_params_structure.x_i = params_result(4);
opt_params_structure.y_i = params_result(5);
opt_params_structure.z_i = params_result(6);
opt_params_structure.alpha = params_result(7);
opt_params_structure.beta = params_result(8);
opt_params_structure.gamma = params_result(9);


% Calcualte the confidence intervals.......................................

confidence_interval = nlparci(opt_params, residual, 'Jacobian', jacobian);
params_ci_result = nan(size(fix_params, 1), 2);
params_ci_result(is_opt_vector, :) = confidence_interval;

params_ci_structure.p = params_ci_result(1, :);
params_ci_structure.q = params_ci_result(2, :);
params_ci_structure.theta = params_ci_result(3, :);
params_ci_structure.x_i = params_ci_result(4, :);
params_ci_structure.y_i = params_ci_result(5, :);
params_ci_structure.z_i = params_ci_result(6, :);
params_ci_structure.alpha = params_ci_result(7, :);
params_ci_structure.beta = params_ci_result(8, :);
params_ci_structure.gamma = params_ci_result(9, :);


% Recalculate the fitting and residual.....................................

[~, v_fit, v_res] = cost_function_for_optimizaiton(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, fix_params, opt_params);

end




%% Subfunctions

% Check input parameters...................................................
function init_params = check_input_params_structure(input_params_structure, x, y, v)

if isfield(input_params_structure, 'p')
    p = input_params_structure.p; % [m]
else
    error('p value is mandatory.');
end

if isfield(input_params_structure, 'q')
    q = input_params_structure.q; % [m]
else
    error('q value is mandatory.');
end

if isfield(input_params_structure, 'theta')
    theta = input_params_structure.theta; % [rad]
else
    error('theta value is mandatory.');
end

if isfield(input_params_structure, 'x_i')
    x_i = input_params_structure.x_i; % [m]
else
    x_i = mean(x(isfinite(v(:))), "omitnan"); % [m]
end

if isfield(input_params_structure, 'y_i')
    y_i = input_params_structure.y_i; % [m]
else
    y_i = mean(y(isfinite(v(:))), "omitnan"); % [m]
end

if isfield(input_params_structure, 'z_i')
    z_i = input_params_structure.z_i; % [m] 
else
    z_i = 0; % [m]
end

if isfield(input_params_structure, 'alpha')
    alpha = input_params_structure.alpha; % [rad]
else
    alpha = 0; % [rad]
end

if isfield(input_params_structure, 'beta')
    beta = input_params_structure.beta; % [rad]
else
    beta = 0; % [rad]
end

if isfield(input_params_structure, 'gamma')
    gamma = input_params_structure.gamma; % [rad]
else
    gamma = 0; % [rad]
end

% Initial values
init_params = [p; q; theta; x_i; y_i; z_i; alpha; beta; gamma];

end



% Check optimization flags.................................................
function [is_opt_vector, tol_vector] = check_tol_structure(tol_structure, surface_generation_function_handle)

% Set the default optimization flags based on the surface data
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


% Set field names in cell
field_names = {'p', 'q', 'theta', 'x_i', 'y_i', 'z_i', 'alpha', 'beta', 'gamma'};

tol_vector = zeros(9, 2);
for num = 1:9
    % Unify the tolerance structure format as two boundaries
    tol_structure = unify_tol_structure_format(tol_structure, field_names{num}, is_opt_vector(num));
    
    % Update the user defined optimization flags
    is_opt_vector(num) = ~all(tol_structure.(field_names{num})==0);

    % Update the tolerance vector
    tol_vector(num, :) = tol_structure.(field_names{num});
end

end

% Unify tolerance structure format
function tol_structure = unify_tol_structure_format(tol_structure, str_field_name, is_opt)

if isfield(tol_structure, str_field_name)
    assert(numel(tol_structure.(str_field_name))<=2);
    if isscalar(tol_structure.(str_field_name))
        tol_structure.(str_field_name) = [-1, 1] * tol_structure.(str_field_name); 
    end
else
    if (true==is_opt)
        tol_structure.(str_field_name) = [-inf, inf];
    else
        tol_structure.(str_field_name) = [0, 0];
    end
end

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
