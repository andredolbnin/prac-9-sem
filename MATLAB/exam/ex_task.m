% Итоговое задание по курсу ИСНВ, Долбнин Андрей, 501 группа

tic

step_x = 0.01; step_t = 0.1;
a = 0; b = 1; X = a : step_x : b;
t0 = 0; t = 5; T = t0 : step_t : t;

% 1 (series)

[Xs, Ts] = meshgrid(a : step_x : b, t0 : step_t : t);
Us = solution(Xs, Ts);
surf(Xs, Ts, Us);
title('Series calculated');
xlabel('r');
ylabel('t');
zlabel('u(r, t)');
colorbar;
colormap summer;

% 2 (PDEPE)

m = 1;

sol = pdepe(m, @pdefun, @icfun, @bcfun, X, T);

figure
surf(X, T, sol(:, :, 1));
title('Solved by PDEPE');
xlabel('r');
ylabel('t');
zlabel('u(r, t)');
colorbar;
colormap summer;

% 4

mod_r = max(max(abs(Us - sol(:, :, 1))))

toc

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% local functions %

function [c, f, s] = pdefun(x, t, u, dudx)
c = 1;
f = 0.2^2 * dudx;
s = t;
end

function u = icfun(x)
u = 0;
end

function [pl, ql, pr, qr] = bcfun(xl, ul, xr, ur, t)
pl = 0;
ql = 1 / 0.2^2;
pr = ur;
qr = 0;
end