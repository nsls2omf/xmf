function varargout = standard_concave_hyperbolic_cylinder_xslope(x, abs_p, abs_q, theta)
% standard_concave_hyperbolic_cylinder_xslope(x, abs_p, abs_q, theta) - Computes the x-slope of a concave hyperbolic cylinder
%   at a given x-coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).
%   
%   Inputs:
%       - x - 2D x-coordinates (vector or matrix)
%       - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
%       - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
%       - theta - Grazing incidence angle (in radians)
%   
%   Outputs:
%       - z2d_quad_sln_quadrics - Quadratic solution for the concave hyperbolic cylinder x-slope
%       - z2d_expression_quadrics - Expression for the concave hyperbolic cylinder x-slope

% Give the sign to p and q based on mirror type
if abs(abs_p) > abs(abs_q)
    p = - abs_p;
    q = abs_q;
else
    p = abs_p;
    q = - abs_q;
end


if nargout == 1

    z2d_quad_sln_quadrics = standard_quadric_cylinder_xslope(x, p, q, theta);
    varargout{1} = z2d_quad_sln_quadrics;

elseif nargout == 2

    z2d_expression_quadrics = standard_quadric_cylinder_xslope(x, p, q, theta);
    z2d_expression_with_abs = expression_with_abs(x, abs_p, abs_q, theta);

    varargout{1} = z2d_expression_quadrics;
    varargout{2} = z2d_expression_with_abs;

else

    error('Unsupported number of outputs.');

end

    
    
    
% Expression with absolute values of p and q...............................

function sx_expression_with_abs = expression_with_abs(x, abs_p, abs_q, theta)  

if abs_p > abs_q
    sx_expression_with_abs = standard_left_hyperbolic_cylinder_slope(x, abs_p, abs_q, theta);
else
    sx_expression_with_abs = standard_right_hyperbolic_cylinder_slope(x, abs_p, abs_q, theta);
end