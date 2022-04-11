clear;
clc;

tic
a = 1;
b = 10;
N = 10;
h = (b - a) / N;
x_k = linspace(a, b, N);

%1
[x_diff, y_diff] = ode45(@func, x_k, [3, -1]);
plot(x_diff, y_diff(:, 2), 'b', 'LineWidth', 6);

%2
y_exact = -x_k + x_k .^ 3 - 1 ./ x_k;
hold on; plot(x_k, y_exact, 'r--', 'LineWidth', 3);

%3
y_k = zeros(1, N);
y_k(1) = f(a);
y_k(2) = f(x_k(2)) / (1 - h * K(x_k(2), x_k(2)));
for n = 3:N
   kern_sum = sum(K(x_k(n), x_k(2:n-1)) .* y_k(2:n-1)); 
   y_k(n) = (f(x_k(n)) + h * kern_sum) / (1 - h * K(x_k(n), x_k(n))); 
end
%hold on; plot(x_k, y_k, 'k.', 'MarkerSize', 15);

%4
p = polyfit(x_k, y_k, 7);
y_interpol = polyval(p, x_k);
hold on; plot(x_k, y_interpol, 'g', 'LineWidth', 2);
hold on; plot(x_k, y_k, 'k.', 'MarkerSize', 15);

%5
y_error = zeros(1, N);
y_error(1) = f(a);
y_error(2) = f(x_k(2)) / (1 - h * K_tilde(x_k(2), x_k(2)));
for n = 3:N
   kern_sum_tilde = sum(K_tilde(x_k(n), x_k(2:n-1)) .* y_error(2:n-1)); 
   y_error(n) = (f(x_k(n)) + h * kern_sum_tilde) / (1 - h * K_tilde(x_k(n), x_k(n))); 
end
hold on; plot(x_k, y_error, 'm', 'LineWidth', 2);

legend('y\_diff', 'y\_exact', 'y\_interpol\_7', 'y\_k', 'y\_error', 'Location', 'northwest', 'FontSize', 20);
set(gca,'fontname','times');
title('Task 1', 'FontSize', 30);
ylabel('y', 'FontSize', 20);
xlabel('x', 'FontSize', 20);
grid on;

%residuals
residual_exact_interpol = norm(y_exact - y_interpol);
residual_exact_error = norm(y_exact - y_error);
residual_diff_interpol = norm(y_diff(:, 2)' - y_interpol);
residual_diff_error = norm(y_diff(:, 2)' - y_error);

y_exact_n = y_exact / norm(y_exact);
y_diff_n = y_diff(:, 2)' / norm(y_diff(:, 2));
y_interpol_n = y_interpol / norm(y_interpol);
y_error_n = y_error / norm(y_error);

residual_exact_interpol_n = norm(y_exact_n - y_interpol_n)
residual_exact_error_n = norm(y_exact_n - y_error_n)
residual_diff_interpol_n = norm(y_diff_n - y_interpol_n)
residual_diff_error_n = norm(y_diff_n - y_error_n)
toc