# Copyright (c) 2025 Lei Huang
#
# Lei Huang
# huanglei0114@gmail.com
#
# All rights reserved
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import re
from scipy.interpolate import interp1d
from mpl_toolkits import axes_grid1


def add_colorbar(im: plt.cm.ScalarMappable,
                 title: str = None,
                 aspect: int = 10,
                 pad_fraction: float = 1.5,
                 **kwargs):
    """
    Add a vertical color bar to an image plot

    Parameters
    ----------
        im:  `matplotlib.cm.ScalarMappable`
            The image to be described by the colorbar
        title: `str`
            The title of the colorbar
        aspect: `int`
            The aspect ratio between width and height
        pad_fraction: `float`
            The padding fraction
    Returns
    -------
        cbar: `matplotlib.pyplot.colorbar`
            The added colorbar
    """

    divider = axes_grid1.make_axes_locatable(im.axes)
    width = axes_grid1.axes_size.AxesY(im.axes, aspect=1./aspect)
    pad = axes_grid1.axes_size.Fraction(pad_fraction, width)
    current_ax = plt.gca()
    cax = divider.append_axes("right", size=width, pad=pad)
    plt.sca(current_ax)
    cbar = im.axes.figure.colorbar(im, cax=cax, **kwargs)

    if title is not None:
        cbar.ax.set_ylabel(title, rotation=0, ha='left', va='center')

    return cbar

def reg_exp_rep(s):
    # Replace scientific notation with LaTeX format
    s = re.sub(r'e\+?0*(\d+)', r'\\times10^{\1}', s)
    s = re.sub(r'e-0*(\d+)', r'\\times10^{-\1}', s)
    return s

def fig_show_2d_maps(x2d, y2d, z2d_quad_sln, z2d_expression, str_title):

    x2d_mm = x2d * 1e3
    y2d_mm = y2d * 1e3
    z2d_quad_sln_um = z2d_quad_sln * 1e6
    z2d_expression_um = z2d_expression * 1e6
    dz2d_nm = (z2d_quad_sln - z2d_expression) * 1e9

    fig, axs = plt.subplots(3, 1, sharex='col')
    fig.set_size_inches(10, 4.5)
    im = axs[0].pcolormesh(x2d_mm, y2d_mm, z2d_quad_sln_um, shading='auto')
    add_colorbar(im, '[µm]')
    im = axs[1].pcolormesh(x2d_mm, y2d_mm, z2d_expression_um, shading='auto')
    add_colorbar(im, '[µm]')
    im = axs[2].pcolormesh(x2d_mm, y2d_mm, dz2d_nm, shading='auto', cmap='seismic')
    add_colorbar(im, '[nm]')
    axs[0].set_ylabel('y [mm]')
    axs[0].set_title(str_title)
    axs[1].set_ylabel('y [mm]')
    axs[2].set_ylabel('y [mm]')
    axs[2].set_xlabel('x [mm]')
    axs[2].set_title(f'Difference: {np.nanstd(dz2d_nm):.2f} nm RMS')
    plt.tight_layout()
    plt.show()
    
def fig_show_1d_height(x1d, z1d_quad_sln, z1d_expression, str_title):
    
    x1d_mm = x1d * 1e3
    z1d_quad_sln_um = z1d_quad_sln * 1e6
    z1d_expression_um = z1d_expression * 1e6
    dz1d_nm = (z1d_quad_sln - z1d_expression) * 1e9

    fig, axs = plt.subplots(2, 1, sharex=True)
    fig.set_size_inches(10, 4.5)

    axs[0].plot(x1d_mm, z1d_quad_sln_um, linewidth=3, label='Quadratic equation solution')
    axs[0].plot(x1d_mm, z1d_expression_um, '--', linewidth=3, label='Expression')
    axs[0].set_ylabel('z [µm]')
    axs[0].set_title(str_title)
    axs[0].legend()
    axs[0].tick_params(labelbottom=False)

    axs[1].plot(x1d_mm, dz1d_nm, 'o', markersize=8, markerfacecolor='r')
    axs[1].set_xlabel('x [mm]')
    axs[1].set_ylabel('z [nm]')
    axs[1].set_title(f'Difference: {np.nanstd(dz1d_nm):.3g} nm RMS')

    plt.tight_layout()
    plt.show()
    
def fig_show_1d_slope(x1d, sx1d, str_title):
    
    x1d_mm = x1d * 1e3
    sx1d_mrad = sx1d * 1e3

    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(10, 2.5)

    ax.plot(x1d_mm, sx1d_mrad, linewidth=3, label='x-slope')
    ax.set_xlabel('x [mm]')
    ax.set_ylabel('x-slope [mrad]')
    ax.set_title(str_title)

    plt.tight_layout()
    plt.show()

def fig_compare_1d_height(x1d, z1d_generation, z1d_standard, str_title):
    
    x1d_mm = x1d * 1e3
    z1d_standard_um = z1d_standard * 1e6
    z1d_generation_um = z1d_generation * 1e6
    dz1d_nm = (z1d_generation - z1d_standard) * 1e9

    fig, axs = plt.subplots(2, 1, sharex=True)
    fig.set_size_inches(10, 4)

    axs[0].plot(x1d_mm, z1d_generation_um, linewidth=3, label= 'generation')
    axs[0].plot(x1d_mm, z1d_standard_um , '--', linewidth=3, label='standard')
    axs[0].set_ylabel('z [µm]')
    axs[0].set_title(str_title)
    axs[0].legend()
    axs[0].tick_params(labelbottom=False)

    axs[1].plot(x1d_mm, dz1d_nm, 'o', markersize=8, markerfacecolor='r')
    axs[1].set_xlabel('x [mm]')
    axs[1].set_ylabel('z [nm]')
    axs[1].set_title(f'Difference: {np.nanstd(dz1d_nm):.3g} nm RMS')

    plt.tight_layout()
    plt.show()
    
def fig_compare_1d_slope(x1d, sx1d_generation, sx1d_standard, str_title):
    
    x1d_mm = x1d * 1e3
    sx1d_generation_mrad = sx1d_generation * 1e3
    sx1d_standard_mrad = sx1d_standard * 1e3
    dsx1d_nrad = (sx1d_generation - sx1d_standard) * 1e9

    fig, axs = plt.subplots(2, 1)
    fig.set_size_inches(10, 4)

    axs[0].plot(x1d_mm, sx1d_generation_mrad, linewidth=3, label='x-slope')
    axs[0].plot(x1d_mm, sx1d_standard_mrad, '--', linewidth=3, label='generation')
    axs[0].set_ylabel('x-slope [mrad]')
    axs[0].set_title(str_title)
    axs[0].legend()
    axs[0].tick_params(labelbottom=False)

    axs[1].plot(x1d_mm, dsx1d_nrad, 'o', markersize=8, markerfacecolor='r')
    axs[1].set_xlabel('x [mm]')
    axs[1].set_ylabel('difference [nrad]')
    axs[1].set_title(f'Difference: {np.nanstd(dsx1d_nrad):.3g} nrad RMS')


    plt.tight_layout()
    plt.show()
    
def fig_show_2d_fitting_maps(x2d, y2d, z2d_measured, z2d_fit, z2d_res, target_params_dict, opt_params_dict, is_optimized_dict, str_title):
    x2d_mm = x2d * 1e3
    y2d_mm = y2d * 1e3
    z2d_um = z2d_measured * 1e6
    z2d_fit_um = z2d_fit * 1e6
    z2d_res_nm = z2d_res * 1e9

    font_size = 14
    large_font_size = 24
    marker_size = 8

    def parameter_to_string_2d(params_dict, is_optimized_dict=None):
        def get_height_map_string(is_optimized_dict):
            if is_optimized_dict is None:
                is_optimized_dict = {'p': False, 'q': False, 'theta': False, 'x_i': False, 'y_i': False, 'z_i': False, 'alpha': False, 'beta': False, 'gamma': False}
                
            str_p = r'\hat{p}' if is_optimized_dict.get('p', True) else 'p'
            str_q = r'\hat{q}' if is_optimized_dict.get('q', True) else 'q'
            str_theta = r'\hat{\theta}' if is_optimized_dict.get('theta', True) else r'\theta'
            str_x_i = r'\hat{x_i}' if is_optimized_dict.get('x_i', True) else 'x_i'
            str_y_i = r'\hat{y_i}' if is_optimized_dict.get('y_i', True) else 'y_i'
            str_z_i = r'\hat{z_i}' if is_optimized_dict.get('z_i', True) else 'z_i'
            str_alpha = r'\hat{\alpha}' if is_optimized_dict.get('alpha', True) else r'\alpha'
            str_beta = r'\hat{\beta}' if is_optimized_dict.get('beta', True) else r'\beta'
            str_gamma = r'\hat{\gamma}' if is_optimized_dict.get('gamma', True) else r'\gamma'

            return str_p, str_q, str_theta, str_x_i, str_y_i, str_z_i, str_alpha, str_beta, str_gamma
        
        # Helper for 2D parameter string formatting
        str_p, str_q, str_theta, str_x_i, str_y_i, str_z_i, str_alpha, str_beta, str_gamma = get_height_map_string(is_optimized_dict)
        if 'y_i' in params_dict:
            str_1 = r'($%s$, $%s$, $%s$) = ($%.4g$ m, $%.4g$ m, $%.4g$ mrad)' % (str_p, str_q, str_theta, params_dict['p'], params_dict['q'], params_dict['theta']*1e3)
            str_2 = r'($%s$, $%s$, $%s$) = ($%.4g$ mm, $%.4g$ mm, $%.4g$ mm)' % (str_x_i, str_y_i, str_z_i, params_dict['x_i']*1e3, params_dict['y_i']*1e3, params_dict['z_i']*1e3)
            str_3 = r'($%s$, $%s$, $%s$) = ($%.4g$ $\mu$rad, $%.4g$ $\mu$rad, $%.4g$ $\mu$rad)' % (str_alpha, str_beta, str_gamma, params_dict['alpha']*1e6, params_dict['beta']*1e6, params_dict['gamma']*1e6)
        else:
            str_1 = r'($p$, $q$, $\theta$) = ($%.4g$ m, $%.4g$ m, $%.4g$ mrad)' % (params_dict['p'], params_dict['q'], params_dict['theta']*1e3)
            str_2 = r'($x_i$, $z_i$) = ($%.4g$ mm, $%.4g$ mm)' % (params_dict['x_i']*1e3, params_dict['z_i']*1e3)
            str_3 = r'($\alpha$, $\beta$, $\gamma$) = ($%.4g$ $\mu$rad, $%.4g$ $\mu$rad, $%.4g$ $\mu$rad)' % (params_dict['alpha']*1e6, params_dict['beta']*1e6, params_dict['gamma']*1e6)
        return [reg_exp_rep(str_1), reg_exp_rep(str_2), reg_exp_rep(str_3)]


    fig = plt.figure(figsize=(18, 6))
    gs = gridspec.GridSpec(3, 3, height_ratios=[1, 1, 1], width_ratios=[1, 1, 1], wspace=0.3, hspace=0.3)

    # Data
    ax1 = plt.subplot(gs[0, 0:2])
    im1 = ax1.pcolormesh(x2d_mm, y2d_mm, z2d_um)
    ax1.set_xticklabels([])
    ax1.set_ylabel('y [mm]', fontsize=font_size)
    ax1.set_title(str_title, fontsize=font_size)
    add_colorbar(im1, '[µm]')
    ax1.tick_params(axis='both', labelsize=font_size)
    
    # Target parameters
    ax2 = plt.subplot(gs[0, 2])
    ax2.axis('off')
    ax2.text(0.5, 1, 'Target parameters:', fontsize=large_font_size, ha='center', va='top', fontweight='bold', color='k', transform=ax2.transAxes)
    for i, s in enumerate(parameter_to_string_2d(target_params_dict)):
        ax2.text(0, 0.7-0.2*i, s, fontsize=font_size, ha='left', va='top', transform=ax2.transAxes)

    # Fit
    ax3 = plt.subplot(gs[1, 0:2])
    im2 = ax3.pcolormesh(x2d_mm, y2d_mm, z2d_fit_um)
    ax3.plot(opt_params_dict['x_i']*1e3, opt_params_dict.get('y_i', 0)*1e3, 'ro', markersize=marker_size, markerfacecolor='r')
    # Beam direction projection
    if 'gamma' in opt_params_dict:
        proj_x = np.cos(opt_params_dict['gamma']) * (x2d[-1, -1] - x2d[0, 0]) * 0.08
        proj_y = np.sin(opt_params_dict['gamma']) * (x2d[-1, -1] - x2d[0, 0]) * 0.08
        ax3.quiver(
            opt_params_dict['x_i']*1e3 - proj_x*1e3,
            opt_params_dict.get('y_i', 0)*1e3 - proj_y*1e3,
            2*proj_x*1e3, 2*proj_y*1e3,
            angles='xy', scale_units='xy', scale=1,
            color='r', linewidth=0.5
        )
    ax3.set_xticklabels([])
    ax3.set_ylabel('y [mm]', fontsize=font_size)
    ax3.set_title('Fitting', fontsize=font_size)
    add_colorbar(im2, '[µm]')
    ax3.tick_params(axis='both', labelsize=font_size)


    # Fitted parameters
    ax4 = plt.subplot(gs[1, 2])
    ax4.axis('off')
    ax4.text(0.5, 1, 'Fitted parameters:', fontsize=large_font_size, ha='center', va='top', fontweight='bold', color='k', transform=ax4.transAxes)
    for i, s in enumerate(parameter_to_string_2d(opt_params_dict, is_optimized_dict)):
        ax4.text(0, 0.7-0.2*i, s, fontsize=font_size, ha='left', va='top', transform=ax4.transAxes)

    # Residual
    ax5 = plt.subplot(gs[2, 0:2])
    im3 = ax5.pcolormesh(x2d_mm, y2d_mm, z2d_res_nm, cmap='seismic')
    ax5.set_xlabel('x [mm]', fontsize=font_size)
    ax5.set_ylabel('y [mm]', fontsize=font_size)
    ax5.set_title('Residual', fontsize=font_size)
    add_colorbar(im3, '[nm]')
    ax5.tick_params(axis='both', labelsize=font_size)

    # Residual RMS
    ax6 = plt.subplot(gs[2, 2])
    ax6.axis('off')
    str_rms = f'Residual:\n{np.nanstd(z2d_res_nm):.2f} nm RMS'
    ax6.text(0.5, 0.5, str_rms, fontsize=large_font_size, fontweight='bold', ha='center', va='center', color='k', transform=ax6.transAxes)

    plt.show()


def fig_show_1d_fitting_height(x1d, z1d_measured, z1d_fit, z1d_res, target_params_dict, opt_params_dict, is_optimized_dict, str_title):

    x1d_mm = x1d * 1e3
    z1d_measured_um = z1d_measured * 1e6
    z1d_fit_um = z1d_fit * 1e6
    z1d_res_nm = z1d_res * 1e9

    font_size = 14
    large_font_size = 24
    marker_size = 8
    line_width = 3
    
    def parameter_to_string_1d(params_dict, is_optimized_dict=None):

        def get_height_string(is_optimized_dict):
            if is_optimized_dict is None:
                is_optimized_dict = {'p': False, 'q': False, 'theta': False, 'x_i': False, 'y_i': False, 'z_i': False, 'alpha': False, 'beta': False, 'gamma': False}

            str_p = r'\hat{p}' if is_optimized_dict.get('p', True) else 'p'
            str_q = r'\hat{q}' if is_optimized_dict.get('q', True) else 'q'
            str_theta = r'\hat{\theta}' if is_optimized_dict.get('theta', True) else r'\theta'
            str_x_i = r'\hat{x_i}' if is_optimized_dict.get('x_i', True) else 'x_i'
            str_z_i = r'\hat{z_i}' if is_optimized_dict.get('z_i', True) else 'z_i'
            str_beta = r'\hat{\beta}' if is_optimized_dict.get('beta', True) else r'\beta'
            return str_p, str_q, str_theta, str_x_i, str_z_i, str_beta

        str_p, str_q, str_theta, str_x_i, str_z_i, str_beta = get_height_string(is_optimized_dict)

        # Helper for 1D parameter string formatting
        str_1 = r'($%s$, $%s$, $%s$) = ($%.4g$ m, $%.4g$ m, $%.4g$ mrad)' % (str_p, str_q, str_theta, params_dict['p'], params_dict['q'], params_dict['theta']*1e3)
        str_2 = r'($%s$, $%s$) = ($%.4g$ mm, $%.4g$ mm)' % (str_x_i, str_z_i, params_dict['x_i']*1e3, params_dict['z_i']*1e3)
        str_3 = r'$%s$ = $%.4g$ $\mu$rad' % (str_beta, params_dict['beta']*1e6)
        return [reg_exp_rep(str_1), reg_exp_rep(str_2), reg_exp_rep(str_3)]

    fig = plt.figure(figsize=(18, 6))
    gs = gridspec.GridSpec(3, 3, height_ratios=[1, 1, 1], width_ratios=[1, 1, 1], wspace=0.3, hspace=0.3)

    # Data
    ax1 = plt.subplot(gs[0:2, 0:2])
    ax1.plot(x1d_mm, z1d_measured_um, 'o', markersize=8, label='Measured')
    ax1.plot(x1d_mm, z1d_fit_um, '-', linewidth=line_width, label='Fit')
    # Interpolate for marker at fitted x_i
    interp_func = interp1d(x1d_mm, z1d_fit_um, bounds_error=False, fill_value="extrapolate")
    ax1.plot(opt_params_dict['x_i']*1e3, interp_func(opt_params_dict['x_i']*1e3), 'ro', markersize=marker_size, markerfacecolor='r')
    ax1.set_xticklabels([])
    ax1.set_ylabel('z [µm]', fontsize=font_size)
    ax1.set_title(str_title, fontsize=font_size)
    ax1.tick_params(axis='both', labelsize=font_size)

    # Target parameters
    ax2 = plt.subplot(gs[0, 2])
    ax2.axis('off')
    ax2.text(0.5, 1, 'Target parameters:', fontsize=large_font_size, ha='center', va='top', fontweight='bold', color='k', transform=ax2.transAxes)
    for i, s in enumerate(parameter_to_string_1d(target_params_dict)):
        ax2.text(0, 0.7-0.2*i, s, fontsize=font_size, ha='left', va='top', transform=ax2.transAxes)

    # Fitted parameters
    ax3 = plt.subplot(gs[1, 2])
    ax3.axis('off')
    ax3.text(0.5, 1, 'Fitted parameters:', fontsize=large_font_size, ha='center', va='top', fontweight='bold', color='tab:orange', transform=ax3.transAxes)
    for i, s in enumerate(parameter_to_string_1d(opt_params_dict, is_optimized_dict)):
        ax3.text(0, 0.7-0.2*i, s, fontsize=font_size, ha='left', va='top', transform=ax3.transAxes)

    # Residual
    ax4 = plt.subplot(gs[2, 0:2])
    ax4.axhline(0, color='k')
    ax4.plot(x1d_mm, z1d_res_nm, 'o-', markersize=marker_size, markerfacecolor='tab:blue', markeredgecolor='tab:blue', color='tab:blue')
    ax4.set_xlabel('x [mm]', fontsize=font_size)
    ax4.set_ylabel('Residual [nm]', fontsize=font_size)
    ax4.tick_params(axis='both', labelsize=font_size)

    # Residual RMS
    ax5 = plt.subplot(gs[2, 2])
    ax5.axis('off')
    str_rms = f'Residual:\n{np.nanstd(z1d_res_nm):.2f} nm RMS'
    ax5.text(0.5, 0.5, str_rms, fontsize=large_font_size, fontweight='bold', ha='center', va='center', color='tab:blue', transform=ax5.transAxes)

    plt.show()

def fig_show_1d_fitting_slope(x1d, sx1d_measured, sx1d_fit, sx1d_res, target_params_dict, opt_params_dict, is_optimized_dict, str_title):

    x1d_mm = x1d * 1e3
    sx1d_measured_mrad = sx1d_measured * 1e3
    sx1d_fit_mrad = sx1d_fit * 1e3
    sx1d_res_urad = sx1d_res * 1e6

    font_size = 14
    large_font_size = 24
    marker_size = 8
    line_width = 3
    
    def parameter_to_string_1d(params_dict, is_optimized_dict=None):

        def get_slope_string(is_optimized_dict):
            if is_optimized_dict is None:
                is_optimized_dict = {'p': False, 'q': False, 'theta': False, 'x_i': False, 'y_i': False, 'z_i': False, 'alpha': False, 'beta': False, 'gamma': False}

            str_p = r'\hat{p}' if is_optimized_dict.get('p', True) else 'p'
            str_q = r'\hat{q}' if is_optimized_dict.get('q', True) else 'q'
            str_theta = r'\hat{\theta}' if is_optimized_dict.get('theta', True) else r'\theta'
            str_x_i = r'\hat{x_i}' if is_optimized_dict.get('x_i', True) else 'x_i'
            str_z_i = r'\hat{z_i}' if is_optimized_dict.get('z_i', True) else 'z_i'
            str_beta = r'\hat{\beta}' if is_optimized_dict.get('beta', True) else r'\beta'
            return str_p, str_q, str_theta, str_x_i, str_z_i, str_beta

        str_p, str_q, str_theta, str_x_i, str_z_i, str_beta = get_slope_string(is_optimized_dict)

        # Helper for 1D parameter string formatting
        str_1 = r'($%s$, $%s$, $%s$) = ($%.4g$ m, $%.4g$ m, $%.4g$ mrad)' % (str_p, str_q, str_theta, params_dict['p'], params_dict['q'], params_dict['theta']*1e3)
        str_2 = r'$%s$ = $%.4g$ mm' % (str_x_i, params_dict['x_i']*1e3)
        str_3 = r'$%s$ = $%.4g$ $\mu$rad' % (str_beta, params_dict['beta']*1e6)
        return [reg_exp_rep(str_1), reg_exp_rep(str_2), reg_exp_rep(str_3)]

    fig = plt.figure(figsize=(18, 6))
    gs = gridspec.GridSpec(3, 3, height_ratios=[1, 1, 1], width_ratios=[1, 1, 1], wspace=0.3, hspace=0.3)

    # Data
    ax1 = plt.subplot(gs[0:2, 0:2])
    ax1.plot(x1d_mm, sx1d_measured_mrad, 'o', markersize=8, label='Measured')
    ax1.plot(x1d_mm, sx1d_fit_mrad, '-', linewidth=line_width, label='Fit')
    # Interpolate for marker at fitted x_i
    interp_func = interp1d(x1d_mm, sx1d_fit_mrad, bounds_error=False, fill_value="extrapolate")
    ax1.plot(opt_params_dict['x_i']*1e3, interp_func(opt_params_dict['x_i']*1e3), 'ro', markersize=marker_size, markerfacecolor='r')
    ax1.set_xticklabels([])
    ax1.set_ylabel('x-slope [mrad]', fontsize=font_size)
    ax1.set_title(str_title, fontsize=font_size)
    ax1.tick_params(axis='both', labelsize=font_size)

    # Target parameters
    ax2 = plt.subplot(gs[0, 2])
    ax2.axis('off')
    ax2.text(0.5, 1, 'Target parameters:', fontsize=large_font_size, ha='center', va='top', fontweight='bold', color='k', transform=ax2.transAxes)
    for i, s in enumerate(parameter_to_string_1d(target_params_dict)):
        ax2.text(0, 0.7-0.2*i, s, fontsize=font_size, ha='left', va='top', transform=ax2.transAxes)

    # Fitted parameters
    ax3 = plt.subplot(gs[1, 2])
    ax3.axis('off')
    ax3.text(0.5, 1, 'Fitted parameters:', fontsize=large_font_size, ha='center', va='top', fontweight='bold', color='tab:orange', transform=ax3.transAxes)
    for i, s in enumerate(parameter_to_string_1d(opt_params_dict, is_optimized_dict)):
        ax3.text(0, 0.7-0.2*i, s, fontsize=font_size, ha='left', va='top', transform=ax3.transAxes)

    # Residual
    ax4 = plt.subplot(gs[2, 0:2])
    ax4.axhline(0, color='k')
    ax4.plot(x1d_mm, sx1d_res_urad, 'o-', markersize=marker_size, markerfacecolor='tab:blue', markeredgecolor='tab:blue', color='tab:blue')
    ax4.set_xlabel('x [mm]', fontsize=font_size)
    ax4.set_ylabel('Residual [µrad]', fontsize=font_size)
    ax4.tick_params(axis='both', labelsize=font_size)

    # Residual RMS
    ax5 = plt.subplot(gs[2, 2])
    ax5.axis('off')
    str_rms = f'Residual:\n{np.nanstd(sx1d_res_urad):.2f} µrad RMS'
    ax5.text(0.5, 0.5, str_rms, fontsize=large_font_size, fontweight='bold', ha='center', va='center', color='tab:blue', transform=ax5.transAxes)

    plt.show()