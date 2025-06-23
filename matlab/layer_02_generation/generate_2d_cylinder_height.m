% Generate 2D cylinder height with rotation and translation
% function z2d = generate_2d_cylinder_height(standard_height_function_handle, x2d, y2d, p, q, theta, x_i, y_i, z_i, alpha, beta, gamma, z2d_measured)

function z2d ... 2D cylinder surface height map
    = generate_2d_cylinder_height ... generation function
    ( standard_height_function_handle ... handle of the standard height function
    , x2d ... 2D x-coordinates
    , y2d ... 2D y-coordinates
    , p ... Distance between the source and the chief ray intersection on mirror
    , q ... Distance between the focus and the chief ray intersection on mirror
    , theta ... Grazing incidence angle
    , x_i ... x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
    , z_i ... z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
    , alpha ... Rotation angle along x-axis in standard mirror coordinates
    , beta ... Rotation angle along y-axis in standard mirror coordinates
    , gamma ... Rotation angle along z-axis in standard mirror coordinates
    , z2d_measured ... (Optional) The height map from metrology
    )

if nargin < 12
    z2d_measured = zeros(size(x2d)); % If
end

y_i = 0; % No need to consider y-position of the chief ray intersection for cylinders
tf = compose_transformation_matrix(alpha, beta, gamma, x_i, y_i, z_i);
z2d = iter_genereate_height(standard_height_function_handle, x2d, y2d, p, q, theta, tf, z2d_measured);