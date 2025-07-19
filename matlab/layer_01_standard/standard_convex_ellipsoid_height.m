function varargout = standard_convex_ellipsoid_height(x2d, y2d, abs_p, abs_q, theta)
% standard_convex_ellipsoid_height(x2d, y2d, abs_p, abs_q, theta) - Computes the height of a convex ellipsoid
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
%       - z2d_quad_sln_quadrics - Quadratic solution for the convex ellipsoid height
%       - z2d_expression_quadrics - Expression for the convex ellipsoid height

% Give the sign to p and q based on mirror type
p = -abs_p;
q = -abs_q;  

if nargout == 1

    z2d_quad_sln_quadrics = standard_quadrics_height(x2d, y2d, p, q, theta);
    varargout{1} = z2d_quad_sln_quadrics;

elseif nargout == 2

    [z2d_quad_sln_quadrics, z2d_expression_quadrics] = standard_quadrics_height(x2d, y2d, p, q, theta);
    varargout{1} = z2d_quad_sln_quadrics;
    varargout{2} = z2d_expression_quadrics;

elseif nargout == 4

    [z2d_quad_sln_quadrics, z2d_expression_quadrics] = standard_quadrics_height(x2d, y2d, p, q, theta);
    z2d_quad_sln_with_abs = quad_sln_with_abs(x2d, y2d, abs_p, abs_q, theta);
    z2d_expression_with_abs = expression_with_abs(x2d, y2d, abs_p, abs_q, theta);
    varargout{1} = z2d_quad_sln_quadrics;
    varargout{2} = z2d_expression_quadrics;
    varargout{3} = z2d_quad_sln_with_abs;
    varargout{4} = z2d_expression_with_abs;

else

    error('Unsupported number of outputs.');

end








% Quadratic solution with absolute values of p and q.......................

function z2d_quad_sln_with_abs = quad_sln_with_abs(x2d, y2d, abs_p, abs_q, theta)
    
A = (abs_p+abs_q).^2 - (abs_p-abs_q).^2.*sin(theta).^2;
B = 2*x2d.*(abs_p+abs_q)*(abs_p-abs_q)*sin(theta)*cos(theta) + 4*abs_p*abs_q*(abs_p+abs_q)*sin(theta);
C = (abs_p+abs_q).^2.*(x2d.^2.*sin(theta).^2 + y2d.^2);

% Discriminant 
Delta = B.^2 - 4*A.*C;

z2d_quad_sln_with_abs = (-B + sqrt(Delta))./(2.*A);
z2d_quad_sln_with_abs(Delta<0) = nan;
    
    




% Expression with absolute values of p and q...............................

function z2d_expression_with_abs = expression_with_abs(x2d, y2d, abs_p, abs_q, theta)    

z2d_expression_with_abs = (abs_p+abs_q)*sin(theta).*(-x2d.*(abs_p-abs_q).*cos(theta) - 2*abs_p*abs_q + sqrt(-4*abs_p*abs_q*x2d.^2 + 4*abs_p*abs_q*(abs_p-abs_q).*x2d.*cos(theta) + 4*abs_p.^2*abs_q.^2 - ((abs_p+abs_q).^2-(abs_p-abs_q).^2.*sin(theta).^2).*y2d.^2./sin(theta).^2))./((abs_p+abs_q).^2-(abs_p-abs_q).^2.*sin(theta).^2);
z2d_expression_with_abs(imag(z2d_expression_with_abs)~=0) = nan;