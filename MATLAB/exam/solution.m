function res = solution(r, t)

%{
X = linspace(0, 50, 1000); 
Y = besselj(0, X);
plot(X, Y); % finding x_0 for fzero
%}

mu(1) = fzero(@(z) besselj(0, z), 2);
mu(2) = fzero(@(z) besselj(0, z), 5);
mu(3) = fzero(@(z) besselj(0, z), 8);
mu(4) = fzero(@(z) besselj(0, z), 11);
mu(5) = fzero(@(z) besselj(0, z), 15);
mu(6) = fzero(@(z) besselj(0, z), 18);
mu(7) = fzero(@(z) besselj(0, z), 21);
mu(8) = fzero(@(z) besselj(0, z), 24);
mu(9) = fzero(@(z) besselj(0, z), 27);
mu(10) = fzero(@(z) besselj(0, z), 30);

%hold on; plot(mu, besselj(0, mu), 'ro'); % checking if fzero worked well

F = zeros(10, size(t, 1), size(r, 2));
for k  = 1 : 10
F(k, :, :) = (2 / 0.2^2) * (t + (1 / (0.2 * mu(k)))^2 * (exp(-(0.2 * mu(k))^ 2 * t) - 1)) ...
.* besselj(0, mu(k) * r) / (mu(k)^3 * besselj(1, mu(k)));
end
res = reshape(sum(F), size(t, 1), size(r, 2));