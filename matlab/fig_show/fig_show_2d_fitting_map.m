function fig_show_2d_fitting_map(x1d, y1d, z2d_measured, z2d_fit, z2d_res, input_params_struct, opt_params_struct, opt_params_ci_struct, str_title)
% fig_show_2d_fitting_map - Show the fitting results of 2D map data
%
%  Input:   
%           - x1d - 1D lateral coordinates [m]
%           - y1d - 1D lateral coordinates [m]
%           - z2d_measured - 2D measured data [m]
%           - z2d_fit - 2D fitted data [m]
%           - z2d_res - 2D residuals [m]
%           - input_params_struct - Input parameters structure
%           - opt_params_struct - Optimized parameters structure
%           - opt_params_ci_struct - Confidence intervals structure
%           - str_title - Title string for the figure

x1d_mm = x1d*1e3;
y1d_mm = y1d*1e3;
z2d_um = z2d_measured*1e6;
z2d_fit_um = z2d_fit*1e6;
z2d_res_nm = z2d_res*1e9;

font_size = 16;
large_font_size = 20;
marker_size = 6;

figure('Position', [100, 100, 1200, 600]);
tiledlayout(3, 2 ...
    , 'TileSpacing', 'tight' ...
    , 'Padding', 'tight' ...
    );

% Data
nexttile;
imagesc(x1d_mm, y1d_mm, z2d_um);
set(gca, 'xTickLabel', []);
ylabel('y [mm]');
title(str_title)
hcb = colorbar;
title(hcb, '[µm]');
axis xy;

nexttile;
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

% Fit
nexttile;
imagesc(x1d_mm, y1d_mm, z2d_fit_um);
hold on;
plot(opt_params_struct.x_i*1e3, opt_params_struct.y_i*1e3, 'ro', 'MarkerSize', marker_size*2, 'MarkerFaceColor', 'r');
% Calculate the projection of beam direction on the mirror surface
proj_x = cos(opt_params_struct.gamma)*range(x1d)*0.08;
proj_y = sin(opt_params_struct.gamma)*range(x1d)*0.08;
quiver(opt_params_struct.x_i*1e3 - proj_x*1e3, opt_params_struct.y_i*1e3 - proj_y*1e3, 2*proj_x*1e3, 2*proj_y*1e3, 0, 'Color', 'r', 'LineWidth', 2);
set(gca, 'xTickLabel', []);
ylabel('y [mm]');
title('Fitting')
hcb = colorbar;
title(hcb, '[µm]');
axis xy;

nexttile;
text(0.5, 1, 'Resultant parameters:' ...
    , 'Units', 'normalized' ...
    , 'FontSize', large_font_size ...
    , 'HorizontalAlignment', 'Center' ...
    , 'FontWeight', 'Bold' ...
    , 'Color', 'k' ...
    );
text(0, 0.4, parameter_to_string(opt_params_struct, opt_params_ci_struct) ...
    , 'Units', 'normalized' ...
    , 'FontSize', font_size ...
    , 'HorizontalAlignment', 'Left' ...
    , 'Interpreter', 'latex' ...
    );
axis off;

% Residual
ax = nexttile;
imagesc(x1d_mm, y1d_mm, z2d_res_nm);
xlabel('x [mm]');
ylabel('y [mm]');
title('Residual');
hcb = colorbar;
title(hcb, '[nm]');
axis xy;
colormap(ax, 'vik');

nexttile;
str_rms = sprintf('Residual:\n%.2f nm RMS', nanstd(z2d_res_nm(:), 1));
text(0.5, 0.5, str_rms ...
    , 'Units', 'normalized' ...
    , 'FontSize', large_font_size ...
    , 'FontWeight', 'Bold' ...
    , 'HorizontalAlignment', 'center' ...
    , 'Color', 'k' ...
    );
axis off;

function cell = parameter_to_string(params, params_ci)

if nargin == 1
    if ~isfield(params, 'x_i')
        params.x_i = nan;
    end
    if ~isfield(params, 'z_i')
        params.z_i = nan;
    end
    if ~isfield(params, 'alpha')
        params.alpha = nan;   
    end
    if ~isfield(params, 'beta')
        params.beta = nan;   
    end
    if ~isfield(params, 'gamma')
        params.gamma = nan;   
    end
 
    if isfield(params, 'y_i')
        assert(numel(params.p)<=2);
        assert(numel(params.q)<=2);
        
        if isscalar(params.p)
            str_p_value = sprintf('%.4g ', params.p);
        elseif numel(params.p)==2
            str_p_value = sprintf('[%.4g, %.4g]', params.p(1), params.p(2));
        end
        if isscalar(params.q)
            str_q_value = sprintf('%.4g ', params.q);
        elseif numel(params.q)==2
            str_q_value = sprintf('[%.4g, %.4g]', params.q(1), params.q(2));
        end
        str_1 = sprintf('($p$, $q$, $\\theta$) = ($%s$ m, $%s$ m, $%.4g$ mrad)' ...
            , str_p_value ...
            , str_q_value ...
            , params.theta * 1e3 ...
            );
        str_2 = sprintf('($x_i$, $y_i$, $z_i$) = ($%.4g$ mm, $%.4g$ mm, $%.4g$ mm)' ...
            , params.x_i * 1e3 ...
            , params.y_i * 1e3 ...
            , params.z_i * 1e3 ...
            );
        str_3 = sprintf('($\\alpha$, $\\beta$, $\\gamma$) = ($%.4g$ $\\mu$rad, $%.4g$ $\\mu$rad, $%.4g$ $\\mu$rad)' ...
            , params.alpha * 1e6 ...
            , params.beta * 1e6 ...
            , params.gamma * 1e6 ...
            );
        str_1 = reg_exp_rep(str_1);
        str_2 = reg_exp_rep(str_2);
        str_3 = reg_exp_rep(str_3);
        cell = {str_1, str_2, str_3};
    else
        str_1 = sprintf('($p$, $q$, $\\theta$) = ($%.4g$ m, $%.4g$ m, $%.4g$ mrad)' ...
            , params.p ...
            , params.q ...
            , params.theta * 1e3 ...
            );
        str_2 = sprintf('($x_i$, $z_i$) = ($%.4g$ mm, $%.4g$ mm)' ...
            , params.x_i * 1e3 ...
            , params.z_i * 1e3 ...
            );
        str_3 = sprintf('($\\alpha$, $\\beta$, $\\gamma$) = ($%.4g$ $\\mu$rad, $%.4g$ $\\mu$rad, $%.4g$ $\\mu$rad)' ...
            , params.alpha * 1e6 ...
            , params.beta * 1e6 ...
            , params.gamma * 1e6 ...
            );
        str_1 = reg_exp_rep(str_1);
        str_2 = reg_exp_rep(str_2);
        str_3 = reg_exp_rep(str_3);
        cell = {str_1, str_2, str_3};
    end

elseif nargin == 2
    
    [str_p, str_q, str_theta, str_x_i, str_y_i, str_z_i, str_alpha, str_beta, str_gamma] = get_height_map_string(params_ci);
    
    if isfield(params, 'y_i')
        assert(numel(params.p)<=2);
        assert(numel(params.q)<=2);
        
        if isscalar(params.p)
            str_p_value = sprintf('%.4g ', params.p);
        elseif numel(params.p)==2
            str_p_value = sprintf('[%.4g, %.4g]', params.p(1), params.p(2));
        end
        if isscalar(params.q)
            str_q_value = sprintf('%.4g ', params.q);
        elseif numel(params.q)==2
            str_q_value = sprintf('[%.4g, %.4g]', params.q(1), params.q(2));
        end
        str_1 = sprintf('($%s$, $%s$, $%s$) = ($%s$ m, $%s$ m, $%.4g$ mrad)' ...
            , str_p ...
            , str_q ...
            , str_theta ...
            , str_p_value ...
            , str_q_value ...
            , params.theta * 1e3 ...
            );
        str_2 = sprintf('($%s$, $%s$, $%s$) = ($%.4g$ mm, $%.4g$ mm, $%.4g$ mm)' ...
            , str_x_i ...
            , str_y_i ...
            , str_z_i ...
            , params.x_i * 1e3 ...
            , params.y_i * 1e3 ...
            , params.z_i * 1e3 ...
            );
        str_3 = sprintf('($%s$, $%s$, $%s$) = ($%.4g$ $\\mu$rad, $%.4g$ $\\mu$rad, $%.4g$ $\\mu$rad)' ...
            , str_alpha ...
            , str_beta ...
            , str_gamma ...
            , params.alpha * 1e6 ...
            , params.beta * 1e6 ...
            , params.gamma * 1e6 ...
            );
        str_1 = reg_exp_rep(str_1);
        str_2 = reg_exp_rep(str_2);
        str_3 = reg_exp_rep(str_3);
        cell = {str_1, str_2, str_3};
    else
        str_1 = sprintf('($p$, $q$, $\\theta$) = ($%.4g$ m, $%.4g$ m, $%.4g$ mrad)' ...
            , params.p ...
            , params.q ...
            , params.theta * 1e3 ...
            );
        str_2 = sprintf('($x_i$, $z_i$) = ($%.4g$ mm, $%.4g$ mm)' ...
            , params.x_i * 1e3 ...
            , params.z_i * 1e3 ...
            );
        str_3 = sprintf('($\\alpha$, $\\beta$, $\\gamma$) = ($%.4g$ $\\mu$rad, $%.4g$ $\\mu$rad, $%.4g$ $\\mu$rad)' ...
            , params.alpha * 1e6 ...
            , params.beta * 1e6 ...
            , params.gamma * 1e6 ...
            );
        str_1 = reg_exp_rep(str_1);
        str_2 = reg_exp_rep(str_2);
        str_3 = reg_exp_rep(str_3);
        cell = {str_1, str_2, str_3};
    end

else
    error('Unexpected input argument numbers.');
end



function str_expression = reg_exp_rep(str_expression)

str_expression = regexprep(str_expression, 'e\+?0*(\d+)', '\\times10^{$1}');
str_expression = regexprep(str_expression, 'e-0*(\d+)', '\\times10^{- $1}');






function [str_p, str_q, str_theta, str_x_i, str_y_i, str_z_i, str_alpha, str_beta, str_gamma] = get_height_map_string(params_ci)

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

if if_opt(params_ci.y_i)
    str_y_i = '\hat{y_i}';
else
    % str_y_i = '\underline{y_i}';
    str_y_i = 'y_i';
end

if if_opt(params_ci.z_i)
    str_z_i = '\hat{z_i}';
else
    % str_z_i = '\underline{z_i}';
    str_z_i = 'z_i';
end

if if_opt(params_ci.alpha)
    str_alpha = '\hat{\alpha}';
else
    % str_alpha = '\underline{\alpha}';
    str_alpha = '\alpha';
end

if if_opt(params_ci.beta)
    str_beta = '\hat{\beta}';
else
    % str_beta = '\underline{\beta}';
    str_beta = '\beta';
end

if if_opt(params_ci.gamma)
    str_gamma = '\hat{\gamma}';
else
    % str_beta = '\underline{\gamma}';
    str_gamma = '\gamma';
end




function b_res = if_opt(ci)
b_res = all(isfinite(ci));
