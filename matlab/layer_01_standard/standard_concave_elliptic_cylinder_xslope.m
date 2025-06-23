function varargout = standard_concave_elliptic_cylinder_xslope(x, abs_p, abs_q, theta)

% Give the sign to p and q based on mirror type
p = abs_p;
q = abs_q;  

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

sx_expression_with_abs = (abs_p+abs_q)*sin(theta)./((abs_p+abs_q).^2-(abs_p-abs_q).^2.*sin(theta).^2)...
    .*(-(abs_p-abs_q).*cos(theta) + (2*abs_p*abs_q*x + abs_p*abs_q*(abs_p-abs_q).*cos(theta))./sqrt(-abs_p*abs_q*x.^2 - abs_p*abs_q*(abs_p-abs_q).*x.*cos(theta) + abs_p.^2*abs_q.^2));

sx_expression_with_abs(imag(sx_expression_with_abs)~=0) = nan;