function [T, R, t] = compose_transformation_matrix(alpha, beta, gamma, x_i, y_i, z_i)

R_x = [1, 0, 0; 0, cos(alpha), -sin(alpha); 0, sin(alpha), cos(alpha)];
R_y = [cos(beta), 0, sin(beta); 0, 1, 0; -sin(beta), 0, cos(beta)];
R_z = [cos(gamma), -sin(gamma), 0; sin(gamma), cos(gamma), 0; 0, 0, 1];

R = R_z * R_y * R_x;
t = [x_i; y_i; z_i];
T = [R, t; 0, 0, 0, 1];