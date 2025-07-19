function varargout = standard_convex_hyperbolic_cylinder_height(x, abs_p, abs_q, theta)
% standard_convex_hyperbolic_cylinder_height(x, abs_p, abs_q, theta) - Computes the height of a convex hyperbolic cylinder
%   at a given x-coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).
%   
%   Inputs:
%       - x - 2D x-coordinates (vector or matrix)
%       - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
%       - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
%       - theta - Grazing incidence angle (in radians)
%   
%   Outputs:
%       - z2d_quad_sln_quadrics - Quadratic solution for the convex hyperbolic cylinder height
%       - z2d_expression_quadrics - Expression for the convex hyperbolic cylinder height

% Give the sign to p and q based on mirror type
if abs(abs_p) > abs(abs_q)
    p = abs_p;
    q = - abs_q;
else
    p = - abs_p;
    q = abs_q;
end

if nargout == 1

    z2d_quad_sln_quadrics = standard_quadric_cylinder_height(x, p, q, theta);
    varargout{1} = z2d_quad_sln_quadrics;

elseif nargout == 2

    [z2d_quad_sln_quadrics, z2d_expression_quadrics] = standard_quadric_cylinder_height(x, p, q, theta);
    varargout{1} = z2d_quad_sln_quadrics;
    varargout{2} = z2d_expression_quadrics;

elseif nargout == 4

    [z2d_quad_sln_quadrics, z2d_expression_quadrics] = standard_quadric_cylinder_height(x, p, q, theta);
    [z2d_quad_sln_with_abs, z2d_expression_with_abs] = sln_with_abs(x, abs_p, abs_q, theta);
    varargout{1} = z2d_quad_sln_quadrics;
    varargout{2} = z2d_expression_quadrics;
    varargout{3} = z2d_quad_sln_with_abs;
    varargout{4} = z2d_expression_with_abs;

else

    error('Unsupported number of outputs.');

end





% Solutions with absolute values of p and q................................

function [z_quad_sln_with_abs, z_expression_with_abs] = sln_with_abs(x, abs_p, abs_q, theta)

if abs_p > abs_q
    [z_quad_sln_with_abs, z_expression_with_abs] = standard_right_hyperbolic_cylinder_height(x, abs_p, abs_q, theta);
else
    [z_quad_sln_with_abs, z_expression_with_abs] = standard_left_hyperbolic_cylinder_height(x, abs_p, abs_q, theta);
end