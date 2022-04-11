m = 2;
a = 0;
b = 5 * pi;
t0 = 0;
t1 = 10;
Nx = 100;
Nt = 100;
xmesh = linspace(a, b, Nx);
tspan = linspace(t0, t1, Nt);

sol = pdepe(m, @pdefun, @icfun, @bcfun, xmesh, tspan);
u = sol(:,:,1);

figure(1)
 surf(xmesh, tspan, u)
 xlabel('x')
 ylabel('t')
 
%f = figure(1);
%f.CurrentAxes.ZDir = 'Reverse'