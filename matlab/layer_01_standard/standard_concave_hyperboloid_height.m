function varargout = standard_concave_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta)
% standard_concave_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta) - Computes the height of a concave hyperboloid
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
%       - z2d_quad_sln_quadrics - Quadratic solution for the concave hyperboloid height
%       - z2d_expression_quadrics - Expression for the concave hyperboloid height

% Give the sign to p and q based on mirror type
if abs(abs_p) > abs(abs_q)
    p = - abs_p;
    q = abs_q;
else
    p = abs_p;
    q = - abs_q;
end

if nargout == 1

    z2d_quad_sln_quadrics = standard_quadrics_height(x2d, y2d, p, q, theta);
    varargout{1} = z2d_quad_sln_quadrics;

elseif nargout == 2

    [z2d_quad_sln_quadrics, z2d_expression_quadrics] = standard_quadrics_height(x2d, y2d, p, q, theta);
    varargout{1} = z2d_quad_sln_quadrics;
    varargout{2} = z2d_expression_quadrics;

elseif nargout == 4

    [z2d_quad_sln_quadrics, z2d_expression_quadrics] = standard_quadrics_height(x2d, y2d, p, q, theta);
    [z2d_quad_sln_with_abs, z2d_expression_with_abs] = sln_with_abs(x2d, y2d, abs_p, abs_q, theta);
    varargout{1} = z2d_quad_sln_quadrics;
    varargout{2} = z2d_expression_quadrics;
    varargout{3} = z2d_quad_sln_with_abs;
    varargout{4} = z2d_expression_with_abs;

else

    error('Unsupported number of outputs.');

end








% Solutions with absolute values of p and q................................

function [z2d_quad_sln_with_abs, z2d_expression_with_abs] = sln_with_abs(x2d, y2d, abs_p, abs_q, theta)

if abs_p > abs_q
    [z2d_quad_sln_with_abs, z2d_expression_with_abs] = standard_left_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta);
else
    [z2d_quad_sln_with_abs, z2d_expression_with_abs] = standard_right_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta);
end