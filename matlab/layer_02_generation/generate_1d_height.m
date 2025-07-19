function z1d ... 1D height profile
    = generate_1d_height ... generation function
    ( standard_height_function_handle ... handle of the standard height function
    , x1d ... 1D x-coordinates
    , p ... Distance between the source and the chief ray intersection on mirror
    , q ... Distance between the focus and the chief ray intersection on mirror
    , theta ... Grazing incidence angle
    , x_i ... x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
    , z_i ... z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
    , beta ... Rotation angle along y-axis in standard mirror coordinates
    , z1d_measured ... (Optional) The height map from metrology
    )
% generate_1d_height - Generates a 1D height profile for a grazing incidence X-ray mirror
%   
%   Inputs:
%       - standard_height_function_handle - Handle to the standard height function (e.g., standard_circular_cylinder_height)
%       - x1d - 1D x-coordinates (vector)
%       - p - Distance between the source and the chief ray intersection on mirror
%       - q - Distance between the focus and the chief ray intersection on mirror
%       - theta - Grazing incidence angle (in radians)
%       - x_i - x-translation in the conversion from standard mirror coordinates to metrology coordinates
%       - z_i - z-translation in the conversion from standard mirror coordinates to metrology coordinates
%       - beta - Rotation angle along y-axis in standard mirror coordinates
%       - z1d_measured - (Optional) The height map from metrology, if available
%   
%   Outputs:
%       - z1d - 1D height profile of the grazing incidence X-ray mirror in metrology coordinates

if nargin < 9
    % If no information on measured height, simply assumping it is flat.
    % This is OK for most grazing incidence X-ray mirrors.
    z1d_measured = zeros(size(x1d)); 
end

y_i = 0; % No need to consider y-position of the chief ray intersection for cylinders
alpha = 0; % No need to consider rotation along x-axis for 1D case
gamma = 0; % No need to consider rotation along z-axis for 1D case
tf = compose_transformation_matrix(alpha, beta, gamma, x_i, y_i, z_i);

y1d = zeros(size(x1d)); % No need to consider y-coordiantes in metrology coordinates
z1d = iter_genereate_height(standard_height_function_handle, x1d, y1d, p, q, theta, tf, z1d_measured);
