function sx1d = generate_1d_slope(standard_slope_function_handle, x1d, p, q, theta, x_i, beta)

x1d = x1d - x_i;
sx1d = standard_slope_function_handle(x1d, p, q, theta);
sx1d = sx1d + tan(beta);