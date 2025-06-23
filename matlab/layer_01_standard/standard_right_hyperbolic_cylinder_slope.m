function sx = standard_right_hyperbolic_cylinder_slope(x, abs_p, abs_q, theta)

sx = (abs_p-abs_q)*sin(theta)./((abs_p-abs_q).^2-(abs_p+abs_q).^2.*sin(theta).^2)...
    .*(-(abs_p+abs_q).*cos(theta) + (2*abs_p*abs_q*x + abs_p*abs_q*(abs_p+abs_q).*cos(theta))./sqrt(abs_p*abs_q*x.^2 + abs_p*abs_q*(abs_p+abs_q).*x.*cos(theta) + abs_p.^2*abs_q.^2));

sx(imag(sx)~=0) = nan;