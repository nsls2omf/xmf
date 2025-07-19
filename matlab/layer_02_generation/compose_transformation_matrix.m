function [T, R, t] = compose_transformation_matrix(alpha, beta, gamma, x_i, y_i, z_i)
% compose_transformation_matrix(alpha, beta, gamma, x_i, y_i, z_i) - Composes a transformation matrix
%   that includes rotation and translation based on the provided angles and translations.
%
%   Inputs:
%       - alpha - Rotation angle along x-axis in radians
%       - beta - Rotation angle along y-axis in radians
%       - gamma - Rotation angle along z-axis in radians
%       - x_i - x-translation in the conversion from standard mirror coordinates to metrology coordinates
%       - y_i - y-translation in the conversion from standard mirror coordinates to metrology coordinates
%       - z_i - z-translation in the conversion from standard mirror coordinates to metrology coordinates
%   
%   Outputs:
%       - T - Transformation matrix (4x4)
%       - R - Rotation matrix (3x3)
%       - t - Translation vector (3x1)

R_x = [1, 0, 0; 0, cos(alpha), -sin(alpha); 0, sin(alpha), cos(alpha)];
R_y = [cos(beta), 0, sin(beta); 0, 1, 0; -sin(beta), 0, cos(beta)];
R_z = [cos(gamma), -sin(gamma), 0; sin(gamma), cos(gamma), 0; 0, 0, 1];

R = R_z * R_y * R_x;
t = [x_i; y_i; z_i];
T = [R, t; 0, 0, 0, 1];