# XMF

Welcome to the X-ray Mirror surface shape Fitting (XMF)!

<p align="center">
    <img src="python/docs/_static/logo.png" alt="xmf_logo" width="400"/>
</p>

In the [XMF documentation (https://nsls2omf.github.io/xmf)](https://nsls2omf.github.io/xmf/), we introduce the modules and functionalities of XMF in Python and MATLAB.

# Framework

XMF is a framework for the X-ray mirror surface shape fitting, particularly in the context of convex and concave shapes.

<p align="center">
   <img src="python/docs/_static/mirror_surfaces.png" alt="mirror surfaces" style="width:100%; max-width:1000px;"/>
</p>

It provides data analysis and visualization tools for fitting measurement data to various geometric shapes, including elliptic cylinders, hyperbolic cylinders, ellipsoids, and hyperboloids.

<p align="center">
   <img src="python/docs/_static/framework.png" alt="framework" style="width:66vw; max-width:1000px;">
</p>

The framework is composed of four main layers:

- **Layer 1: Standard shape from expressions**. It contains the standard mathematical expressions of various off-axis mirror shapes.
- **Layer 2: Surface generation**. It generates surface shapes in height or slope, by taking into account the rotation and translation of the shapes.
- **Layer 3: Optimization**. It optimizes the user-selected fitting parameters.
- **Layer 4: Function wrapper**. It offers convenient functions to fit measurement data for specific shapes.

# Example codes

Python example for fitting a concave ellipse slope:

```python

import numpy as np
import xmf

x_range = 200e-3 
y_range = 20e-3 
x_num = 201 
y_num = 21 

x1d = np.linspace(-x_range/2, x_range/2, x_num) 
y1d = np.linspace(-y_range/2, y_range/2, y_num) 
x2d, y2d = np.meshgrid(x1d, y1d)

abs_p = 30 
abs_q = 0.3
theta = 30e-3 

x_i = -1e-3 
y_i = -2e-4 
z_i = 3e-7 
alpha = 2e-6 
beta = 1e-5 
gamma = 0.5e-3 

true_params_dict = {
    'p': abs_p,
    'q': abs_q,
    'theta': theta,
    'x_i': x_i,
    'y_i': y_i,
    'z_i': z_i,
    'alpha': alpha,
    'beta': beta,
    'gamma': gamma
}

height_measurement_noise_std = 0.5e-9
slope_measurement_noise_std = 100e-9

input_params_dict = {
    'p': abs_p,
    'q': abs_q,
    'theta': theta
}

tol_dict = {
    'p': 0,
    'q': 0,
    'theta': 0
}

z2d = xmf.generate_2d_curved_surface_height(xmf.standard_concave_ellipsoid_height, x2d, y2d, abs_p, abs_q, theta, x_i, y_i, z_i, alpha, beta, gamma) 
z2d_measured = z2d + np.random.randn(z2d.shape[0], z2d.shape[1])*height_measurement_noise_std 
z2d_res, z2d_fit, opt_params_dict, opt_params_ci_dict, _ = xmf.fit_concave_ellipsoid_height(x2d, y2d, z2d_measured, input_params_dict, tol_dict) 
xmf.fig_show_2d_fitting_map(x2d, y2d, z2d_measured, z2d_fit, z2d_res, true_params_dict, opt_params_dict, opt_params_ci_dict,'Concave Ellipsoid') 
```

MATLAB example for fitting a concave ellipse slope:

```matlab
x_range = 200e-3;
y_range = 20e-3;
x_num = 201;
y_num = 21;
x1d = linspace(-x_range/2, x_range/2, x_num);
y1d = linspace(-y_range/2, y_range/2, y_num);
[x2d, y2d] = meshgrid(x1d, y1d);

abs_p = 30;
abs_q = 0.3;
theta = 30e-3;

x_i = -1e-3;
y_i = -2e-4;
z_i = 3e-7;
alpha = 2e-6;
beta = 1e-5;
gamma = 0.5e-3;

true_params_struct.p = abs_p;
true_params_struct.q = abs_q;
true_params_struct.theta = theta;
true_params_struct.x_i = x_i;
true_params_struct.y_i = y_i;
true_params_struct.z_i = z_i;
true_params_struct.alpha = alpha;
true_params_struct.beta = beta;
true_params_struct.gamma = gamma;

height_measurement_noise_std = 0.5e-9;
slope_measurement_noise_std = 100e-9;

input_params_struct.p = abs_p;
input_params_struct.q = abs_q;
input_params_struct.theta = theta;

opt_struct.p = false;
opt_struct.q = false;
opt_struct.theta = false;

z2d = generate_2d_cylinder_height(@standard_concave_elliptic_cylinder_height, x2d, y2d, abs_p, abs_q, theta, x_i, z_i, alpha, beta, gamma);
z2d_measured = z2d + randn(size(z2d))*height_measurement_noise_std;
[z2d_res, z2d_fit, opt_params_struct, opt_params_ci_struct] = fit_concave_elliptic_cylinder_height(x2d, y2d, z2d_measured, input_params_struct, opt_struct);
fig_show_2d_fitting_map(x1d, y1d, z2d_measured, z2d_fit, z2d_res, true_params_struct, opt_params_struct, opt_params_ci_struct, 'Concave Elliptic Cylinder');
```
