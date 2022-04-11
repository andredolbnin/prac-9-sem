function z = K_tilde(x, t)
z = -0.4 + 0.8 * rand() + (4 * x - 3 * t) / t .^ 2;