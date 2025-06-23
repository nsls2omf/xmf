function fig_show_1d_slope(x1d, sx1d, sx1d_quadrics, str_title)

x1d_mm = x1d*1e3;
sx1d_mrad = sx1d*1e3;
sx1d_quadrics_mrad = sx1d_quadrics*1e3;
dsx1d_nrad = (sx1d - sx1d_quadrics)*1e9;


figure;
tiledlayout(2,1, 'TileSpacing', 'normal');

nexttile;
plot(x1d_mm, sx1d_mrad, 'LineWidth', 3); hold on;
plot(x1d_mm, sx1d_quadrics_mrad, '--', 'LineWidth', 3); 
set(gca, 'xTickLabel', []);
ylabel('sx [mrad]');
title(str_title);


nexttile;
plot(x1d_mm, dsx1d_nrad, 'o', 'MarkerSize', 8, 'MarkerFaceColor', 'r');
set(gca, 'xTickLabel', []);
ylabel('sx [nrad]');
title(sprintf('Difference: %.3g nrad RMS', nanstd(dsx1d_nrad, 1)));
