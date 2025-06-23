function [z2d_quad_sln, z2d_expression] = standard_left_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta)

% Quadratic solution.......................................................

A = (abs_p-abs_q).^2 - (abs_p+abs_q).^2.*sin(theta).^2;
B = 2*x2d.*(abs_p+abs_q)*(abs_p-abs_q)*sin(theta)*cos(theta) - 4*abs_p*abs_q*(abs_p-abs_q)*sin(theta);
C = (abs_p-abs_q).^2.*(x2d.^2.*sin(theta).^2 + y2d.^2);

% Discriminant 
Delta = B.^2 - 4*A.*C;

if abs_p > abs_q % p>q and left means concave hyperboloid
    z2d_quad_sln = (-B - sqrt(Delta))./(2.*A);
else % p<q and left means convex hyperboloid
    z2d_quad_sln = (-B + sqrt(Delta))./(2.*A);
end
z2d_quad_sln(Delta<0) = nan;


% Expression...............................................................
z2d_expression = (abs_p-abs_q)*sin(theta).*(-x2d.*(abs_p+abs_q).*cos(theta) + 2*abs_p*abs_q - sqrt(4*abs_p*abs_q*x2d.^2 - 4*abs_p*abs_q*(abs_p+abs_q).*x2d.*cos(theta) + 4*abs_p.^2*abs_q.^2 - ((abs_p-abs_q).^2-(abs_p+abs_q).^2.*sin(theta).^2).*y2d.^2./sin(theta).^2))./((abs_p-abs_q).^2-(abs_p+abs_q).^2.*sin(theta).^2);
z2d_expression(imag(z2d_expression)~=0) = nan;
