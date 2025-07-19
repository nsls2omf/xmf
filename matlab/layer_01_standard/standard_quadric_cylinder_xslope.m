function sx = standard_quadric_cylinder_xslope(x, p, q, theta)
% standard_quadric_cylinder_xslope(x, p, q, theta) - Computes the x-slope of a quadric cylinder
%   at a given x-coordinate, based on the parameters p and q and the grazing incidence angle (theta).
%   
%   Inputs:
%       - x - 2D x-coordinates (vector or matrix)
%       - p - Distance between the source and the chief ray intersection on mirror
%       - q - Distance between the focus and the chief ray intersection on mirror
%       - theta - Grazing incidence angle (in radians)
%   
%   Outputs:
%       - sx - x-slope of the quadric cylinder at the given x-coordinates

if (p*q>0) % Elliptic cylinder
    
    sx = (p+q)*sin(theta)./((p+q).^2-(p-q).^2.*sin(theta).^2)...
        .*(-(p-q).*cos(theta) + (2*p*q*x + p*q*(p-q).*cos(theta))./sqrt(-p*q*x.^2 - p*q*(p-q).*x.*cos(theta) + p.^2*q.^2));

elseif (p*q<0) % Hyperbolic cylinder
    
    sx = (p+q)*sin(theta)./((p+q).^2-(p-q).^2.*sin(theta).^2)...
        .*(-(p-q).*cos(theta) - (2*p*q*x + p*q*(p-q).*cos(theta))./sqrt(-p*q*x.^2 - p*q*(p-q).*x.*cos(theta) + p.^2*q.^2));
else
    
    error('Parameters with p=0 or q=0 is not allowed.');

end


sx(imag(sx)~=0) = nan;