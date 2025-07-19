function [z_quad_sln, z_expression] = standard_left_hyperbolic_cylinder_height(x, abs_p, abs_q, theta)
% standard_left_hyperbolic_cylinder_height(x, abs_p, abs_q, theta) - Computes the height of a left hyperbolic cylinder
%   at a given x-coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).
%
%   Inputs:
%       - x - 2D x-coordinates (vector or matrix)
%       - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
%       - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
%       - theta - Grazing incidence angle (in radians)
%
%   Outputs:
%       - z_quad_sln - Quadratic solution for the left hyperbolic cylinder height
%       - z_expression - Expression for the left hyperbolic cylinder height

% Quadratic solution.......................................................

A = (abs_p-abs_q).^2 - (abs_p+abs_q).^2.*sin(theta).^2;
B = 2*x.*(abs_p+abs_q)*(abs_p-abs_q)*sin(theta)*cos(theta) - 4*abs_p*abs_q*(abs_p-abs_q)*sin(theta);
C = (abs_p-abs_q).^2.*x.^2.*sin(theta).^2;

% Discriminant 
Delta = B.^2 - 4*A.*C;

if abs_p > abs_q % left and p>q, means concave hyperbolic cylinder
    z_quad_sln = (-B - sqrt(Delta))./(2.*A);
else % left and p<q, means convex hyperbolic cylinder
    z_quad_sln = (-B + sqrt(Delta))./(2.*A);
end
z_quad_sln(Delta<0) = nan;


% Expression...............................................................

z_expression = (abs_p-abs_q)*sin(theta).*(-x.*(abs_p+abs_q).*cos(theta) + 2*abs_p*abs_q - 2*sqrt(abs_p*abs_q*x.^2 - abs_p*abs_q*(abs_p+abs_q).*x.*cos(theta) + abs_p.^2*abs_q.^2))./((abs_p-abs_q).^2-(abs_p+abs_q).^2.*sin(theta).^2);
z_expression(imag(z_expression)~=0) = nan;
