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
% generate_2d_cylinder_height(standard_height_function_handle, x2d, y2d, p, q, theta, x_i, z_i, alpha, beta, gamma, z2d_measured)
% - Generates a 2D height map for a circular cylinder
%   
%   Inputs:
%       - standard_height_function_handle - Handle to the standard height function (e.g., standard_circular_cylinder_height)
%       - x2d - 2D x-coordinates (vector or matrix)
%       - y2d - 2D y-coordinates (vector or matrix)
%       - p - Distance between the source and the chief ray intersection on mirror
%       - q - Distance between the focus and the chief ray intersection on mirror
%       - theta - Grazing incidence angle (in radians)
%       - x_i - x-translation in the conversion from standard mirror coordinates to metrology coordinates
%       - z_i - z-translation in the conversion from standard mirror coordinates to metrology coordinates
%       - alpha - Rotation angle along x-axis in standard mirror coordinates
%       - beta - Rotation angle along y-axis in standard mirror coordinates
%       - gamma - Rotation angle along z-axis in standard mirror coordinates
%       - z2d_measured - (Optional) The height map from metrology, if available
%   
%   Outputs:
%       - z2d - 2D height map of the circular cylinder in metrology coordinates

arguments
    standard_height_function_handle function_handle
    x2d double
    y2d double
    p (1,1) double {mustBePositive}
    q (1,1) double {mustBePositive}
    theta (1,1) double {mustBeReal}
    x_i (1,1) double {mustBeReal} = mean(x2d(:), 'omitnan') % Default to the mean of x2d if not provided
    z_i (1,1) double {mustBeReal} = 0; % Default to 0 if not provided
    alpha (1,1) double {mustBeReal} = 0; % Default to 0 if not provided
    beta (1,1) double {mustBeReal} = 0; % Default to 0 if not provided
    gamma (1,1) double {mustBeReal} = 0; % Default to 0 if not provided
    z2d_measured double {mustBeReal} = zeros(size(x2d)); % Default to flat if not provided
end

y_i = 0; % No need to consider y-position of the chief ray intersection for cylinders
tf = compose_transformation_matrix(alpha, beta, gamma, x_i, y_i, z_i);
z2d = iter_genereate_height(standard_height_function_handle, x2d, y2d, p, q, theta, tf, z2d_measured);