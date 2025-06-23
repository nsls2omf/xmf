function varargout = standard_quadrics_height(x2d, y2d, p, q, theta)

if nargout == 1
    
    z2d_quad_sln = quad_sln(x2d, y2d, p, q, theta);
    varargout{1} = z2d_quad_sln;

elseif nargout == 2

    z2d_quad_sln = quad_sln(x2d, y2d, p, q, theta);
    z2d_expression = expression(x2d, y2d, p, q, theta);
    varargout{1} = z2d_quad_sln;
    varargout{2} = z2d_expression;

else
    error('Unsupported number of outputs.');

end



% Quadratic solution.......................................................

function z2d_quad_sln = quad_sln(x2d, y2d, p, q, theta)

% Parameters
A = (p+q).^2 - (p-q).^2.*sin(theta).^2;
B = 2*x2d.*(p+q)*(p-q)*sin(theta)*cos(theta) - 4*p*q*(p+q)*sin(theta);
C = (p+q).^2.*(x2d.^2.*sin(theta).^2 + y2d.^2);

% Discriminant 
Delta = B.^2 - 4*A.*C;

% Check (p, q) conditions
if (p < 0 && q < 0) % Top (convex) ellipsoid
    z2d_quad_sln = (-B + sqrt(Delta))./(2.*A);
elseif (p > 0 && q > 0) % Bottom (concave) ellipsoid
    z2d_quad_sln = (-B - sqrt(Delta))./(2.*A);
elseif (p < 0 && q > 0) % Left hyperboloid
    if (abs(p) <= abs(q)) % Left convex hyperboloid
        z2d_quad_sln = (-B + sqrt(Delta))./(2.*A);
    else % Left concave hyperboloid
        z2d_quad_sln = (-B - sqrt(Delta))./(2.*A);
    end
elseif (p > 0 && q < 0) % Right hyperboloid
    if (abs(p) >= abs(q)) % Right convex hyperboloid
        z2d_quad_sln = (-B + sqrt(Delta))./(2.*A);
    else % Right concave hyperboloid
        z2d_quad_sln = (-B - sqrt(Delta))./(2.*A);
    end
end

z2d_quad_sln(Delta<0) = nan;





% Expression...............................................................

function z2d_expression = expression(x2d, y2d, p, q, theta)

if (p*q>0) % Ellipsoid
    z2d_expression = (p+q)*sin(theta).*(-x2d.*(p-q).*cos(theta) + 2*p*q - sqrt(-4*p*q*x2d.^2 - 4*p*q*(p-q).*x2d.*cos(theta) + 4*p.^2*q.^2 - ((p+q).^2-(p-q).^2.*sin(theta).^2).*y2d.^2./sin(theta).^2))./((p+q).^2-(p-q).^2.*sin(theta).^2);
elseif (p*q < 0) % Hyperboloid
    z2d_expression = (p+q)*sin(theta).*(-x2d.*(p-q).*cos(theta) + 2*p*q + sqrt(-4*p*q*x2d.^2 - 4*p*q*(p-q).*x2d.*cos(theta) + 4*p.^2*q.^2 - ((p+q).^2-(p-q).^2.*sin(theta).^2).*y2d.^2./sin(theta).^2))./((p+q).^2-(p-q).^2.*sin(theta).^2);
end
z2d_expression(imag(z2d_expression)~=0) = nan;