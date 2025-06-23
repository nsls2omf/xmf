function fig_show_2d_maps(x1d, y1d, z2d, z2d_quad_sln, str_title)

x1d_mm = x1d*1e3;
y1d_mm = y1d*1e3;
z2d_um = z2d*1e6;
z2d_quad_sln_um = z2d_quad_sln*1e6;
dz2d_nm = (z2d - z2d_quad_sln)*1e9;


figure;
tiledlayout(3,1, 'TileSpacing', 'normal');

nexttile;
imagesc(x1d_mm, y1d_mm, z2d_um);
set(gca, 'xTickLabel', []);
ylabel('y [mm]');
title(str_title)
hcb = colorbar;
title(hcb, '[µm]');
axis xy;

nexttile;
imagesc(x1d_mm, y1d_mm, z2d_quad_sln_um);
set(gca, 'xTickLabel', []);
ylabel('y [mm]');
hcb = colorbar;
title(hcb, '[µm]');
axis xy;

nexttile;
imagesc(x1d_mm, y1d_mm, dz2d_nm);
xlabel('x [mm]');
ylabel('y [mm]');
title(sprintf('Difference: %.3g nm RMS', nanstd(dz2d_nm(:), 1)));
hcb = colorbar;
title(hcb, '[nm]');axis xy;
axis xy;
