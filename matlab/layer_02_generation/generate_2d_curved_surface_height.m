function z2d ... 2D curved surface height map
    = generate_2d_curved_surface_height ... generation function
    ( standard_height_function_handle ... handle of the standard height function
    , x2d ... 2D x-coordinates
    , y2d ... 2D y-coordinates
    , p ... Distance between the source and the chief ray intersection on mirror
    , q ... Distance between the focus and the chief ray intersection on mirror
    , theta ... Grazing incidence angle
    , x_i ... x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
    , y_i ... y-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the y-position of chief ray intersection in metrology coordinates
    , z_i ... z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
    , alpha ... Rotation angle along x-axis in standard mirror coordinates
    , beta ... Rotation angle along y-axis in standard mirror coordinates
    , gamma ... Rotation angle along z-axis in standard mirror coordinates
    , z2d_measured ... (Optional) The height map from metrology
    )
% generate_2d_curved_surface_height(standard_height_function_handle, x2d, y2d, p, q, theta, x_i, y_i, z_i, alpha, beta, gamma, z2d_measured) 
% - Generates a 2D height map for a curved surface
%   
%   Inputs:
%       - standard_height_function_handle - Handle to the standard height function (e.g., standard_sag_col_diaboloid_height)
%       - x2d - 2D x-coordinates (vector or matrix)
%       - y2d - 2D y-coordinates (vector or matrix)
%       - p - Distance between the source and the chief ray intersection on mirror
%       - q - Distance between the focus and the chief ray intersection on mirror
%       - theta - Grazing incidence angle (in radians)
%       - x_i - x-translation in the conversion from standard mirror coordinates to metrology coordinates
%       - y_i - y-translation in the conversion from standard mirror coordinates to metrology coordinates
%       - z_i - z-translation in the conversion from standard mirror coordinates to metrology coordinates
%       - alpha - Rotation angle along x-axis in standard mirror coordinates
%       - beta - Rotation angle along y-axis in standard mirror coordinates
%       - gamma - Rotation angle along z-axis in standard mirror coordinates
%       - z2d_measured - (Optional) The height map from metrology, if available
%   
%   Outputs:
%       - z2d - 2D height map of the curved surface in metrology coordinates

if nargin < 13
    % If no information on measured height, simply assumping it is flat.
    % This is OK for most grazing incidence X-ray mirrors.
    z2d_measured = zeros(size(x2d));
end

tf = compose_transformation_matrix(alpha, beta, gamma, x_i, y_i, z_i);
z2d = iter_genereate_height(standard_height_function_handle, x2d, y2d, p, q, theta, tf, z2d_measured);