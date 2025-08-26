function sx1d = generate_1d_slope(standard_slope_function_handle, x1d, p, q, theta, x_i, beta)
% generate_1d_slope - Generates a 1D slope profile for a grazing incidence X-ray mirror
%   
%   Inputs:
%       - standard_slope_function_handle - Handle to the standard slope function
%       - x1d - 1D x-coordinates (vector)
%       - p - Distance between the source and the chief ray intersection on mirror
%       - q - Distance between the focus and the chief ray intersection on mirror
%       - theta - Grazing incidence angle (in radians)
%       - x_i - x-translation in the conversion from standard mirror coordinates to metrology coordinates
%       - beta - Rotation angle along y-axis in standard mirror coordinates
%
%   Outputs:
%       - sx1d - 1D slope profile of the grazing incidence X-ray mirror in metrology coordinates

arguments
    standard_slope_function_handle function_handle
    x1d double
    p (1,1) double {mustBePositive}
    q (1,1) double {mustBePositive}
    theta (1,1) double {mustBeReal}
    x_i (1,1) double {mustBeReal} = mean(x1d, 'omitnan') % Default to the mean of x1d if not provided
    beta (1,1) double {mustBeReal} = 0; % Default to 0 if not provided
end

x1d = x1d - x_i;
sx1d = standard_slope_function_handle(x1d, p, q, theta);
sx1d = sx1d - tan(beta); % Note: the direction of beta