function [c, f, s] = pdefun(x, t, u, dudx)
c = x .^ 2 + t .^ 2;
f = dudx;
s = abs(besselh(0, x));
