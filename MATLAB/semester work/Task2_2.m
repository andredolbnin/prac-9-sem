% Долбнин Андрей, 501 группа
% Зачётное задание номер 2, вариант 3, задание 2

a = 1 / 3;
syms x t phi(x) psi(x) u(x, t)
phi(x) = 0;
psi(x) = piecewise((x >= 1) & (x <= 2), 3, 0);
u(x, t) = (1 / 2) * (phi(x - a * t) + phi(x + a * t)) + (1 / (2 * a)) * int(psi(x), x - a * t, x + a * t);

%fsurf(u, [-5 5 0 5]) % for test

Nx = 100;
Nt = 20;
X = linspace(-24, 25, Nx);
T = linspace(0, 38, Nt);
figure
for i = 1 : Nt
    plot(u(X, T(i)), 'LineWidth', 2);
    title('Task 2, N 2');
    xlabel('x');
    ylabel('u(x, t_k)');
    xlim auto;
    ylim([-1 6]);
    %ylim auto;
    pause(0.5);
end