function z2d = standard_tan_col_diaboloid_height(x2d, y2d, abs_p, abs_q, theta)
% standard_tan_col_diaboloid_height(x2d, y2d, abs_p, abs_q, theta) - Computes the height of a tangential collimating diaboloid
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
%       - z2d - Height of the tangential collimating diaboloid at the given (x, y) coordinates

% Reference: https://doi.org/10.1107/S1600577521004860
% Eq. (32)

A = - cos(theta).^4;
B = 4*(abs_p-abs_q)*cos(theta).^2.*sin(theta) + 4 *cos(theta).^3.*sin(theta)*x2d;
C = 4*abs_q*((abs_p+abs_q)*cos(theta).^2 + 4.*abs_p*sin(theta).^2) + 2*cos(theta)*(abs_q - 3*abs_p + (abs_p-3*abs_q)*cos(2*theta)).*x2d - 6*cos(theta).^2.*sin(theta).^2.*x2d.^2;
D = -16*abs_p*abs_q*(abs_p+abs_q)*sin(theta) + 4*(abs_p+abs_q)*(2*abs_p-abs_q)*sin(2*theta)*x2d + 2*(3*abs_p+abs_q+(3*abs_q+abs_p)*cos(2*theta))*sin(theta)*x2d.^2 + 4*cos(theta)*sin(theta).^3.*x2d.^3;
E = 4*(abs_p+abs_q).^2.*y2d.^2 + 4*abs_q*(abs_p+abs_q)*sin(theta).^2.*x2d.^2 - 4*(abs_p+abs_q)*cos(theta)*sin(theta).^2.*x2d.^3 - sin(theta).^4.*x2d.^4;

b = B./A;
c = C./A;
d = D./A;
e = E./A;

% Solve the equation
k = (8.*c-3.*b.^2)./8;
m = (b.^3-4.*b.*c+8.*d)./8;

Delta_0 = c.^2 - 3.*b.*d + 12.*e;
Delta_1 = 2*c.^3 - 9.*b.*c.*d + 27.*b.^2.*e + 27.*d.^2 - 72.*c.*e;

mask = Delta_1.^2 - 4.*Delta_0.^3 >= 0;

% Note: the expression of Q in the reference paper was wrong.
Q = 0.5.^(1/3).*(Delta_1 + sqrt(Delta_1.^2 - 4.*Delta_0.^3)).^(1/3); % ?! complex number?! LH20241110
S1 = real(0.5*sqrt((1/3).*(Q + Delta_0./Q) - 2/3.*k));

% Another way to avoid the complex number Q,
% when Delta_1.^2 - 4.*Delta_0.^3<0
% Source: https://en.wikipedia.org/wiki/Quartic_function#
phi = acos(Delta_1./(2*sqrt(Delta_0.^3)));
S2 = 0.5*sqrt(- 2/3.*k + 2/3.*sqrt(Delta_0).*cos(phi/3));

S = mask.*S1 + ~mask.*S2;

z2d = -b/4 - S + 0.5*sqrt(-4.*S.^2 - 2.*k + m./S);