function varargout = standard_convex_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta)

% Give the sign to p and q based on mirror type
if abs_p > abs_q
    p = abs_p;
    q = - abs_q;
else
    p = - abs_p;
    q = abs_q;
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
    [z2d_quad_sln_with_abs, z2d_expression_with_abs] = standard_right_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta);
else
    [z2d_quad_sln_with_abs, z2d_expression_with_abs] = standard_left_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta);
end