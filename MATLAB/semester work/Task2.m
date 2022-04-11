% Долбнин Андрей, 501 группа
% Зачётное задание номер 2, вариант 3, задание 1

syms x y Dy D2y
F(x, y, Dy) = Dy^2 + 4 * y^2 + 4 * x^2 * y + x * cos(x);

Fy = diff(F, y);
Fq = diff(F, Dy);

Fq_x = diff(Fq, x);
Fq_y = diff(Fq, y);
Fq_q = diff(Fq, Dy);

EulerRight = Fq_x + Fq_y * Dy + Fq_q * D2y;
Euler = Fy - EulerRight;
Equation = [char(Euler) '=0'];

S = dsolve(Equation, x);

x_1 = -1;
y_1 = 2;

x_2 = 1;
y_2 = 0.5;

Tmp1 = subs(S, x, sym(x_1));
Tmp2 = subs(S, x, sym(x_2));

Eq1 = [char(Tmp1) ' = ' char(sym(y_1))];
Eq2 = [char(Tmp2) ' = ' char(sym(y_2))];

FinalS = solve(str2sym(Eq1), str2sym(Eq2));
C1 = FinalS.C1;
C2 = FinalS.C2;
FinalFinalS = vpa(eval(S), 4);

xgrid = linspace(x_1, x_2);
ygrid = subs(FinalFinalS, x, xgrid);
plot(xgrid, ygrid, 'LineWidth', 2);
title('Task 2, N 1');
xlabel('x');
ylabel('y(x)');

% Задание 2

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