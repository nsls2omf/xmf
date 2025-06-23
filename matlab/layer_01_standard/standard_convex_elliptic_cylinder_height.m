function varargout = standard_convex_elliptic_cylinder_height(x, abs_p, abs_q, theta)

% Give the sign to p and q based on mirror type
p = -abs_p;
q = -abs_q;  

if nargout == 1

    z2d_quad_sln_quadrics = standard_quadric_cylinder_height(x, p, q, theta);
    varargout{1} = z2d_quad_sln_quadrics;

elseif nargout == 2

    [z2d_quad_sln_quadrics, z2d_expression_quadrics] = standard_quadric_cylinder_height(x, p, q, theta);
    varargout{1} = z2d_quad_sln_quadrics;
    varargout{2} = z2d_expression_quadrics;

elseif nargout == 4

    [z2d_quad_sln_quadrics, z2d_expression_quadrics] = standard_quadric_cylinder_height(x, p, q, theta);
    z2d_quad_sln_with_abs = quad_sln_with_abs(x, abs_p, abs_q, theta);
    z2d_expression_with_abs = expression_with_abs(x, abs_p, abs_q, theta);
    varargout{1} = z2d_quad_sln_quadrics;
    varargout{2} = z2d_expression_quadrics;
    varargout{3} = z2d_quad_sln_with_abs;
    varargout{4} = z2d_expression_with_abs;

else

    error('Unsupported number of outputs.');

end







% Quadratic solution with absolute values of p and q.......................

function z2d_quad_sln_with_abs = quad_sln_with_abs(x, abs_p, abs_q, theta)

A = (abs_p+abs_q).^2 - (abs_p-abs_q).^2.*sin(theta).^2;
B = 2*x.*(abs_p+abs_q)*(abs_p-abs_q)*sin(theta)*cos(theta) + 4*abs_p*abs_q*(abs_p+abs_q)*sin(theta);
C = (abs_p+abs_q).^2.*x.^2.*sin(theta).^2;

% Discriminant 
Delta = B.^2 - 4*A.*C;

z2d_quad_sln_with_abs = (-B + sqrt(Delta))./(2.*A);
z2d_quad_sln_with_abs(Delta<0) = nan;





% Expression with absolute values of p and q...............................

function z2d_expression_with_abs = expression_with_abs(x, abs_p, abs_q, theta)  

z2d_expression_with_abs = (abs_p+abs_q)*sin(theta).*(-x.*(abs_p-abs_q).*cos(theta) - 2*abs_p*abs_q + 2.*sqrt(-abs_p*abs_q*x.^2 + abs_p*abs_q*(abs_p-abs_q).*x.*cos(theta) + abs_p.^2*abs_q.^2))./((abs_p+abs_q).^2-(abs_p-abs_q).^2.*sin(theta).^2);
z2d_expression_with_abs(imag(z2d_expression_with_abs)~=0) = nan;
