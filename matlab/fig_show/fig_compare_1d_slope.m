function fig_compare_1d_slope(x1d, sx1d, sx1d_nominal, str_title)

x1d_mm = x1d*1e3;
sx1d_mrad = sx1d*1e3;
sx1d_nominal_mrad = sx1d_nominal*1e3;
dsx1d_urad = (sx1d - sx1d_nominal)*1e6;

figure;
tiledlayout(2, 1, 'TileSpacing', 'normal');

nexttile;
plot(x1d_mm, sx1d_mrad, 'LineWidth', 3); 
hold on;
plot(x1d_mm, sx1d_nominal_mrad, '--', 'LineWidth', 3); 
set(gca, 'xTickLabel', []);
ylabel('x-slope [mrad]');
title(str_title);

nexttile;
plot(x1d_mm, dsx1d_urad, 'o', 'MarkerSize', 8, 'MarkerFaceColor', 'r'); 
xlabel('x [mm]');
ylabel('x-slope [µrad]');
title(sprintf('Difference: %.3g µrad RMS', nanstd(dsx1d_urad, 1)));
