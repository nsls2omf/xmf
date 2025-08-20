function fig_show_1d_fitting_height(x1d, z1d_measured, z1d_fit, z1d_res, input_params_struct, opt_params_struct, opt_params_ci_struct, str_title)
% fig_show_1d_fitting_height - Show the fitting results of 1D height data
%
%  Input:   
%           - x1d - 1D lateral coordinates [m]
%           - z1d_measured - Measured height data [m]
%           - z1d_fit - Fitted height data [m]
%           - z1d_res - Residuals [m]
%           - input_params_struct - Input parameters structure
%           - opt_params_struct - Optimized parameters structure
%           - opt_params_ci_struct - Confidence intervals structure
%           - str_title - Title string for the figure

x1d_mm = x1d*1e3;
z1d_measured_um = z1d_measured*1e6;
z1d_fit_um = z1d_fit*1e6;
z1d_res_nm = z1d_res*1e9;

cs = lines(7);
font_size = 20;
large_font_size = 24;
marker_size = 6;
line_width = 4;

figure('Position', [100, 100, 1500, 600]);
tiledlayout(3, 5 ...
    , 'TileSpacing', 'tight' ...
    , 'Padding', 'tight' ...
    );

% Data
nexttile([2, 3]);
plot(x1d_mm, z1d_measured_um, 'o', 'MarkerSize', 8); 
hold on;
plot(x1d_mm, z1d_fit_um, 'LineWidth', line_width); 
plot(opt_params_struct.x_i*1e3, interp1(x1d_mm, z1d_fit_um, opt_params_struct.x_i*1e3), 'ro', 'MarkerSize', marker_size*2, 'MarkerFaceColor', 'r'); 
set(gca, 'xTickLabel', []);
ylabel('z [µm]');
title(str_title);


nexttile([1, 2]);
text(0.5, 1, 'Input parameters:' ...
    , 'Units', 'normalized' ...
    , 'FontSize', large_font_size ...
    , 'HorizontalAlignment', 'Center' ...
    , 'FontWeight', 'Bold' ...
    , 'Color', 'k' ...
    );
text(0, 0.4, parameter_to_string(input_params_struct) ...
    , 'Units', 'normalized' ...
    , 'FontSize', font_size ...
    , 'HorizontalAlignment', 'Left' ...
    , 'Interpreter', 'latex' ...
    );
axis off;

nexttile([1, 2]);
text(0.5, 1, 'Resultant parameters:' ...
    , 'Units', 'normalized' ...
    , 'FontSize', large_font_size ...
    , 'HorizontalAlignment', 'Center' ...
    , 'FontWeight', 'Bold' ...
    , 'Color', cs(2,:) ...
    );
text(0, 0.4, parameter_to_string(opt_params_struct, opt_params_ci_struct) ...
    , 'Units', 'normalized' ...
    , 'FontSize', font_size ...
    , 'HorizontalAlignment', 'Left' ...
    , 'Interpreter', 'latex' ...
    );
axis off;

% Residual
nexttile([1, 3]);
plot([min(x1d_mm), max(x1d_mm)], [0, 0], 'k');
hold on;
plot(x1d_mm, z1d_res_nm, 'o-' ...
    , 'MarkerSize', marker_size ...
    , 'MarkerFaceColor', cs(1,:) ...
    , 'MarkerEdgeColor', cs(1,:) ...
    , 'Color', cs(1,:) ...
    );
xlabel('x [mm]');
ylabel('Residual [nm]');

ax = nexttile([1, 2]);
str_rms = sprintf('Residual:\n%.2f nm RMS', nanstd(z1d_res_nm, 1));
text(ax, 0.5, 0.5, str_rms ...
    , 'Units', 'normalized' ...
    , 'FontSize', large_font_size ...
    , 'FontWeight', 'Bold' ...
    , 'HorizontalAlignment', 'center' ...
    , 'Color', cs(1,:) ...
    );
axis off;



function cell = parameter_to_string(params, params_ci)

if nargin == 1

    str_1 = sprintf('($p$, $q$, $\\theta$) = ($%.4g$ m, $%.4g$ m, $%.4g$ mrad)' ...
        , params.p...
        , params.q ...
        , params.theta * 1e3 ...
        );
    str_2 = sprintf('($x_i$, $z_i$) = ($%.4g$ mm, $%.4g$ mm)' ...
        , params.x_i * 1e3 ...
        , params.z_i * 1e3 ...
        );
    str_3 = sprintf('$\\beta$ = $%.4g$ $\\mu$rad' ...
        , params.beta * 1e6 ...
        );
    str_1 = reg_exp_rep(str_1);
    str_2 = reg_exp_rep(str_2);
    str_3 = reg_exp_rep(str_3);
    cell = {str_1, str_2, str_3};
elseif nargin == 2
    
    [str_p, str_q, str_theta, str_x_i, str_z_i, str_beta] = get_height_string(params_ci);

    str_1 = sprintf('($%s$, $%s$, $%s$) = ($%.4g$ m, $%.4g$ m, $%.4g$ mrad)' ...
        , str_p ...
        , str_q ...
        , str_theta ...
        , params.p...
        , params.q ...
        , params.theta * 1e3 ...
        );
    str_2 = sprintf('($%s$, $%s$) = ($%.4g$ mm, $%.4g$ mm)' ...
        , str_x_i ...
        , str_z_i ...
        , params.x_i * 1e3 ...
        , params.z_i * 1e3 ...
        );
    str_3 = sprintf('$%s$ = $%.4g$ $\\mu$rad' ...
        , str_beta ...
        , params.beta * 1e6 ...
        );
    str_1 = reg_exp_rep(str_1);
    str_2 = reg_exp_rep(str_2);
    str_3 = reg_exp_rep(str_3);
    cell = {str_1, str_2, str_3};
else
    error('Unexpected input argument numbers.');
end



function str_expression = reg_exp_rep(str_expression)

str_expression = regexprep(str_expression, 'e\+?0*(\d+)', '\\times10^{$1}');
str_expression = regexprep(str_expression, 'e-0*(\d+)', '\\times10^{- $1}');





function [str_p, str_q, str_theta, str_x_i, str_z_i, str_beta] = get_height_string(params_ci)

if if_opt(params_ci.p)
    str_p = '\hat{p}';
else
    % str_p = '\underline{p}';
    str_p = 'p';
end

if if_opt(params_ci.q)
    str_q = '\hat{q}';
else
    % str_q = '\underline{q}';
    str_q = 'q';
end

if if_opt(params_ci.theta)
    str_theta = '\hat{\theta}';
else
    % str_theta = '\underline{\theta}';
    str_theta = '\theta';
end

if if_opt(params_ci.x_i)
    str_x_i = '\hat{x_i}';
else
    % str_x_i = '\underline{x_i}';
    str_x_i = 'x_i';
end

if if_opt(params_ci.z_i)
    str_z_i = '\hat{z_i}';
else
    % str_z_i = '\underline{z_i}';
    str_z_i = 'z_i';
end

if if_opt(params_ci.beta)
    str_beta = '\hat{\beta}';
else
    % str_beta = '\underline{\beta}';
    str_beta = '\beta';
end




function b_res = if_opt(ci)
b_res = all(isfinite(ci));
