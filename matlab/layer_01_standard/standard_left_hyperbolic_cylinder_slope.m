function sx = standard_left_hyperbolic_cylinder_slope(x, abs_p, abs_q, theta)
% standard_left_hyperbolic_cylinder_slope(x, abs_p, abs_q, theta) - Computes the x-slope of a left hyperbolic cylinder
%   at a given x-coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).
%   
%   Inputs:
%       - x - 2D x-coordinates (vector or matrix)
%       - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
%       - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
%       - theta - Grazing incidence angle (in radians)
%
%   Outputs:
%       - sx - x-slope of the left hyperbolic cylinder at the given x-coordinates

sx = (abs_p-abs_q)*sin(theta)./((abs_p-abs_q).^2-(abs_p+abs_q).^2.*sin(theta).^2)...
    .*(-(abs_p+abs_q).*cos(theta) - (2*abs_p*abs_q*x - abs_p*abs_q*(abs_p+abs_q).*cos(theta))./sqrt(abs_p*abs_q*x.^2 - abs_p*abs_q*(abs_p+abs_q).*x.*cos(theta) + abs_p.^2*abs_q.^2));

sx(imag(sx)~=0) = nan;