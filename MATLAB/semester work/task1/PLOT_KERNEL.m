a = 1;
b = 10;
t_kerl = [a : 0.2 : b];
x_kerl = [a : 0.2 : b];
[T_KERL, X_KERL] = meshgrid(t_kerl, x_kerl);
KERL = abs((4 .* X_KERL - 3 .* T_KERL) ./ T_KERL .^ 2);
mesh(T_KERL, X_KERL, KERL);
set(gca,'fontname','times');
xlabel('t', 'Rotation', 20, 'FontSize', 20);
ylabel('x', 'Rotation', -30, 'FontSize', 20);
zlabel('|K(x, t)|', 'FontSize', 20);
%according to the graph, max equals to 37 (t = 1, x = 10) 
%delta = 3.7