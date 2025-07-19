function [z2d_quad_sln, z2d_expression] = standard_quadric_cylinder_height(x2d, p, q, theta)
% standard_quadric_cylinder_height(x2d, p, q, theta) - Computes the height of a quadric cylinder
%   at a given x-coordinate, based on the parameters p and q and the grazing incidence angle (theta).
%   
%   Inputs:
%       - x2d - 2D x-coordinates (vector or matrix)
%       - p - Distance between the source and the chief ray intersection on mirror
%       - q - Distance between the focus and the chief ray intersection on mirror
%       - theta - Grazing incidence angle (in radians)
%   
%   Outputs:
%       - z2d_quad_sln - Quadratic solution for the quadric cylinder height
%       - z2d_expression - Expression for the quadric cylinder height

% Quadratic solution.......................................................

A = (p+q).^2 - (p-q).^2.*sin(theta).^2;
B = 2*x2d.*(p+q)*(p-q)*sin(theta)*cos(theta) - 4*p*q*(p+q)*sin(theta);
C = (p+q).^2.*(x2d.^2.*sin(theta).^2);

% Discriminant 
Delta = B.^2 - 4*A.*C;

if (p < 0 && q < 0) % Top (convex) elliptic cylinder
    z2d_quad_sln = (-B + sqrt(Delta))./(2.*A);
elseif (p > 0 && q > 0) % Bottom (concave) elliptic cylinder
    z2d_quad_sln = (-B - sqrt(Delta))./(2.*A);
elseif (p < 0 && q > 0) % Left hyperbolic cylinder
    if (abs(p) <= abs(q)) % Left convex hyperbolic cylinder
        z2d_quad_sln = (-B + sqrt(Delta))./(2.*A);
    else % Left concave hyperbolic cylinder
        z2d_quad_sln = (-B - sqrt(Delta))./(2.*A);
    end
elseif (p > 0 && q < 0) % Right hyperbolic cylinder
    if (abs(p) >= abs(q)) % Right convex hyperbolic cylinder
        z2d_quad_sln = (-B + sqrt(Delta))./(2.*A);
    else % Right concave hyperbolic cylinder
        z2d_quad_sln = (-B - sqrt(Delta))./(2.*A);
    end
end

z2d_quad_sln(Delta<0) = nan;


% Expression...............................................................

if (p*q>0) % Elliptical cylinder
    z2d_expression = (p+q)*sin(theta).*(-x2d.*(p-q).*cos(theta) + 2*p*q - sqrt(-4*p*q*x2d.^2 - 4*p*q*(p-q).*x2d.*cos(theta) + 4*p.^2*q.^2))./((p+q).^2-(p-q).^2.*sin(theta).^2);
elseif (p*q < 0) % Hyperbolic cylinder
    z2d_expression = (p+q)*sin(theta).*(-x2d.*(p-q).*cos(theta) + 2*p*q + sqrt(-4*p*q*x2d.^2 - 4*p*q*(p-q).*x2d.*cos(theta) + 4*p.^2*q.^2))./((p+q).^2-(p-q).^2.*sin(theta).^2);
end
z2d_expression(imag(z2d_expression)~=0) = nan;

