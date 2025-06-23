function sx = standard_quadric_cylinder_xslope(x, p, q, theta)

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