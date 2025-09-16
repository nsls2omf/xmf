function z2d_quad_sln = standard_sag_col_diaboloid_height(x2d, y2d, abs_p, abs_q, theta)
% standard_sag_col_diaboloid_height(x2d, y2d, abs_p, abs_q, theta) - Computes the height of a sagittal collimating diaboloid
%   at a given (x, y) coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).
%   
%   Inputs:
%       - x2d - 2D x-coordinates (vector or matrix)
%       - y2d - 2D y-coordinates (vector or matrix)
%       - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
%       - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
%       - theta - Grazing incidence angle (in radians)
%   
%   Outputs:
%       - z2d_quad_sln - Quadratic solution for the sagittal collimating diaboloid height

% Quadratic solution.......................................................

A = (abs_p-abs_q).^2.*cos(theta).^2 + 4*abs_p*abs_q;
B = (abs_p-abs_q)*sin(theta).*y2d.^2 + (abs_p^2-abs_q^2)*sin(2*theta)*x2d - 4*(abs_p+abs_q).*abs_p.*abs_q.*sin(theta);
C = (abs_p+abs_q).^2*sin(theta).^2.*x2d.^2 - (abs_p+abs_q)*(cos(theta).*x2d - abs_q).*y2d.^2 - 0.25*y2d.^4;

% Discriminant 
Delta = B.^2 - 4*A.*C;

z2d_quad_sln = (-B - sqrt(Delta))./(2.*A);
z2d_quad_sln(Delta<0) = nan;

