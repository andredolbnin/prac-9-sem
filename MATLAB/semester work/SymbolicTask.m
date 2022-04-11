% Долбнин Андрей, 501 группа

syms x y z n;

% 1 (17)
V1 = (((x^2 - y^2) / (x - y)) - ((x^2 + y^2)/(x + y))) * ((x^2 - y^2)/(2*x*y));
ans1 = simplify(V1);
ans1

% 2 (6)
V2 = tan(2*x) * sin(2*x) - sin(3*x);
ans2 = expand(V2);
ans2

% 3 (8)
V3 = x^3 * y - x * y - x^3 + x;
ans3 = factor(V3);
ans3

% 4 (15)
V4 = x^4 + 9 * x^3 + 31 * x^2 + 59 * x + 60;
ans4 = subs(V4, x, y + z);
ans4
ans4_1 = collect(ans4, y);
ans4_1
ans4_2 = collect(ans4, z);
ans4_2

% 5 (15)
V5 = sqrt(1 + exp(-x));
%ans5 = taylor(V5, x, 0, 'Order', 3);
ans5 = taylor(V5);
ans5

% 6 (15)
V6 = x * (sqrt(x^2 + 1) - x);
ans6 = limit(V6, x, -Inf);
ans6

% 7 (23)
V7 = (x^n) / (factorial(n) * (n+1));
F(x) = symsum(V7, n, 1, Inf);
ans7 = F(23);
ans7




