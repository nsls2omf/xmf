# XMF Matlab functions

## fig_show

<a id="module-matlab.fig_show"></a>

### matlab.fig_show.fig_show_1d_fitting_height(x1d, z1d_measured, z1d_fit, z1d_res, input_params_struct, opt_params_struct, opt_params_ci_struct, str_title)

fig_show_1d_fitting_height - Show the fitting results of 1D height data

Input:
: - x1d - 1D lateral coordinates [m]
  - z1d_measured - Measured height data [m]
  - z1d_fit - Fitted height data [m]
  - z1d_res - Residuals [m]
  - input_params_struct - Input parameters structure
  - opt_params_struct - Optimized parameters structure
  - opt_params_ci_struct - Confidence intervals structure
  - str_title - Title string for the figure

### matlab.fig_show.fig_show_1d_fitting_slope(x1d, sx1d_measured, sx1d_fit, sx1d_res, input_params_struct, opt_params_struct, opt_params_ci_struct, str_title)

fig_show_1d_fitting_slope - Show the fitting results of 1D slope data

Input:
: - x1d - 1D lateral coordinates [m]
  - sx1d_measured - Measured slope data [rad/m]
  - sx1d_fit - Fitted slope data [rad/m]
  - sx1d_res - Residuals [rad/m]
  - input_params_struct - Input parameters structure
  - opt_params_struct - Optimized parameters structure
  - opt_params_ci_struct - Confidence intervals structure
  - str_title - Title string for the figure

### matlab.fig_show.fig_show_2d_fitting_map(x1d, y1d, z2d_measured, z2d_fit, z2d_res, input_params_struct, opt_params_struct, opt_params_ci_struct, str_title)

fig_show_2d_fitting_map - Show the fitting results of 2D map data

Input:
: - x1d - 1D lateral coordinates [m]
  - y1d - 1D lateral coordinates [m]
  - z2d_measured - 2D measured data [m]
  - z2d_fit - 2D fitted data [m]
  - z2d_res - 2D residuals [m]
  - input_params_struct - Input parameters structure
  - opt_params_struct - Optimized parameters structure
  - opt_params_ci_struct - Confidence intervals structure
  - str_title - Title string for the figure

### matlab.fig_show.fig_compare_1d_slope(x1d, sx1d, sx1d_nominal, str_title)

fig_compare_1d_slope - Show the comparison of 1D slope data against nominal values
This function plots the measured slope data and the nominal slope data

Input:
: - x1d - 1D lateral coordinates [m]
  - sx1d - Measured slope data [rad/m]
  - sx1d_nominal - Nominal slope data [rad/m]
  - str_title - Title string for the figure

### matlab.fig_show.fig_compare_1d_height(x1d, z1d, z1d_nominal, str_title)

fig_compare_1d_height - Show the comparison of 1D height data against nominal values
This function plots the measured height data and the nominal height data

Input:
: - x1d - 1D lateral coordinates [m]
  - z1d - Measured height data [m]
  - z1d_nominal - Nominal height data [m]
  - str_title - Title string for the figure

### matlab.fig_show.fig_show_2d_different_fitting_maps(x1d, y1d, z2d_measured, z2d_fit_1, z2d_res_1, z2d_fit_2, z2d_res_2, input_params_struct, opt_params_struct_1, opt_params_ci_struct_1, opt_params_struct_2, opt_params_ci_struct_2, str_title)

fig_show_2d_different_fitting_maps - Show the different fitting results of 2D map data

Input:
: - x1d - 1D lateral coordinates [m]
  - y1d - 1D lateral coordinates [m]
  - z2d_measured - 2D measured data [m]
  - z2d_fit_1 - 2D fitted data [m]
  - z2d_res_1 - 2D residuals [m]
  - z2d_fit_2 - 2D fitted data [m]
  - z2d_res_2 - 2D residuals [m]
  - input_params_struct - Input parameters structure
  - opt_params_struct_1 - Optimized parameters structure 1
  - opt_params_ci_struct_1 - Confidence intervals structure 1
  - opt_params_struct_2 - Optimized parameters structure 2
  - opt_params_ci_struct_2 - Confidence intervals structure 2
  - str_title - Title string for the figure

### matlab.fig_show.fig_compare_2d_map(x1d, y1d, z2d, z2d_quad_sln, str_title)

fig_compare_2d_map - Show the comparison of 2D maps

Input:
: - x1d - 1D lateral coordinates [m]
  - y1d - 1D lateral coordinates [m]
  - z2d - 2D measured data [m]
  - z2d_quad_sln - 2D fitted data [m]
  - str_title - Title string for the figure

## layer_01_standard

<a id="module-matlab.layer_01_standard"></a>

### matlab.layer_01_standard.standard_concave_hyperbolic_cylinder_xslope(x, abs_p, abs_q, theta)

standard_concave_hyperbolic_cylinder_xslope(x, abs_p, abs_q, theta) - Computes the x-slope of a concave hyperbolic cylinder
at a given x-coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x - 2D x-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z2d_quad_sln_quadrics - Quadratic solution for the concave hyperbolic cylinder x-slope
  - z2d_expression_quadrics - Expression for the concave hyperbolic cylinder x-slope

### matlab.layer_01_standard.standard_right_hyperbolic_cylinder_height(x, abs_p, abs_q, theta)

standard_right_hyperbolic_cylinder_height(x, abs_p, abs_q, theta) - Computes the height of a right hyperbolic cylinder
at a given x-coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x - 2D x-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z_quad_sln - Quadratic solution for the right hyperbolic cylinder height
  - z_expression - Expression for the right hyperbolic cylinder height

### matlab.layer_01_standard.standard_right_hyperbolic_cylinder_slope(x, abs_p, abs_q, theta)

standard_right_hyperbolic_cylinder_slope(x, abs_p, abs_q, theta) - Computes the x-slope of a right hyperbolic cylinder
at a given x-coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x - 2D x-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - sx - x-slope of the right hyperbolic cylinder at the given x-coordinates

### matlab.layer_01_standard.standard_convex_hyperbolic_cylinder_xslope(x, abs_p, abs_q, theta)

standard_convex_hyperbolic_cylinder_xslope(x, abs_p, abs_q, theta) - Computes the x-slope of a convex hyperbolic cylinder
at a given x-coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x - 2D x-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z2d_quad_sln_quadrics - Quadratic solution for the convex hyperbolic cylinder x-slope
  - z2d_expression_quadrics - Expression for the convex hyperbolic cylinder x-slope

### matlab.layer_01_standard.standard_left_hyperbolic_cylinder_slope(x, abs_p, abs_q, theta)

standard_left_hyperbolic_cylinder_slope(x, abs_p, abs_q, theta) - Computes the x-slope of a left hyperbolic cylinder
at a given x-coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x - 2D x-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - sx - x-slope of the left hyperbolic cylinder at the given x-coordinates

### matlab.layer_01_standard.standard_concave_elliptic_cylinder_xslope(x, abs_p, abs_q, theta)

standard_concave_elliptic_cylinder_xslope(x, abs_p, abs_q, theta) - Computes the x-slope of a concave elliptic cylinder
at a given x-coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x - 2D x-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z2d_quad_sln_quadrics - Quadratic solution for the concave elliptic cylinder x-slope
  - z2d_expression_quadrics - Expression for the concave elliptic cylinder x-slope

### matlab.layer_01_standard.standard_left_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta)

standard_left_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta) - Computes the height of a left hyperboloid
at a given (x, y) coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x2d - 2D x-coordinates (vector or matrix)
  - y2d - 2D y-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z2d_quad_sln - Quadratic solution for the left hyperboloid height
  - z2d_expression - Expression for the left hyperboloid height

### matlab.layer_01_standard.standard_quadric_cylinder_height(x2d, p, q, theta)

standard_quadric_cylinder_height(x2d, p, q, theta) - Computes the height of a quadric cylinder
at a given x-coordinate, based on the parameters p and q and the grazing incidence angle (theta).

Inputs:
: - x2d - 2D x-coordinates (vector or matrix)
  - p - Distance between the source and the chief ray intersection on mirror
  - q - Distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z2d_quad_sln - Quadratic solution for the quadric cylinder height
  - z2d_expression - Expression for the quadric cylinder height

### matlab.layer_01_standard.standard_convex_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta)

standard_convex_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta) - Computes the height of a convex hyperboloid
at a given (x, y) coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x2d - 2D x-coordinates (vector or matrix)
  - y2d - 2D y-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z2d_quad_sln_quadrics - Quadratic solution for the convex hyperboloid height
  - z2d_expression_quadrics - Expression for the convex hyperboloid height

### matlab.layer_01_standard.standard_convex_ellipsoid_height(x2d, y2d, abs_p, abs_q, theta)

standard_convex_ellipsoid_height(x2d, y2d, abs_p, abs_q, theta) - Computes the height of a convex ellipsoid
at a given (x, y) coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x2d - 2D x-coordinates (vector or matrix)
  - y2d - 2D y-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z2d_quad_sln_quadrics - Quadratic solution for the convex ellipsoid height
  - z2d_expression_quadrics - Expression for the convex ellipsoid height

### matlab.layer_01_standard.standard_convex_elliptic_cylinder_height(x, abs_p, abs_q, theta)

standard_convex_elliptic_cylinder_height(x, abs_p, abs_q, theta) - Computes the height of a convex elliptic cylinder
at a given x-coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x - 2D x-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z2d_quad_sln_quadrics - Quadratic solution for the convex elliptic cylinder height
  - z2d_expression_quadrics - Expression for the convex elliptic cylinder height

### matlab.layer_01_standard.standard_convex_elliptic_cylinder_xslope(x, abs_p, abs_q, theta)

standard_convex_elliptic_cylinder_xslope(x, abs_p, abs_q, theta) - Computes the x-slope of a convex elliptic cylinder
at a given x-coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x - 2D x-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z2d_quad_sln_quadrics - Quadratic solution for the convex elliptic cylinder x-slope
  - z2d_expression_quadrics - Expression for the convex elliptic cylinder x-slope

### matlab.layer_01_standard.standard_concave_elliptic_cylinder_height(x, abs_p, abs_q, theta)

standard_concave_elliptic_cylinder_height(x, abs_p, abs_q, theta) - Computes the height of a concave elliptic cylinder
at a given x-coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x - 2D x-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z2d_quad_sln_quadrics - Quadratic solution for the concave elliptic cylinder height
  - z2d_expression_quadrics - Expression for the concave elliptic cylinder height

### matlab.layer_01_standard.standard_concave_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta)

standard_concave_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta) - Computes the height of a concave hyperboloid
at a given (x, y) coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x2d - 2D x-coordinates (vector or matrix)
  - y2d - 2D y-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z2d_quad_sln_quadrics - Quadratic solution for the concave hyperboloid height
  - z2d_expression_quadrics - Expression for the concave hyperboloid height

### matlab.layer_01_standard.standard_concave_ellipsoid_height(x2d, y2d, abs_p, abs_q, theta)

Computes the height of a concave ellipsoid at given 2D coordinates.

Inputs:
: - x2d - 2D x-coordinates (vector or matrix)
  - y2d - 2D y-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z2d_quad_sln_quadrics - Quadratic solution for the concave ellipsoid height
  - z2d_expression_quadrics - Expression for the concave ellipsoid height

### matlab.layer_01_standard.standard_convex_hyperbolic_cylinder_height(x, abs_p, abs_q, theta)

standard_convex_hyperbolic_cylinder_height(x, abs_p, abs_q, theta) - Computes the height of a convex hyperbolic cylinder
at a given x-coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x - 2D x-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z2d_quad_sln_quadrics - Quadratic solution for the convex hyperbolic cylinder height
  - z2d_expression_quadrics - Expression for the convex hyperbolic cylinder height

### matlab.layer_01_standard.standard_quadrics_height(x2d, y2d, p, q, theta)

standard_quadrics_height(x2d, y2d, p, q, theta) - Computes the height of a quadric surface
at a given (x, y) coordinate, based on the parameters p and q and the grazing incidence angle (theta).

Inputs:
: - x2d - 2D x-coordinates (vector or matrix)
  - y2d - 2D y-coordinates (vector or matrix)
  - p - Distance between the source and the chief ray intersection on mirror
  - q - Distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z2d_quad_sln - Quadratic solution for the quadric surface height
  - z2d_expression - Expression for the quadric surface height

### matlab.layer_01_standard.standard_concave_hyperbolic_cylinder_height(x, abs_p, abs_q, theta)

standard_concave_hyperbolic_cylinder_height(x, abs_p, abs_q, theta) - Computes the height of a concave hyperbolic cylinder
at a given x-coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x - 2D x-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z2d_quad_sln_quadrics - Quadratic solution for the concave hyperbolic cylinder height
  - z2d_expression_quadrics - Expression for the concave hyperbolic cylinder height

### matlab.layer_01_standard.standard_left_hyperbolic_cylinder_height(x, abs_p, abs_q, theta)

standard_left_hyperbolic_cylinder_height(x, abs_p, abs_q, theta) - Computes the height of a left hyperbolic cylinder
at a given x-coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x - 2D x-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z_quad_sln - Quadratic solution for the left hyperbolic cylinder height
  - z_expression - Expression for the left hyperbolic cylinder height

### matlab.layer_01_standard.standard_quadric_cylinder_xslope(x, p, q, theta)

standard_quadric_cylinder_xslope(x, p, q, theta) - Computes the x-slope of a quadric cylinder
at a given x-coordinate, based on the parameters p and q and the grazing incidence angle (theta).

Inputs:
: - x - 2D x-coordinates (vector or matrix)
  - p - Distance between the source and the chief ray intersection on mirror
  - q - Distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - sx - x-slope of the quadric cylinder at the given x-coordinates

### matlab.layer_01_standard.standard_right_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta)

standard_right_hyperboloid_height(x2d, y2d, abs_p, abs_q, theta) - Computes the height of a right hyperboloid
at a given (x, y) coordinate, based on the absolute values of p and q and the grazing incidence angle (theta).

Inputs:
: - x2d - 2D x-coordinates (vector or matrix)
  - y2d - 2D y-coordinates (vector or matrix)
  - abs_p - Absolute value of the distance between the source and the chief ray intersection on mirror
  - abs_q - Absolute value of the distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)

Outputs:
: - z2d_quad_sln - Quadratic solution for the right hyperboloid height
  - z2d_expression - Expression for the right hyperboloid height

## layer_02_generation

<a id="module-matlab.layer_02_generation"></a>

### matlab.layer_02_generation.generate_2d_curved_surface_height(standard_height_function_handle, x2d, y2d, p, q, theta, x_i, y_i, z_i, alpha, beta, gamma, z2d_measured)

generate_2d_curved_surface_height(standard_height_function_handle, x2d, y2d, p, q, theta, x_i, y_i, z_i, alpha, beta, gamma, z2d_measured)
- Generates a 2D height map for a curved surface

> Inputs:
> : - standard_height_function_handle - Handle to the standard height function (e.g., standard_sag_col_diaboloid_height)
>   - x2d - 2D x-coordinates (vector or matrix)
>   - y2d - 2D y-coordinates (vector or matrix)
>   - p - Distance between the source and the chief ray intersection on mirror
>   - q - Distance between the focus and the chief ray intersection on mirror
>   - theta - Grazing incidence angle (in radians)
>   - x_i - x-translation in the conversion from standard mirror coordinates to metrology coordinates
>   - y_i - y-translation in the conversion from standard mirror coordinates to metrology coordinates
>   - z_i - z-translation in the conversion from standard mirror coordinates to metrology coordinates
>   - alpha - Rotation angle along x-axis in standard mirror coordinates
>   - beta - Rotation angle along y-axis in standard mirror coordinates
>   - gamma - Rotation angle along z-axis in standard mirror coordinates
>   - z2d_measured - (Optional) The height map from metrology, if available

> Outputs:
> : - z2d - 2D height map of the curved surface in metrology coordinates

### matlab.layer_02_generation.generate_1d_slope(standard_slope_function_handle, x1d, p, q, theta, x_i, beta)

generate_1d_slope - Generates a 1D slope profile for a grazing incidence X-ray mirror

Inputs:
: - standard_slope_function_handle - Handle to the standard slope function
  - x1d - 1D x-coordinates (vector)
  - p - Distance between the source and the chief ray intersection on mirror
  - q - Distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)
  - x_i - x-translation in the conversion from standard mirror coordinates to metrology coordinates
  - beta - Rotation angle along y-axis in standard mirror coordinates

Outputs:
: - sx1d - 1D slope profile of the grazing incidence X-ray mirror in metrology coordinates

### matlab.layer_02_generation.compose_transformation_matrix(alpha, beta, gamma, x_i, y_i, z_i)

compose_transformation_matrix(alpha, beta, gamma, x_i, y_i, z_i) - Composes a transformation matrix
that includes rotation and translation based on the provided angles and translations.

Inputs:
: - alpha - Rotation angle along x-axis in radians
  - beta - Rotation angle along y-axis in radians
  - gamma - Rotation angle along z-axis in radians
  - x_i - x-translation in the conversion from standard mirror coordinates to metrology coordinates
  - y_i - y-translation in the conversion from standard mirror coordinates to metrology coordinates
  - z_i - z-translation in the conversion from standard mirror coordinates to metrology coordinates

Outputs:
: - T - Transformation matrix (4x4)
  - R - Rotation matrix (3x3)
  - t - Translation vector (3x1)

### matlab.layer_02_generation.generate_1d_height(standard_height_function_handle, x1d, p, q, theta, x_i, z_i, beta, z1d_measured)

generate_1d_height - Generates a 1D height profile for a grazing incidence X-ray mirror

Inputs:
: - standard_height_function_handle - Handle to the standard height function (e.g., standard_circular_cylinder_height)
  - x1d - 1D x-coordinates (vector)
  - p - Distance between the source and the chief ray intersection on mirror
  - q - Distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)
  - x_i - x-translation in the conversion from standard mirror coordinates to metrology coordinates
  - z_i - z-translation in the conversion from standard mirror coordinates to metrology coordinates
  - beta - Rotation angle along y-axis in standard mirror coordinates
  - z1d_measured - (Optional) The height map from metrology, if available

Outputs:
: - z1d - 1D height profile of the grazing incidence X-ray mirror in metrology coordinates

### matlab.layer_02_generation.iter_genereate_height(standard_height_function_handle, x2d, y2d, p, q, theta, tf, z2d_measured, thr_rms_dxy)

Iteratively generates the height map in metrology coordinates

Inputs:
: - standard_height_function_handle - Handle to the standard height function (e.g., standard_circular_cylinder_height)
  - x2d - 2D x-coordinates (vector or matrix)
  - y2d - 2D y-coordinates (vector or matrix)
  - p - Distance between the source and the chief ray intersection on mirror
  - q - Distance between the focus and the chief ray intersection on mirror
  - theta - Grazing incidence angle (in radians)
  - tf - Transformation matrix from standard mirror coordinates to metrology coordinates
  - z2d_measured - (Optional) The height map from metrology, if available
  - thr_rms_dxy - (Optional) Threshold for the RMS of the distances in lateral coordinates (default: 1e-9)

Outputs:
: - z2d - 2D height map of the curved surface in metrology coordinates

### matlab.layer_02_generation.generate_2d_cylinder_height(standard_height_function_handle, x2d, y2d, p, q, theta, x_i, z_i, alpha, beta, gamma, z2d_measured)

- Generates a 2D height map for a circular cylinder

  Inputs:
  : - standard_height_function_handle - Handle to the standard height function (e.g., standard_circular_cylinder_height)
    - x2d - 2D x-coordinates (vector or matrix)
    - y2d - 2D y-coordinates (vector or matrix)
    - p - Distance between the source and the chief ray intersection on mirror
    - q - Distance between the focus and the chief ray intersection on mirror
    - theta - Grazing incidence angle (in radians)
    - x_i - x-translation in the conversion from standard mirror coordinates to metrology coordinates
    - z_i - z-translation in the conversion from standard mirror coordinates to metrology coordinates
    - alpha - Rotation angle along x-axis in standard mirror coordinates
    - beta - Rotation angle along y-axis in standard mirror coordinates
    - gamma - Rotation angle along z-axis in standard mirror coordinates
    - z2d_measured - (Optional) The height map from metrology, if available

  Outputs:
  : - z2d - 2D height map of the circular cylinder in metrology coordinates

## layer_03_optimization

<a id="module-matlab.layer_03_optimization"></a>

### matlab.layer_03_optimization.optimize_parameters_with_tol(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, input_params_struct, tol_struct)

optimize_parameters_with_tol provide a convenient way to optimize the
surface parameters with tolerance from the measurement data.

> Input:
> : - surface_generation_function_handle is function handle for surface generation
>   - standard_surface_shape_function_handle is function handle for a standard surface shape
>   - x is the measured x-coordinate, in unit of [m] as a suggestion
>   - y is the measured y-coordinate, in unit of [m] as a suggestion
>   - v is the measured slope or height in [rad] or [m] as a suggestion
>   - input_params_struct contains p, q, theta, x_i(optional), y_i(optional), z_i(optional), alpha(optional), beta(optional) and gamma(optional) target parameters
>   - tol_struct is a structure to set the tolerance values for p, q, theta, x_i, y_i, z_i, alpha, beta, gamma.

> Output:
> : - v_res is the residual in [m], if the input x and z are in [m]
>   - v_fit is fitting result in [m], if the input x and z are in [m]
>   - opt_params_struct is the optimized params in structure
>   - opt_params_ci_struct is the confidence intervals of the parameters
>   - init_params contains the used initial parameters.

### matlab.layer_03_optimization.optimize_parameters(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, input_params_struct, opt_or_tol_struct)

optimize_parameters provide a convenient way to optimize the surface
parameters from measurement data.

> Input:
> : - surface_generation_function_handle is function handle for surface generation
>   - standard_surface_shape_function_handle is function handle for a standard surface shape
>   - x is the measured x-coordinate, in unit of [m] as a suggestion
>   - y is the measured y-coordinate, in unit of [m] as a suggestion
>   - v is the measured slope or height in [rad] or [m] as a suggestion
>   - input_params_struct contains p, q, theta, x_i(optional), y_i(optional), z_i(optional), alpha(optional), beta(optional) and gamma(optional) target parameters, suggested in unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
>   - opt_or_tol_struct is a structure of optimization flag or tolerance for p, q, theta, x_i, y_i, z_i, alpha, beta, gamma.

> Output:
> : - v_res is the residual in [m], if the input x and z are in [m]
>   - v_fit is fitting result in [m], if the input x and z are in [m]
>   - opt_params_struct is the optimized params in structure
>   - params_ci_struct is the confidence intervals of the parameters.
>   - init_params contains the used initial parameters.

### matlab.layer_03_optimization.optimize_parameters_with_opt(surface_generation_function_handle, standard_surface_shape_function_handle, x, y, v, input_params_struct, opt_struct)

optimize_parameters provide a convenient way to optimize the surface
parameters from measurement data.

> Input:

> > - surface_generation_function_handle is function handle for surface generation
> > - standard_surface_shape_function_handle is function handle for a standard surface shape
> > - x is the measured x-coordinate, in unit of [m] as a suggestion
> > - y is the measured y-coordinate, in unit of [m] as a suggestion
> > - v is the measured slope or height in [rad] or [m] as a suggestion
> > - input_params_struct contains p, q, theta, x_i(optional), y_i(optional), z_i(optional), alpha(optional), beta(optional) and gamma(optional) target parameters, suggested in unit of [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
> > - opt_struct is a structure to set whether optimization is needed for p, q, theta, x_i, y_i, z_i, alpha, beta, gamma.

> Output:
> : - v_res is the residual in [m], if the input x and z are in [m]
>   - v_fit is fitting result in [m], if the input x and z are in [m]
>   - opt_params_struct is the optimized params in structure
>   - opt_params_ci_struct is the confidence intervals of the parameters
>   - init_params contains the used initial parameters.

## layer_04_fit

<a id="module-matlab.layer_04_fit"></a>

### matlab.layer_04_fit.fit_concave_ellipse_slope(x1d, sx1d_measured, input_params_struct, opt_or_tol_struct)

fit_concave_ellipse_slope - Fits a concave elliptic cylinder to a 1D slope profile

Inputs:
: - x1d - 1D x-coordinates (vector)
  - sx1d_measured - 1D slope values (vector)
  - input_params_struct - Structure containing initial parameters for the fit
  - opt_or_tol_struct - Structure containing optimization or tolerance parameters

Outputs:
: - sx1d_res - Residuals of the fitted slope profile
  - sx1d_fit - Fitted slope profile
  - params - Fitted parameters of the concave elliptic cylinder
  - params_ci - Confidence intervals of the fitted parameters

### matlab.layer_04_fit.fit_concave_hyperbola_height(x1d, z1d_measured, input_params_struct, opt_or_tol_struct)

fit_concave_hyperbola_height - Fits a concave hyperbolic cylinder to a 1D height profile

Inputs:
: - x1d - 1D x-coordinates (vector)
  - z1d_measured - 1D height values (vector)
  - input_params_struct - Structure containing initial parameters for the fit
  - opt_or_tol_struct - Structure containing optimization or tolerance parameters

Outputs:
: - z1d_res - Residuals of the fitted height profile
  - z1d_fit - Fitted height profile
  - params - Fitted parameters of the concave hyperbolic cylinder
  - params_ci - Confidence intervals of the fitted parameters

### matlab.layer_04_fit.fit_convex_ellipsoid_height(x2d, y2d, z2d, input_params_struct, opt_or_tol_struct)

fit_convex_ellipsoid_height - Fits a convex ellipsoid to a 2D height map

Inputs:
: - x2d - 2D x-coordinates (matrix)
  - y2d - 2D y-coordinates (matrix)
  - z2d - 2D height values (matrix)
  - input_params_struct - Structure containing initial parameters for the fit
  - opt_or_tol_struct - Structure containing optimization or tolerance parameters

Outputs:
: - z2d_res - Residuals of the fitted height map
  - z2d_fit - Fitted height map
  - params - Fitted parameters of the convex ellipsoid
  - params_ci - Confidence intervals of the fitted parameters

### matlab.layer_04_fit.fit_convex_hyperbola_slope(x1d, sx1d_measured, input_params_struct, opt_or_tol_struct)

fit_convex_hyperbola_slope - Fits a convex hyperbolic cylinder to a 1D slope profile

Inputs:
: - x1d - 1D x-coordinates (vector)
  - sx1d_measured - 1D slope values (vector)
  - input_params_struct - Structure containing initial parameters for the fit
  - opt_or_tol_struct - Structure containing optimization or tolerance parameters

Outputs:
: - sx1d_res - Residuals of the fitted slope profile
  - sx1d_fit - Fitted slope profile
  - params - Fitted parameters of the convex hyperbolic cylinder
  - params_ci - Confidence intervals of the fitted parameters

### matlab.layer_04_fit.fit_convex_ellipse_height(x1d, z1d_measured, input_params_struct, opt_or_tol_struct)

fit_convex_ellipse_height - Fits a convex elliptic cylinder to a 1D height profile

Inputs:
: - x1d - 1D x-coordinates (vector)
  - z1d_measured - 1D height values (vector)
  - input_params_struct - Structure containing initial parameters for the fit
  - opt_or_tol_struct - Structure containing optimization or tolerance parameters

Outputs:
: - z1d_res - Residuals of the fitted height profile
  - z1d_fit - Fitted height profile
  - params - Fitted parameters of the convex elliptic cylinder
  - params_ci - Confidence intervals of the fitted parameters

### matlab.layer_04_fit.fit_concave_hyperbola_slope(x1d, sx1d_measured, input_params_struct, opt_or_tol_struct)

fit_concave_hyperbola_slope - Fits a concave hyperbolic cylinder to a 1D slope profile

Inputs:
: - x1d - 1D x-coordinates (vector)
  - sx1d_measured - 1D slope values (vector)
  - input_params_struct - Structure containing initial parameters for the fit
  - opt_or_tol_struct - Structure containing optimization or tolerance parameters

Outputs:
: - sx1d_res - Residuals of the fitted slope profile
  - sx1d_fit - Fitted slope profile
  - params - Fitted parameters of the concave hyperbolic cylinder
  - params_ci - Confidence intervals of the fitted parameters

### matlab.layer_04_fit.fit_convex_hyperboloid_height(x2d, y2d, z2d, input_params_struct, opt_or_tol_struct)

fit_convex_hyperboloid_height - Fits a convex hyperboloid to a 2D height map

Inputs:
: - x2d - 2D x-coordinates (matrix)
  - y2d - 2D y-coordinates (matrix)
  - z2d - 2D height values (matrix)
  - input_params_struct - Structure containing initial parameters for the fit
  - opt_or_tol_struct - Structure containing optimization or tolerance parameters

Outputs:
: - z2d_res - Residuals of the fitted height map
  - z2d_fit - Fitted height map
  - params - Fitted parameters of the convex hyperboloid
  - params_ci - Confidence intervals of the fitted parameters

### matlab.layer_04_fit.fit_concave_hyperboloid_height(x2d, y2d, z2d, input_params_struct, opt_or_tol_struct)

fit_concave_hyperboloid_height - Fits a concave hyperboloid to a 2D height map

Inputs:
: - x2d - 2D x-coordinates (matrix)
  - y2d - 2D y-coordinates (matrix)
  - z2d - 2D height values (matrix)
  - input_params_struct - Structure containing initial parameters for the fit
  - opt_or_tol_struct - Structure containing optimization or tolerance parameters

Outputs:
: - z2d_res - Residuals of the fitted height map
  - z2d_fit - Fitted height map
  - params - Fitted parameters of the concave hyperboloid
  - params_ci - Confidence intervals of the fitted parameters

### matlab.layer_04_fit.fit_concave_hyperbolic_cylinder_height(x2d, y2d, z2d, input_params_struct, opt_or_tol_struct)

fit_concave_hyperbolic_cylinder_height - Fits a concave hyperbolic cylinder to a 2D height map

Inputs:
: - x2d - 2D x-coordinates (matrix)
  - y2d - 2D y-coordinates (matrix)
  - z2d - 2D height values (matrix)
  - input_params_struct - Structure containing initial parameters for the fit
  - opt_or_tol_struct - Structure containing optimization or tolerance parameters

Outputs:
: - z2d_res - Residuals of the fitted height map
  - z2d_fit - Fitted height map
  - params - Fitted parameters of the concave hyperbolic cylinder
  - params_ci - Confidence intervals of the fitted parameters

### matlab.layer_04_fit.fit_convex_hyperbolic_cylinder_height(x2d, y2d, z2d, input_params_struct, opt_or_tol_struct)

fit_convex_hyperbolic_cylinder_height - Fits a convex hyperbolic cylinder to a 2D height map

Inputs:
: - x2d - 2D x-coordinates (matrix)
  - y2d - 2D y-coordinates (matrix)
  - z2d - 2D height values (matrix)
  - input_params_struct - Structure containing initial parameters for the fit
  - opt_or_tol_struct - Structure containing optimization or tolerance parameters

Outputs:
: - z2d_res - Residuals of the fitted height map
  - z2d_fit - Fitted height map
  - params - Fitted parameters of the convex hyperbolic cylinder
  - params_ci - Confidence intervals of the fitted parameters

### matlab.layer_04_fit.fit_convex_ellipse_slope(x1d, sx1d_measured, input_params_struct, opt_or_tol_struct)

fit_convex_ellipse_slope - Fits a convex elliptic cylinder to a 1D slope profile

Inputs:
: - x1d - 1D x-coordinates (vector)
  - sx1d_measured - 1D slope values (vector)
  - input_params_struct - Structure containing initial parameters for the fit
  - opt_or_tol_struct - Structure containing optimization or tolerance parameters

Outputs:
: - sx1d_res - Residuals of the fitted slope profile
  - sx1d_fit - Fitted slope profile
  - params - Fitted parameters of the convex elliptic cylinder
  - params_ci - Confidence intervals of the fitted parameters

### matlab.layer_04_fit.fit_concave_ellipse_height(x1d, z1d_measured, input_params_struct, opt_or_tol_struct)

fit_concave_ellipse_height - Fits a concave elliptic cylinder to a 1D height profile

Inputs:
: - x1d - 1D x-coordinates (vector)
  - z1d_measured - 1D height values (vector)
  - input_params_struct - Structure containing initial parameters for the fit
  - opt_or_tol_struct - Structure containing optimization or tolerance parameters

Outputs:
: - z1d_res - Residuals of the fitted height profile
  - z1d_fit - Fitted height profile
  - params - Fitted parameters of the concave elliptic cylinder
  - params_ci - Confidence intervals of the fitted parameters

### matlab.layer_04_fit.fit_convex_hyperbola_height(x1d, z1d_measured, input_params_struct, opt_or_tol_struct)

fit_convex_hyperbola_height - Fits a convex hyperbolic cylinder to a 1D height profile

Inputs:
: - x1d - 1D x-coordinates (vector)
  - z1d_measured - 1D height values (vector)
  - input_params_struct - Structure containing initial parameters for the fit
  - opt_or_tol_struct - Structure containing optimization or tolerance parameters

Outputs:
: - z1d_res - Residuals of the fitted height profile
  - z1d_fit - Fitted height profile
  - params - Fitted parameters of the convex hyperbolic cylinder
  - params_ci - Confidence intervals of the fitted parameters

### matlab.layer_04_fit.fit_concave_ellipsoid_height(x2d, y2d, z2d, input_params_struct, opt_or_tol_struct)

fit_concave_ellipsoid_height - Fits a concave ellipsoid to a 2D height map

Inputs:
: - x2d - 2D x-coordinates (matrix)
  - y2d - 2D y-coordinates (matrix)
  - z2d - 2D height values (matrix)
  - input_params_struct - Structure containing initial parameters for the fit
  - opt_or_tol_struct - Structure containing optimization or tolerance parameters

Outputs:
: - z2d_res - Residuals of the fitted height map
  - z2d_fit - Fitted height map
  - params - Fitted parameters of the concave ellipsoid
  - params_ci - Confidence intervals of the fitted parameters

### matlab.layer_04_fit.fit_concave_elliptic_cylinder_height(x2d, y2d, z2d, input_params_struct, opt_or_tol_struct)

fit_concave_elliptic_cylinder_height - Fits a concave elliptic cylinder to a 2D height map

Inputs:
: - x2d - 2D x-coordinates (matrix)
  - y2d - 2D y-coordinates (matrix)
  - z2d - 2D height values (matrix)
  - input_params_struct - Structure containing initial parameters for the fit
  - opt_or_tol_struct - Structure containing optimization or tolerance parameters

Outputs:
: - z2d_res - Residuals of the fitted height map
  - z2d_fit - Fitted height map
  - params - Fitted parameters of the concave elliptic cylinder
  - params_ci - Confidence intervals of the fitted parameters

### matlab.layer_04_fit.fit_convex_elliptic_cylinder_height(x2d, y2d, z2d, input_params_struct, opt_or_tol_struct)

fit_convex_elliptic_cylinder_height - Fits a convex elliptic cylinder to a 2D height map

Inputs:
: - x2d - 2D x-coordinates (matrix)
  - y2d - 2D y-coordinates (matrix)
  - z2d - 2D height values (matrix)
  - input_params_struct - Structure containing initial parameters for the fit
  - opt_or_tol_struct - Structure containing optimization or tolerance parameters

Outputs:
: - z2d_res - Residuals of the fitted height map
  - z2d_fit - Fitted height map
  - params - Fitted parameters of the convex elliptic cylinder
  - params_ci - Confidence intervals of the fitted parameters

## scripts

<a id="module-matlab"></a>

### matlab.demo_script_05_fit_real_data_with_opt

Demo script to fit real data with optimization parameters

### matlab.demo_script_03_fit_simulation_data_with_opt

Demo script to fit simulation data with optimization parameters

### matlab.demo_script_02_generate_shapes

Demo script to generate shapes

### matlab.demo_script_01_standard_shapes

Demo script to calculate standard shapes

### matlab.demo_script_06_fit_real_data_with_tol

Demo script to fit real data with tolerance parameters

### matlab.demo_script_04_fit_simulation_data_with_tol

Demo script to fit simulation data with tolerance parameters
