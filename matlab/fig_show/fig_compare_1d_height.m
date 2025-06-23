function fig_compare_1d_height(x1d, z1d, z1d_nominal, str_title)

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
