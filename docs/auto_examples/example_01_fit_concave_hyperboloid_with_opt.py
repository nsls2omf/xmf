"""
Example 01: Fit concave hyperboloid 
========================================

This example shows how to fit a concave hyperboloid to simulated data using the XMF library.
"""

import numpy as np
import xmf

## 1. Lateral coordinates

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

opt_dict = {
    'p': False,
    'q': False,
    'theta': False
}

## 6.2. Concave Hyperboloid (CCVH)

z2d = xmf.generate_2d_curved_surface_height(xmf.standard_concave_hyperboloid_height, x2d, y2d, abs_p, abs_q, theta, x_i, y_i, z_i, alpha, beta, gamma) 
z2d_measured = z2d + np.random.randn(z2d.shape[0], z2d.shape[1])*height_measurement_noise_std 
z2d_res, z2d_fit, opt_params_dict, opt_params_ci_dict, _ = xmf.fit_concave_hyperboloid_height(x2d, y2d, z2d_measured, input_params_dict, opt_dict) 
xmf.fig_show_2d_fitting_map(x2d, y2d, z2d_measured, z2d_fit, z2d_res, true_params_dict, opt_params_dict, opt_params_ci_dict, 'Concave Hyperboloid') 