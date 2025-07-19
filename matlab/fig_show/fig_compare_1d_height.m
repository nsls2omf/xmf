function fig_compare_1d_height(x1d, z1d, z1d_nominal, str_title)
% fig_compare_1d_height - Show the comparison of 1D height data against nominal values
%  This function plots the measured height data and the nominal height data
%
%  Input:   
%           - x1d - 1D lateral coordinates [m]
%           - z1d - Measured height data [m]
%           - z1d_nominal - Nominal height data [m]
%           - str_title - Title string for the figure

x1d_mm = x1d*1e3;
z1d_um = z1d*1e6;
z1d_nominal_um = z1d_nominal*1e6;
dz1d_nm = (z1d - z1d_nominal)*1e9;

figure;
tiledlayout(2,1, 'TileSpacing', 'normal');

nexttile;
plot(x1d_mm, z1d_um, 'LineWidth', 3); 
hold on;
plot(x1d_mm, z1d_nominal_um, '--', 'LineWidth', 3); 
set(gca, 'xTickLabel', []);
ylabel('z [µm]');
title(str_title);

nexttile;
plot(x1d_mm, dz1d_nm, 'o', 'MarkerSize', 8, 'MarkerFaceColor', 'r'); 
xlabel('x [mm]');
ylabel('z [nm]');
title(sprintf('Difference: %.3g nm RMS', nanstd(dz1d_nm, 1)));
