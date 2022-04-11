function [pl, ql, pr, qr] = bcfun(xl, ul, xr, ur, t)
pl = ul;
ql = 0;
pr = ur - 1;
qr = 0;
