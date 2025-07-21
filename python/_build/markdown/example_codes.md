# Example codes

Python example for fitting a concave ellipse slope:

```python
import xmf

target_params_dict = {
   'p': p,
   'q': q,
   'theta': theta,
   'x_i': x_i,
   'beta': beta,
}

params_input_dict = {
   'p': p,
   'q': q,
   'theta': theta
}

opt_dict = {
   'p': False,
   'q': False,
   'theta': False
}

sx1d_res, sx1d_fit, opt_params_dict, opt_params_ci_dict, _ = xmf.fit_concave_ellipse_slope(x1d, sx1d_measured, params_input_dict, opt_dict)
xmf.fig_show_1d_fitting_slope(x1d, sx1d_measured, sx1d_fit, sx1d_res, target_params_dict, opt_params_dict, opt_params_ci_dict, 'Concave Ellipse Slope')
```

MATLAB example for fitting a concave ellipse slope:

```matlab
input_params_struct.p = p;
input_params_struct.q = q;
input_params_struct.theta = theta;

opt_struct.p = false;
opt_struct.q = false;
opt_struct.theta = false;

[sx1d_res, sx1d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_ellipse_slope(x1d, sx1d_measured, input_params_struct, opt_struct);
fig_show_1d_fitting_slope(x1d, sx1d_measured, sx1d_fit, sx1d_res, input_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Elliptic Cylinder');
```
