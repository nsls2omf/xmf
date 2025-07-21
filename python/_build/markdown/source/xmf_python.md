# XMF API

## Summary table

| [`xmf.fit_convex_ellipsoid_height`](#id18)(x2d, y2d, ...)    | Fit the convex ellipsoid parameters from a measured height map.            |
|--------------------------------------------------------------|----------------------------------------------------------------------------|
| [`xmf.fit_concave_ellipsoid_height`](#id10)(x2d, y2d, ...)   | Fit the concave ellipsoid parameters from a measured height map.           |
| [`xmf.fit_convex_elliptic_cylinder_height`](#id19)(x2d, ...) | Fit the convex elliptic cylinder parameters from a measured height map.    |
| [`xmf.fit_concave_elliptic_cylinder_height`](#id11)(...)     | Fit the concave elliptic cylinder parameters from a measured height map.   |
| [`xmf.fit_convex_ellipse_height`](#id16)(x1d, z1d, ...)      | Fit the convex ellipse parameters from a measured height profile.          |
| [`xmf.fit_concave_ellipse_height`](#id8)(x1d, z1d, ...)      | Fit the concave ellipse parameters from a measured height profile.         |
| [`xmf.fit_convex_ellipse_slope`](#id17)(x1d, sx1d, ...)      | Fit the convex ellipse parameters from a measured slope profile.           |
| [`xmf.fit_concave_ellipse_slope`](#id9)(x1d, sx1d, ...)      | Fit the concave ellipse parameters from a measured slope profile.          |
| [`xmf.fit_concave_hyperboloid_height`](#id15)(x2d, y2d, ...) | Fit the concave hyperboloid parameters from a measured height map.         |
| [`xmf.fit_convex_hyperboloid_height`](#id23)(x2d, y2d, ...)  | Fit the convex hyperboloid parameters from a measured height map.          |
| [`xmf.fit_convex_hyperbolic_cylinder_height`](#id22)(...)    | Fit the convex hyperbolic cylinder parameters from a measured height map.  |
| [`xmf.fit_concave_hyperbolic_cylinder_height`](#id14)(...)   | Fit the concave hyperbolic cylinder parameters from a measured height map. |
| [`xmf.fit_concave_hyperbola_height`](#id12)(x1d, ...)        | Fit the concave hyperbola parameters from a measured height profile.       |
| [`xmf.fit_convex_hyperbola_height`](#id20)(x1d, ...)         | Fit the convex hyperbola parameters from a measured height profile.        |
| [`xmf.fit_convex_hyperbola_slope`](#id21)(x1d, sx1d, ...)    | Fit the convex hyperbola parameters from a measured slope profile.         |
| [`xmf.fit_concave_hyperbola_slope`](#id13)(x1d, sx1d, ...)   | Fit the concave hyperbola parameters from a measured slope profile.        |

## Full API Details

### xmf.fig_compare_1d_height(x1d, z1d_generation, z1d_standard, str_title)

Compare two 1D height data sets and plot the difference

* **Parameters:**
  * **x1d** (numpy.ndarray) – 1D array of x-coordinates
  * **z1d_generation** (numpy.ndarray) – 1D array of height data from generation
  * **z1d_standard** (numpy.ndarray) – 1D array of height data from standard
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_compare_1d_slope(x1d, sx1d_generation, sx1d_standard, str_title)

Compare two 1D slope data sets and plot the difference

* **Parameters:**
  * **x1d** (numpy.ndarray) – 1D array of x-coordinates
  * **sx1d_generation** (numpy.ndarray) – 1D array of slope data from generation
  * **sx1d_standard** (numpy.ndarray) – 1D array of slope data from standard
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show_1d_fitting_height(x1d, z1d_measured, z1d_fit, z1d_res, target_params_dict, opt_params_dict, opt_params_ci_dict, str_title)

Show a 1D fitting plot with measured data, fitted data, residuals, target parameters, and optimized parameters

* **Parameters:**
  * **x1d** (numpy.ndarray) – 1D array of x-coordinates
  * **z1d_measured** (numpy.ndarray) – 1D array of measured z-values
  * **z1d_fit** (numpy.ndarray) – 1D array of fitted z-values
  * **z1d_res** (numpy.ndarray) – 1D array of residuals
  * **target_params_dict** (dict) – Dictionary of target parameters
  * **opt_params_dict** (dict) – Dictionary of optimized parameters
  * **opt_params_ci_dict** (dict) – Dictionary of optimized parameters confidence intervals
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show_1d_fitting_slope(x1d, sx1d_measured, sx1d_fit, sx1d_res, target_params_dict, opt_params_dict, opt_params_ci_dict, str_title)

Show a 1D fitting plot with measured slopes, fitted slopes, residuals, target parameters, and optimized parameters

* **Parameters:**
  * **x1d** (numpy.ndarray) – 1D array of x-coordinates
  * **sx1d_measured** (numpy.ndarray) – 1D array of measured slopes
  * **sx1d_fit** (numpy.ndarray) – 1D array of fitted slopes
  * **sx1d_res** (numpy.ndarray) – 1D array of residuals
  * **target_params_dict** (dict) – Dictionary of target parameters
  * **opt_params_dict** (dict) – Dictionary of optimized parameters
  * **opt_params_ci_dict** (dict) – Dictionary of optimized parameters confidence intervals
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show_1d_height(x1d, z1d_quad_sln, z1d_expression, str_title)

Show a 1D plot of height data from quadratic equation solution and expression

* **Parameters:**
  * **x1d** (numpy.ndarray) – 1D array of x-coordinates
  * **z1d_quad_sln** (numpy.ndarray) – 1D array of height data from quadratic equation solution
  * **z1d_expression** (numpy.ndarray) – 1D array of height data from expression
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show_1d_slope(x1d, sx1d, str_title)

### xmf.fig_show_2d_fitting_map(x2d, y2d, z2d_measured, z2d_fit, z2d_res, target_params_dict, opt_params_dict, opt_params_ci_dict, str_title)

Show a 2D fitting map with colorbar, target parameters, fitted parameters, and residuals

* **Parameters:**
  * **x2d** (numpy.ndarray) – 2D array of x-coordinates
  * **y2d** (numpy.ndarray) – 2D array of y-coordinates
  * **z2d_measured** (numpy.ndarray) – 2D array of measured z-values
  * **z2d_fit** (numpy.ndarray) – 2D array of fitted z-values
  * **z2d_res** (numpy.ndarray) – 2D array of residuals
  * **target_params_dict** (dict) – Dictionary of target parameters
  * **opt_params_dict** (dict) – Dictionary of optimized parameters
  * **opt_params_ci_dict** (dict) – Dictionary of optimized parameters confidence intervals
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show_2d_map(x2d, y2d, z2d_quad_sln, z2d_expression, str_title)

Show a 2D map of height data with colorbar

* **Parameters:**
  * **x2d** (numpy.ndarray) – 2D array of x-coordinates
  * **y2d** (numpy.ndarray) – 2D array of y-coordinates
  * **z2d_quad_sln** (numpy.ndarray) – 2D array of height data from quadratic equation solution
  * **z2d_expression** (numpy.ndarray) – 2D array of height data from expression
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fit_concave_ellipse_height(x1d: ndarray, z1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave ellipse parameters from a measured height profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **z1d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z1d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_concave_ellipse_slope(x1d: ndarray, sx1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave ellipse parameters from a measured slope profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **sx1d** (numpy.ndarray) – The measured slope in the suggested unit of [m/m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **sx1d_fit** (numpy.ndarray) – The fitted slope
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_concave_ellipsoid_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave ellipsoid parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **input_params_dict** (dict) – The input parameters dictionary containing `p`, `q`, `theta`, `x_i` (optional), and `y_i` (optional) in the suggested unit of [m] [m] [rad] [m]
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_concave_elliptic_cylinder_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave elliptic cylinder parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_concave_hyperbola_height(x1d: ndarray, z1d_measured: ndarray, input_params_dict: dict, opt_1d_cylinder_height: dict)

Fit the concave hyperbola parameters from a measured height profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **z1d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z1d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_concave_hyperbola_slope(x1d: ndarray, sx1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave hyperbola parameters from a measured slope profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **sx1d** (numpy.ndarray) – The measured slope in the suggested unit of [m/m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **sx1d_fit** (numpy.ndarray) – The fitted slope
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_concave_hyperbolic_cylinder_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave hyperbolic cylinder parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_concave_hyperboloid_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave hyperboloid parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **input_params_dict** (numpy.ndarray) – The the `p`, `q`, `theta`, `x_i` (optional), and `y_i` (optional) in the suggested unit of [m] [m] [rad] [m]
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_convex_ellipse_height(x1d: ndarray, z1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex ellipse parameters from a measured height profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **z1d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z1d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_convex_ellipse_slope(x1d: ndarray, sx1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex ellipse parameters from a measured slope profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **sx1d** (numpy.ndarray) – The measured slope in the suggested unit of [m/m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **sx1d_fit** (numpy.ndarray) – The fitted slope
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_convex_ellipsoid_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex ellipsoid parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **input_params_dict** (numpy.ndarray) – The the `p`, `q`, `theta`, `x_i` (optional), and `y_i` (optional) in the suggested unit of [m] [m] [rad] [m]
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_convex_elliptic_cylinder_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex elliptic cylinder parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_convex_hyperbola_height(x1d: ndarray, z1d_measured: ndarray, input_params_dict: dict, opt_1d_cylinder_height: dict)

Fit the convex hyperbola parameters from a measured height profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **z1d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z1d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_convex_hyperbola_slope(x1d: ndarray, sx1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex hyperbola parameters from a measured slope profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **sx1d** (numpy.ndarray) – The measured slope in the suggested unit of [m/m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **sx1d_fit** (numpy.ndarray) – The fitted slope
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_convex_hyperbolic_cylinder_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex hyperbolic cylinder parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_convex_hyperboloid_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex hyperboloid parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **input_params_dict** (numpy.ndarray) – The the `p`, `q`, `theta`, `x_i` (optional), and `y_i` (optional) in the suggested unit of [m] [m] [rad] [m]
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.generate_1d_height(standard_height_function: LambdaType, x1d: array, p: float, q: float, theta: float, x_i: float, z_i: float, beta: float, z1d_measured: array = None)

Geneate 1D height map with (`p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`)

* **Parameters:**
  * **standard_height_function** (function) – The standard height function
  * **x1d** (numpy.ndarray) – The 1D x coordinates
  * **p** (float) – The `p` value: the distance from the source to the chief ray intersection
  * **q** (float) – The `q` value: the distance from the chief ray intersection to the focus
  * **theta** (float) – The grazing angle
  * **alpha** (float) – The angle around x-axis
  * **beta** (float) – The angle around y-axis
  * **gamma** (float) – The angle around z-axis
  * **x_i** (float) – x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
  * **z_i** (float) – z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
  * **z1d_measured** (numpy.ndarray) – The measured height map
* **Returns:**
  **z1d** – The height map
* **Return type:**
  numpy.ndarray

### xmf.generate_1d_slope(standard_slope_function: LambdaType, x1d: array, p: float, q: float, theta: float, x_i: float, beta: float)

Generate 1D slope map with (`p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`)

* **Parameters:**
  * **standard_slope_function** (function) – The standard slope function
  * **x1d** (numpy.ndarray) – The 1D x coordinates
  * **p** (float) – The `p` value: the distance from the source to the chief ray intersection
  * **q** (float) – The `q` value: the distance from the chief ray intersection to the focus
  * **theta** (float) – The grazing angle
  * **alpha** (float) – The angle around x-axis
  * **beta** (float) – The angle around y-axis
  * **gamma** (float) – The angle around z-axis
  * **x_i** (float) – x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
  * **sx1d_measured** (numpy.ndarray) – The measured slope map
* **Returns:**
  **sx1d** – The slope map
* **Return type:**
  numpy.ndarray

### xmf.generate_2d_curved_surface_height(standard_height_function: LambdaType, x2d: ndarray, y2d: ndarray, p: float, q: float, theta: float, x_i: float, y_i: float, z_i: float, alpha: float, beta: float, gamma: float, z2d_measured: ndarray = None)

Geneate 2D curved surface height map with (`p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`)

* **Parameters:**
  * **standard_height_function** (function) – The standard height function
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **p** (float) – The `p` value: the distance from the source to the chief ray intersection
  * **q** (float) – The `q` value: the distance from the chief ray intersection to the focus
  * **theta** (float) – The grazing angle
  * **alpha** (float) – The angle around x-axis
  * **beta** (float) – The angle around y-axis
  * **gamma** (float) – The angle around z-axis
  * **x_i** (float) – x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
  * **y_i** (float) – y-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the y-position of chief ray intersection in metrology coordinates
  * **z_i** (float) – z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
  * **z2d_measured** (numpy.ndarray) – The measured height map
* **Returns:**
  **z2d** – The height map
* **Return type:**
  numpy.ndarray

### xmf.generate_2d_cylinder_height(standard_height_function: LambdaType, x2d: ndarray, y2d: ndarray, p: float, q: float, theta: float, x_i: float, z_i: float, alpha: float, beta: float, gamma: float, z2d_measured: ndarray = None)

Geneate 2D cylinder surface height map with (`p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`)

* **Parameters:**
  * **standard_height_function** (function) – The standard height function
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **p** (float) – The `p` value: the distance from the source to the chief ray intersection
  * **q** (float) – The `q` value: the distance from the chief ray intersection to the focus
  * **theta** (float) – The grazing angle
  * **alpha** (float) – The angle around x-axis
  * **beta** (float) – The angle around y-axis
  * **gamma** (float) – The angle around z-axis
  * **x_i** (float) – x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
  * **z_i** (float) – z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
  * **z2d_measured** (numpy.ndarray) – The measured height map
* **Returns:**
  **z2d** – The height map
* **Return type:**
  numpy.ndarray

### xmf.standard_concave_ellipsoid_height(x2d: ndarray, y2d: ndarray, abs_p: float, abs_q: float, theta: float, return_z2d_expression_as_extra: bool = False)

The standard 2D concave ellipsoid height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z2d_expression_as_extra** (bool) – If True, return the z2d_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.standard_concave_elliptic_cylinder_height(x: ndarray, abs_p: float, abs_q: float, theta: float, return_z_expression_as_extra: bool = False)

The standard convex elliptic cylinder height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z_expression_as_extra** (bool) – If True, return the z_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.standard_concave_elliptic_cylinder_xslope(x: ndarray, abs_p: float, abs_q: float, theta: float)

The standard concave elliptic cylinder x-slope with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
* **Returns:**
  **sx** – The x-slope
* **Return type:**
  numpy.ndarray

### xmf.standard_concave_hyperbolic_cylinder_height(x: ndarray, abs_p: float, abs_q: float, theta: float, return_z_expression_as_extra: bool = False)

The standard 2D concave hyperbolic height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The 2D x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z_expression_as_extra** (bool) – If True, return the z_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.standard_concave_hyperbolic_cylinder_xslope(x: ndarray, abs_p: float, abs_q: float, theta: float)

The standard concave hyperbolic cylinder x-slope with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
* **Returns:**
  **sx** – The x-slope
* **Return type:**
  numpy.ndarray

### xmf.standard_concave_hyperboloid_height(x2d: ndarray, y2d: ndarray, abs_p: float, abs_q: float, theta: float, return_z2d_expression_as_extra: bool = False)

The standard 2D concave hyperboloid height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z2d_expression_as_extra** (bool) – If True, return the z2d_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.standard_convex_ellipsoid_height(x2d: ndarray, y2d: ndarray, abs_p: float, abs_q: float, theta: float, return_z2d_expression_as_extra: bool = False)

The standard 2D convex ellipsoid height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z2d_expression_as_extra** (bool) – If True, return the z2d_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.standard_convex_elliptic_cylinder_height(x: ndarray, abs_p: float, abs_q: float, theta: float, return_z_expression_as_extra: bool = False)

The standard convex elliptic cylinder height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z_expression_as_extra** (bool) – If True, return the z_expression as well
* **Returns:**
  **z** – The height
* **Return type:**
  numpy.ndarray

### xmf.standard_convex_elliptic_cylinder_xslope(x: ndarray, abs_p: float, abs_q: float, theta: float)

The standard convex elliptic cylinder x-slope with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
* **Returns:**
  **sx** – The x-slope
* **Return type:**
  numpy.ndarray

### xmf.standard_convex_hyperbolic_cylinder_height(x: ndarray, abs_p: float, abs_q: float, theta: float, return_z_expression_as_extra: bool = False)

The standard 2D convex hyperbolic height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The 2D x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z_expression_as_extra** (bool) – If True, return the z_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.standard_convex_hyperbolic_cylinder_xslope(x: ndarray, abs_p: float, abs_q: float, theta: float)

The standard convex hyperbolic cylinder x-slope with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
* **Returns:**
  **sx** – The x-slope
* **Return type:**
  numpy.ndarray

### xmf.standard_convex_hyperboloid_height(x2d: ndarray, y2d: ndarray, abs_p: float, abs_q: float, theta: float, return_z2d_expression_as_extra: bool = False)

The standard 2D convex hyperboloid height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z2d_expression_as_extra** (bool) – If True, return the z2d_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

# XMF package

## xmf.fig_show module

### xmf.fig_show.add_colorbar(im: \_ScalarMappable, title: str = None, aspect: int = 10, pad_fraction: float = 1.5, \*\*kwargs)

Add a vertical color bar to an image plot

* **Parameters:**
  * **im** (matplotlib.cm.ScalarMappable) – The image to be described by the colorbar
  * **title** (str) – The title of the colorbar
  * **aspect** (int) – The aspect ratio between width and height
  * **pad_fraction** (float) – The padding fraction
* **Returns:**
  **cbar** – The added colorbar
* **Return type:**
  matplotlib.pyplot.colorbar

### xmf.fig_show.fig_compare_1d_height(x1d, z1d_generation, z1d_standard, str_title)

Compare two 1D height data sets and plot the difference

* **Parameters:**
  * **x1d** (numpy.ndarray) – 1D array of x-coordinates
  * **z1d_generation** (numpy.ndarray) – 1D array of height data from generation
  * **z1d_standard** (numpy.ndarray) – 1D array of height data from standard
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show.fig_compare_1d_slope(x1d, sx1d_generation, sx1d_standard, str_title)

Compare two 1D slope data sets and plot the difference

* **Parameters:**
  * **x1d** (numpy.ndarray) – 1D array of x-coordinates
  * **sx1d_generation** (numpy.ndarray) – 1D array of slope data from generation
  * **sx1d_standard** (numpy.ndarray) – 1D array of slope data from standard
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show.fig_show_1d_fitting_height(x1d, z1d_measured, z1d_fit, z1d_res, target_params_dict, opt_params_dict, opt_params_ci_dict, str_title)

Show a 1D fitting plot with measured data, fitted data, residuals, target parameters, and optimized parameters

* **Parameters:**
  * **x1d** (numpy.ndarray) – 1D array of x-coordinates
  * **z1d_measured** (numpy.ndarray) – 1D array of measured z-values
  * **z1d_fit** (numpy.ndarray) – 1D array of fitted z-values
  * **z1d_res** (numpy.ndarray) – 1D array of residuals
  * **target_params_dict** (dict) – Dictionary of target parameters
  * **opt_params_dict** (dict) – Dictionary of optimized parameters
  * **opt_params_ci_dict** (dict) – Dictionary of optimized parameters confidence intervals
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show.fig_show_1d_fitting_slope(x1d, sx1d_measured, sx1d_fit, sx1d_res, target_params_dict, opt_params_dict, opt_params_ci_dict, str_title)

Show a 1D fitting plot with measured slopes, fitted slopes, residuals, target parameters, and optimized parameters

* **Parameters:**
  * **x1d** (numpy.ndarray) – 1D array of x-coordinates
  * **sx1d_measured** (numpy.ndarray) – 1D array of measured slopes
  * **sx1d_fit** (numpy.ndarray) – 1D array of fitted slopes
  * **sx1d_res** (numpy.ndarray) – 1D array of residuals
  * **target_params_dict** (dict) – Dictionary of target parameters
  * **opt_params_dict** (dict) – Dictionary of optimized parameters
  * **opt_params_ci_dict** (dict) – Dictionary of optimized parameters confidence intervals
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show.fig_show_1d_height(x1d, z1d_quad_sln, z1d_expression, str_title)

Show a 1D plot of height data from quadratic equation solution and expression

* **Parameters:**
  * **x1d** (numpy.ndarray) – 1D array of x-coordinates
  * **z1d_quad_sln** (numpy.ndarray) – 1D array of height data from quadratic equation solution
  * **z1d_expression** (numpy.ndarray) – 1D array of height data from expression
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show.fig_show_1d_slope(x1d, sx1d, str_title)

### xmf.fig_show.fig_show_2d_fitting_map(x2d, y2d, z2d_measured, z2d_fit, z2d_res, target_params_dict, opt_params_dict, opt_params_ci_dict, str_title)

Show a 2D fitting map with colorbar, target parameters, fitted parameters, and residuals

* **Parameters:**
  * **x2d** (numpy.ndarray) – 2D array of x-coordinates
  * **y2d** (numpy.ndarray) – 2D array of y-coordinates
  * **z2d_measured** (numpy.ndarray) – 2D array of measured z-values
  * **z2d_fit** (numpy.ndarray) – 2D array of fitted z-values
  * **z2d_res** (numpy.ndarray) – 2D array of residuals
  * **target_params_dict** (dict) – Dictionary of target parameters
  * **opt_params_dict** (dict) – Dictionary of optimized parameters
  * **opt_params_ci_dict** (dict) – Dictionary of optimized parameters confidence intervals
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show.fig_show_2d_map(x2d, y2d, z2d_quad_sln, z2d_expression, str_title)

Show a 2D map of height data with colorbar

* **Parameters:**
  * **x2d** (numpy.ndarray) – 2D array of x-coordinates
  * **y2d** (numpy.ndarray) – 2D array of y-coordinates
  * **z2d_quad_sln** (numpy.ndarray) – 2D array of height data from quadratic equation solution
  * **z2d_expression** (numpy.ndarray) – 2D array of height data from expression
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show.reg_exp_rep(s)

Replace scientific notation in a string with LaTeX format

* **Parameters:**
  **s** (str) – The string to be processed
* **Returns:**
  The processed string with LaTeX format
* **Return type:**
  str

## xmf.layer_01_standard module

### xmf.layer_01_standard.standard_concave_ellipsoid_height(x2d: ndarray, y2d: ndarray, abs_p: float, abs_q: float, theta: float, return_z2d_expression_as_extra: bool = False)

The standard 2D concave ellipsoid height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z2d_expression_as_extra** (bool) – If True, return the z2d_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.layer_01_standard.standard_concave_elliptic_cylinder_height(x: ndarray, abs_p: float, abs_q: float, theta: float, return_z_expression_as_extra: bool = False)

The standard convex elliptic cylinder height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z_expression_as_extra** (bool) – If True, return the z_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.layer_01_standard.standard_concave_elliptic_cylinder_xslope(x: ndarray, abs_p: float, abs_q: float, theta: float)

The standard concave elliptic cylinder x-slope with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
* **Returns:**
  **sx** – The x-slope
* **Return type:**
  numpy.ndarray

### xmf.layer_01_standard.standard_concave_hyperbolic_cylinder_height(x: ndarray, abs_p: float, abs_q: float, theta: float, return_z_expression_as_extra: bool = False)

The standard 2D concave hyperbolic height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The 2D x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z_expression_as_extra** (bool) – If True, return the z_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.layer_01_standard.standard_concave_hyperbolic_cylinder_xslope(x: ndarray, abs_p: float, abs_q: float, theta: float)

The standard concave hyperbolic cylinder x-slope with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
* **Returns:**
  **sx** – The x-slope
* **Return type:**
  numpy.ndarray

### xmf.layer_01_standard.standard_concave_hyperboloid_height(x2d: ndarray, y2d: ndarray, abs_p: float, abs_q: float, theta: float, return_z2d_expression_as_extra: bool = False)

The standard 2D concave hyperboloid height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z2d_expression_as_extra** (bool) – If True, return the z2d_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.layer_01_standard.standard_convex_ellipsoid_height(x2d: ndarray, y2d: ndarray, abs_p: float, abs_q: float, theta: float, return_z2d_expression_as_extra: bool = False)

The standard 2D convex ellipsoid height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z2d_expression_as_extra** (bool) – If True, return the z2d_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.layer_01_standard.standard_convex_elliptic_cylinder_height(x: ndarray, abs_p: float, abs_q: float, theta: float, return_z_expression_as_extra: bool = False)

The standard convex elliptic cylinder height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z_expression_as_extra** (bool) – If True, return the z_expression as well
* **Returns:**
  **z** – The height
* **Return type:**
  numpy.ndarray

### xmf.layer_01_standard.standard_convex_elliptic_cylinder_xslope(x: ndarray, abs_p: float, abs_q: float, theta: float)

The standard convex elliptic cylinder x-slope with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
* **Returns:**
  **sx** – The x-slope
* **Return type:**
  numpy.ndarray

### xmf.layer_01_standard.standard_convex_hyperbolic_cylinder_height(x: ndarray, abs_p: float, abs_q: float, theta: float, return_z_expression_as_extra: bool = False)

The standard 2D convex hyperbolic height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The 2D x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z_expression_as_extra** (bool) – If True, return the z_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.layer_01_standard.standard_convex_hyperbolic_cylinder_xslope(x: ndarray, abs_p: float, abs_q: float, theta: float)

The standard convex hyperbolic cylinder x-slope with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
* **Returns:**
  **sx** – The x-slope
* **Return type:**
  numpy.ndarray

### xmf.layer_01_standard.standard_convex_hyperboloid_height(x2d: ndarray, y2d: ndarray, abs_p: float, abs_q: float, theta: float, return_z2d_expression_as_extra: bool = False)

The standard 2D convex hyperboloid height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z2d_expression_as_extra** (bool) – If True, return the z2d_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.layer_01_standard.standard_quadric_cylinder_height(x: ndarray, p: float, q: float, theta: float, return_z_expression_as_extra: bool = False)

The standard quadric cylinder height with (`p`, `q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **p** (float) – The `p` value: the distance from the source to the chief ray intersection
  * **q** (float) – The `q` value: the distance from the chief ray intersection to the focus
  * **theta** (float) – The grazing angle
  * **return_z_expression_as_extra** (bool) – If True, return the z_expression as well
* **Returns:**
  **z** – The height
* **Return type:**
  numpy.ndarray

### xmf.layer_01_standard.standard_quadric_cylinder_xslope(x: ndarray, p: float, q: float, theta: float)

The standard quadric cylinder slope with (`p`, `q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **p** (float) – The `p` value: the distance from the source to the chief ray intersection
  * **q** (float) – The `q` value: the distance from the chief ray intersection to the focus
  * **theta** (float) – The grazing angle
* **Returns:**
  **sx** – The x-slope
* **Return type:**
  numpy.ndarray

### xmf.layer_01_standard.standard_quadrics_height(x2d: ndarray, y2d: ndarray, p: float, q: float, theta: float, return_z2d_expression_as_extra: bool = False)

The standard quadrics height with (`p`, `q`, `theta`)

* **Parameters:**
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **p** (float) – The `p` value: the distance from the source to the chief ray intersection
  * **q** (float) – The `q` value: the distance from the chief ray intersection to the focus
  * **theta** (float) – The grazing angle
  * **return_z2d_expression_as_extra** (bool) – If True, return the z2d_expression as well
* **Returns:**
  **z2d_quad_sln** – The 2D height map
* **Return type:**
  numpy.ndarray

## xmf.layer_02_generation module

### xmf.layer_02_generation.compose_transformation_matrix(alpha: float, beta: float, gamma: float, x_i: float, y_i: float, z_i: float)

The standard concave hyperbolic cylinder x-slope with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **alpha** (float) – The angle around x-axis
  * **beta** (float) – The angle around y-axis
  * **gamma** (float) – The angle around z-axis
  * **x_i** (float) – x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
  * **y_i** (float) – y-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the y-position of chief ray intersection in metrology coordinates
  * **z_i** (float) – z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
* **Returns:**
  **T** – The x-slope”
* **Return type:**
  numpy.ndarray

### xmf.layer_02_generation.generate_1d_height(standard_height_function: LambdaType, x1d: array, p: float, q: float, theta: float, x_i: float, z_i: float, beta: float, z1d_measured: array = None)

Geneate 1D height map with (`p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`)

* **Parameters:**
  * **standard_height_function** (function) – The standard height function
  * **x1d** (numpy.ndarray) – The 1D x coordinates
  * **p** (float) – The `p` value: the distance from the source to the chief ray intersection
  * **q** (float) – The `q` value: the distance from the chief ray intersection to the focus
  * **theta** (float) – The grazing angle
  * **alpha** (float) – The angle around x-axis
  * **beta** (float) – The angle around y-axis
  * **gamma** (float) – The angle around z-axis
  * **x_i** (float) – x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
  * **z_i** (float) – z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
  * **z1d_measured** (numpy.ndarray) – The measured height map
* **Returns:**
  **z1d** – The height map
* **Return type:**
  numpy.ndarray

### xmf.layer_02_generation.generate_1d_slope(standard_slope_function: LambdaType, x1d: array, p: float, q: float, theta: float, x_i: float, beta: float)

Generate 1D slope map with (`p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`)

* **Parameters:**
  * **standard_slope_function** (function) – The standard slope function
  * **x1d** (numpy.ndarray) – The 1D x coordinates
  * **p** (float) – The `p` value: the distance from the source to the chief ray intersection
  * **q** (float) – The `q` value: the distance from the chief ray intersection to the focus
  * **theta** (float) – The grazing angle
  * **alpha** (float) – The angle around x-axis
  * **beta** (float) – The angle around y-axis
  * **gamma** (float) – The angle around z-axis
  * **x_i** (float) – x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
  * **sx1d_measured** (numpy.ndarray) – The measured slope map
* **Returns:**
  **sx1d** – The slope map
* **Return type:**
  numpy.ndarray

### xmf.layer_02_generation.generate_2d_curved_surface_height(standard_height_function: LambdaType, x2d: ndarray, y2d: ndarray, p: float, q: float, theta: float, x_i: float, y_i: float, z_i: float, alpha: float, beta: float, gamma: float, z2d_measured: ndarray = None)

Geneate 2D curved surface height map with (`p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`)

* **Parameters:**
  * **standard_height_function** (function) – The standard height function
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **p** (float) – The `p` value: the distance from the source to the chief ray intersection
  * **q** (float) – The `q` value: the distance from the chief ray intersection to the focus
  * **theta** (float) – The grazing angle
  * **alpha** (float) – The angle around x-axis
  * **beta** (float) – The angle around y-axis
  * **gamma** (float) – The angle around z-axis
  * **x_i** (float) – x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
  * **y_i** (float) – y-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the y-position of chief ray intersection in metrology coordinates
  * **z_i** (float) – z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
  * **z2d_measured** (numpy.ndarray) – The measured height map
* **Returns:**
  **z2d** – The height map
* **Return type:**
  numpy.ndarray

### xmf.layer_02_generation.generate_2d_cylinder_height(standard_height_function: LambdaType, x2d: ndarray, y2d: ndarray, p: float, q: float, theta: float, x_i: float, z_i: float, alpha: float, beta: float, gamma: float, z2d_measured: ndarray = None)

Geneate 2D cylinder surface height map with (`p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`)

* **Parameters:**
  * **standard_height_function** (function) – The standard height function
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **p** (float) – The `p` value: the distance from the source to the chief ray intersection
  * **q** (float) – The `q` value: the distance from the chief ray intersection to the focus
  * **theta** (float) – The grazing angle
  * **alpha** (float) – The angle around x-axis
  * **beta** (float) – The angle around y-axis
  * **gamma** (float) – The angle around z-axis
  * **x_i** (float) – x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
  * **z_i** (float) – z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
  * **z2d_measured** (numpy.ndarray) – The measured height map
* **Returns:**
  **z2d** – The height map
* **Return type:**
  numpy.ndarray

### xmf.layer_02_generation.iter_generate_height(standard_height_function, x2d: ndarray, y2d: ndarray, p: float, q: float, theta: float, tf: ndarray, z2d_measured: ndarray = None, thr_rms_dxy: float = 1e-09)

The height generation with iterations(`p`, `q`, `theta`,  `thr_rms_dxy`)

* **Parameters:**
  * **standard_height_function** – The standard height function
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **p** (float) – The `p` value: the distance from the source to the chief ray intersection
  * **q** (float) – The `q` value: the distance from the chief ray intersection to the focus
  * **theta** (float) – The grazing angle
  * **tf** (numpy.ndarray) – The transformation matrix
  * **z2d_measured** (numpy.ndarray) – The measured height map
  * **thr_rms_dxy** (float) – The threshold of RMS
* **Returns:**
  **z2d** – The height map
* **Return type:**
  numpy.ndarray

## xmf.layer_03_optimization module

### xmf.layer_03_optimization.check_input_params(input_params_dict: dict, x: ndarray, y: ndarray, v: ndarray)

Function to check input parameters.

* **Parameters:**
  * **input_params_dict** (dict) – The `p`, `q`, `theta`, `x_i` (optional), `y_i` (optional),
    `z_i` (optional), `alpha` (optional), `beta` (optional) and
    `gamma` (optional) target parameters, suggested in unit of
    [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
  * **x** (numpy.ndarray) – The measured x-coordinate in in unit of [m] as a suggestion
  * **y** (numpy.ndarray) – The measured y-coordinate in in unit of [m] as a suggestion
  * **v** (numpy.ndarray) – The measured slope or height in [rad] or [m] as a suggestion
* **Returns:**
  **init_params** – The used initial parameters.
* **Return type:**
  numpy.ndarray

### xmf.layer_03_optimization.optimize_parameters(surface_generation_function: LambdaType, standard_surface_shape_function: LambdaType, x: ndarray, y: ndarray, v: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Basic function to provide a convenient way to optimize the surface parameters.

* **Parameters:**
  * **surface_generation_function** (function) – The function to generate surface (1D or 2D, slope or height)
  * **standard_surface_shape_function** (function) – The function handle for a standard surface shape
  * **x** (numpy.ndarray) – The measured x-coordinate in in unit of [m] as a suggestion
  * **y** (numpy.ndarray) – The measured y-coordinate in in unit of [m] as a suggestion
  * **v** (numpy.ndarray) – The measured slope or height in [rad] or [m] as a suggestion
  * **input_params_dict** (dict) – The `p`, `q`, `theta`, `x_i` (optional), `y_i` (optional),
    `z_i` (optional), `alpha` (optional), `beta` (optional) and
    `gamma` (optional) target parameters, suggested in unit of
    [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **v_res** (numpy.ndarray) – The residual (1D or 2D)
  * **v_fit** (numpy.ndarray) – The fitting result (1D or 2D)
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary
  * **init_params** (numpy.ndarray) – The used initial parameters.

### xmf.layer_03_optimization.optimize_parameters_with_opt(surface_generation_function: LambdaType, standard_surface_shape_function: LambdaType, x: ndarray, y: ndarray, v: ndarray, input_params_dict: dict, opt_dict: dict)

Basic function to provide a convenient way to optimize the surface parameters with optimization flag.

* **Parameters:**
  * **surface_generation_function** (function) – The function to generate surface (1D or 2D, slope or height)
  * **standard_surface_shape_function** (function) – The function handle for a standard surface shape
  * **x** (numpy.ndarray) – The measured x-coordinate in in unit of [m] as a suggestion
  * **y** (numpy.ndarray) – The measured y-coordinate in in unit of [m] as a suggestion
  * **v** (numpy.ndarray) – The measured slope or height in [rad] or [m] as a suggestion
  * **input_params_dict** (dict) – The `p`, `q`, `theta`, `x_i` (optional), `y_i` (optional),
    `z_i` (optional), `alpha` (optional), `beta` (optional) and
    `gamma` (optional) target parameters, suggested in unit of
    [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
  * **opt_dict** (dict) – The structure to set whether optimization is needed for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **v_res** (numpy.ndarray) – The residual (1D or 2D)
  * **v_fit** (numpy.ndarray) – The fitting result (1D or 2D)
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary
  * **init_params** (numpy.ndarray) – The used initial parameters.

### xmf.layer_03_optimization.optimize_parameters_with_tol(surface_generation_function: LambdaType, standard_surface_shape_function: LambdaType, x: ndarray, y: ndarray, v: ndarray, input_params_dict: dict, tol_dict: dict)

Basic function to provide a convenient way to optimize the surface parameters with tolerances.

* **Parameters:**
  * **surface_generation_function** (function) – The function to generate surface (1D or 2D, slope or height)
  * **standard_surface_shape_function** (function) – The function handle for a standard surface shape
  * **x** (numpy.ndarray) – The measured x-coordinate in in unit of [m] as a suggestion
  * **y** (numpy.ndarray) – The measured y-coordinate in in unit of [m] as a suggestion
  * **v** (numpy.ndarray) – The measured slope or height in [rad] or [m] as a suggestion
  * **input_params_dict** (dict) – The `p`, `q`, `theta`, `x_i` (optional), `y_i` (optional),
    `z_i` (optional), `alpha` (optional), `beta` (optional) and
    `gamma` (optional) target parameters, suggested in unit of
    [m] [m] [rad] [m] [m] [m] [rad] [rad] [rad]
  * **tol_dict** (dict) – The structure to set the tolerances for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **v_res** (numpy.ndarray) – The residual (1D or 2D)
  * **v_fit** (numpy.ndarray) – The fitting result (1D or 2D)
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary
  * **init_params** (numpy.ndarray) – The used initial parameters.

## xmf.layer_04_fit module

### xmf.layer_04_fit.fit_concave_ellipse_height(x1d: ndarray, z1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave ellipse parameters from a measured height profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **z1d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z1d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.layer_04_fit.fit_concave_ellipse_slope(x1d: ndarray, sx1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave ellipse parameters from a measured slope profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **sx1d** (numpy.ndarray) – The measured slope in the suggested unit of [m/m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **sx1d_fit** (numpy.ndarray) – The fitted slope
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.layer_04_fit.fit_concave_ellipsoid_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave ellipsoid parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **input_params_dict** (dict) – The input parameters dictionary containing `p`, `q`, `theta`, `x_i` (optional), and `y_i` (optional) in the suggested unit of [m] [m] [rad] [m]
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.layer_04_fit.fit_concave_elliptic_cylinder_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave elliptic cylinder parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.layer_04_fit.fit_concave_hyperbola_height(x1d: ndarray, z1d_measured: ndarray, input_params_dict: dict, opt_1d_cylinder_height: dict)

Fit the concave hyperbola parameters from a measured height profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **z1d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z1d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.layer_04_fit.fit_concave_hyperbola_slope(x1d: ndarray, sx1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave hyperbola parameters from a measured slope profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **sx1d** (numpy.ndarray) – The measured slope in the suggested unit of [m/m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **sx1d_fit** (numpy.ndarray) – The fitted slope
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.layer_04_fit.fit_concave_hyperbolic_cylinder_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave hyperbolic cylinder parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.layer_04_fit.fit_concave_hyperboloid_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave hyperboloid parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **input_params_dict** (numpy.ndarray) – The the `p`, `q`, `theta`, `x_i` (optional), and `y_i` (optional) in the suggested unit of [m] [m] [rad] [m]
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.layer_04_fit.fit_convex_ellipse_height(x1d: ndarray, z1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex ellipse parameters from a measured height profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **z1d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z1d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.layer_04_fit.fit_convex_ellipse_slope(x1d: ndarray, sx1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex ellipse parameters from a measured slope profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **sx1d** (numpy.ndarray) – The measured slope in the suggested unit of [m/m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **sx1d_fit** (numpy.ndarray) – The fitted slope
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.layer_04_fit.fit_convex_ellipsoid_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex ellipsoid parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **input_params_dict** (numpy.ndarray) – The the `p`, `q`, `theta`, `x_i` (optional), and `y_i` (optional) in the suggested unit of [m] [m] [rad] [m]
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.layer_04_fit.fit_convex_elliptic_cylinder_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex elliptic cylinder parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.layer_04_fit.fit_convex_hyperbola_height(x1d: ndarray, z1d_measured: ndarray, input_params_dict: dict, opt_1d_cylinder_height: dict)

Fit the convex hyperbola parameters from a measured height profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **z1d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z1d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.layer_04_fit.fit_convex_hyperbola_slope(x1d: ndarray, sx1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex hyperbola parameters from a measured slope profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **sx1d** (numpy.ndarray) – The measured slope in the suggested unit of [m/m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **sx1d_fit** (numpy.ndarray) – The fitted slope
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.layer_04_fit.fit_convex_hyperbolic_cylinder_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex hyperbolic cylinder parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.layer_04_fit.fit_convex_hyperboloid_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex hyperboloid parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **input_params_dict** (numpy.ndarray) – The the `p`, `q`, `theta`, `x_i` (optional), and `y_i` (optional) in the suggested unit of [m] [m] [rad] [m]
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

## Module contents

### xmf.fig_compare_1d_height(x1d, z1d_generation, z1d_standard, str_title)

Compare two 1D height data sets and plot the difference

* **Parameters:**
  * **x1d** (numpy.ndarray) – 1D array of x-coordinates
  * **z1d_generation** (numpy.ndarray) – 1D array of height data from generation
  * **z1d_standard** (numpy.ndarray) – 1D array of height data from standard
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_compare_1d_slope(x1d, sx1d_generation, sx1d_standard, str_title)

Compare two 1D slope data sets and plot the difference

* **Parameters:**
  * **x1d** (numpy.ndarray) – 1D array of x-coordinates
  * **sx1d_generation** (numpy.ndarray) – 1D array of slope data from generation
  * **sx1d_standard** (numpy.ndarray) – 1D array of slope data from standard
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show_1d_fitting_height(x1d, z1d_measured, z1d_fit, z1d_res, target_params_dict, opt_params_dict, opt_params_ci_dict, str_title)

Show a 1D fitting plot with measured data, fitted data, residuals, target parameters, and optimized parameters

* **Parameters:**
  * **x1d** (numpy.ndarray) – 1D array of x-coordinates
  * **z1d_measured** (numpy.ndarray) – 1D array of measured z-values
  * **z1d_fit** (numpy.ndarray) – 1D array of fitted z-values
  * **z1d_res** (numpy.ndarray) – 1D array of residuals
  * **target_params_dict** (dict) – Dictionary of target parameters
  * **opt_params_dict** (dict) – Dictionary of optimized parameters
  * **opt_params_ci_dict** (dict) – Dictionary of optimized parameters confidence intervals
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show_1d_fitting_slope(x1d, sx1d_measured, sx1d_fit, sx1d_res, target_params_dict, opt_params_dict, opt_params_ci_dict, str_title)

Show a 1D fitting plot with measured slopes, fitted slopes, residuals, target parameters, and optimized parameters

* **Parameters:**
  * **x1d** (numpy.ndarray) – 1D array of x-coordinates
  * **sx1d_measured** (numpy.ndarray) – 1D array of measured slopes
  * **sx1d_fit** (numpy.ndarray) – 1D array of fitted slopes
  * **sx1d_res** (numpy.ndarray) – 1D array of residuals
  * **target_params_dict** (dict) – Dictionary of target parameters
  * **opt_params_dict** (dict) – Dictionary of optimized parameters
  * **opt_params_ci_dict** (dict) – Dictionary of optimized parameters confidence intervals
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show_1d_height(x1d, z1d_quad_sln, z1d_expression, str_title)

Show a 1D plot of height data from quadratic equation solution and expression

* **Parameters:**
  * **x1d** (numpy.ndarray) – 1D array of x-coordinates
  * **z1d_quad_sln** (numpy.ndarray) – 1D array of height data from quadratic equation solution
  * **z1d_expression** (numpy.ndarray) – 1D array of height data from expression
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show_1d_slope(x1d, sx1d, str_title)

### xmf.fig_show_2d_fitting_map(x2d, y2d, z2d_measured, z2d_fit, z2d_res, target_params_dict, opt_params_dict, opt_params_ci_dict, str_title)

Show a 2D fitting map with colorbar, target parameters, fitted parameters, and residuals

* **Parameters:**
  * **x2d** (numpy.ndarray) – 2D array of x-coordinates
  * **y2d** (numpy.ndarray) – 2D array of y-coordinates
  * **z2d_measured** (numpy.ndarray) – 2D array of measured z-values
  * **z2d_fit** (numpy.ndarray) – 2D array of fitted z-values
  * **z2d_res** (numpy.ndarray) – 2D array of residuals
  * **target_params_dict** (dict) – Dictionary of target parameters
  * **opt_params_dict** (dict) – Dictionary of optimized parameters
  * **opt_params_ci_dict** (dict) – Dictionary of optimized parameters confidence intervals
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fig_show_2d_map(x2d, y2d, z2d_quad_sln, z2d_expression, str_title)

Show a 2D map of height data with colorbar

* **Parameters:**
  * **x2d** (numpy.ndarray) – 2D array of x-coordinates
  * **y2d** (numpy.ndarray) – 2D array of y-coordinates
  * **z2d_quad_sln** (numpy.ndarray) – 2D array of height data from quadratic equation solution
  * **z2d_expression** (numpy.ndarray) – 2D array of height data from expression
  * **str_title** (str) – Title of the plot
* **Return type:**
  None

### xmf.fit_concave_ellipse_height(x1d: ndarray, z1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave ellipse parameters from a measured height profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **z1d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z1d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_concave_ellipse_slope(x1d: ndarray, sx1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave ellipse parameters from a measured slope profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **sx1d** (numpy.ndarray) – The measured slope in the suggested unit of [m/m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **sx1d_fit** (numpy.ndarray) – The fitted slope
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_concave_ellipsoid_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave ellipsoid parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **input_params_dict** (dict) – The input parameters dictionary containing `p`, `q`, `theta`, `x_i` (optional), and `y_i` (optional) in the suggested unit of [m] [m] [rad] [m]
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_concave_elliptic_cylinder_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave elliptic cylinder parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_concave_hyperbola_height(x1d: ndarray, z1d_measured: ndarray, input_params_dict: dict, opt_1d_cylinder_height: dict)

Fit the concave hyperbola parameters from a measured height profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **z1d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z1d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_concave_hyperbola_slope(x1d: ndarray, sx1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave hyperbola parameters from a measured slope profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **sx1d** (numpy.ndarray) – The measured slope in the suggested unit of [m/m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **sx1d_fit** (numpy.ndarray) – The fitted slope
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_concave_hyperbolic_cylinder_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave hyperbolic cylinder parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_concave_hyperboloid_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the concave hyperboloid parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **input_params_dict** (numpy.ndarray) – The the `p`, `q`, `theta`, `x_i` (optional), and `y_i` (optional) in the suggested unit of [m] [m] [rad] [m]
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_convex_ellipse_height(x1d: ndarray, z1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex ellipse parameters from a measured height profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **z1d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z1d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_convex_ellipse_slope(x1d: ndarray, sx1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex ellipse parameters from a measured slope profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **sx1d** (numpy.ndarray) – The measured slope in the suggested unit of [m/m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **sx1d_fit** (numpy.ndarray) – The fitted slope
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_convex_ellipsoid_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex ellipsoid parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **input_params_dict** (numpy.ndarray) – The the `p`, `q`, `theta`, `x_i` (optional), and `y_i` (optional) in the suggested unit of [m] [m] [rad] [m]
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_convex_elliptic_cylinder_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex elliptic cylinder parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_convex_hyperbola_height(x1d: ndarray, z1d_measured: ndarray, input_params_dict: dict, opt_1d_cylinder_height: dict)

Fit the convex hyperbola parameters from a measured height profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **z1d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z1d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_convex_hyperbola_slope(x1d: ndarray, sx1d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex hyperbola parameters from a measured slope profile.

* **Parameters:**
  * **x1d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **sx1d** (numpy.ndarray) – The measured slope in the suggested unit of [m/m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z1d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **sx1d_fit** (numpy.ndarray) – The fitted slope
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_convex_hyperbolic_cylinder_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex hyperbolic cylinder parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.fit_convex_hyperboloid_height(x2d: ndarray, y2d: ndarray, z2d: ndarray, input_params_dict: dict, opt_or_tol_dict: dict)

Fit the convex hyperboloid parameters from a measured height map.

* **Parameters:**
  * **x2d** (numpy.ndarray) – The x coordinate in the suggested unit of [m]
  * **y2d** (numpy.ndarray) – The y coordinate in the suggested unit of [m]
  * **z2d** (numpy.ndarray) – The z coordinate in the suggested unit of [m]
  * **input_params_dict** (numpy.ndarray) – The the `p`, `q`, `theta`, `x_i` (optional), and `y_i` (optional) in the suggested unit of [m] [m] [rad] [m]
  * **opt_or_tol_dict** (dict) – The structure to set whether optimization flag or tolerance for
    `p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`.
* **Returns:**
  * **z2d_residual** (numpy.ndarray) – The height residual after the best fit.
  * **z2d_fit** (numpy.ndarray) – The fitted height
  * **opt_params_dict** (dict) – The optimized parameters in dictionary
  * **opt_params_ci_dict** (dict) – The confidence intervals of the optimized parameters in dictionary

### xmf.generate_1d_height(standard_height_function: LambdaType, x1d: array, p: float, q: float, theta: float, x_i: float, z_i: float, beta: float, z1d_measured: array = None)

Geneate 1D height map with (`p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`)

* **Parameters:**
  * **standard_height_function** (function) – The standard height function
  * **x1d** (numpy.ndarray) – The 1D x coordinates
  * **p** (float) – The `p` value: the distance from the source to the chief ray intersection
  * **q** (float) – The `q` value: the distance from the chief ray intersection to the focus
  * **theta** (float) – The grazing angle
  * **alpha** (float) – The angle around x-axis
  * **beta** (float) – The angle around y-axis
  * **gamma** (float) – The angle around z-axis
  * **x_i** (float) – x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
  * **z_i** (float) – z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
  * **z1d_measured** (numpy.ndarray) – The measured height map
* **Returns:**
  **z1d** – The height map
* **Return type:**
  numpy.ndarray

### xmf.generate_1d_slope(standard_slope_function: LambdaType, x1d: array, p: float, q: float, theta: float, x_i: float, beta: float)

Generate 1D slope map with (`p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`)

* **Parameters:**
  * **standard_slope_function** (function) – The standard slope function
  * **x1d** (numpy.ndarray) – The 1D x coordinates
  * **p** (float) – The `p` value: the distance from the source to the chief ray intersection
  * **q** (float) – The `q` value: the distance from the chief ray intersection to the focus
  * **theta** (float) – The grazing angle
  * **alpha** (float) – The angle around x-axis
  * **beta** (float) – The angle around y-axis
  * **gamma** (float) – The angle around z-axis
  * **x_i** (float) – x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
  * **sx1d_measured** (numpy.ndarray) – The measured slope map
* **Returns:**
  **sx1d** – The slope map
* **Return type:**
  numpy.ndarray

### xmf.generate_2d_curved_surface_height(standard_height_function: LambdaType, x2d: ndarray, y2d: ndarray, p: float, q: float, theta: float, x_i: float, y_i: float, z_i: float, alpha: float, beta: float, gamma: float, z2d_measured: ndarray = None)

Geneate 2D curved surface height map with (`p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`)

* **Parameters:**
  * **standard_height_function** (function) – The standard height function
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **p** (float) – The `p` value: the distance from the source to the chief ray intersection
  * **q** (float) – The `q` value: the distance from the chief ray intersection to the focus
  * **theta** (float) – The grazing angle
  * **alpha** (float) – The angle around x-axis
  * **beta** (float) – The angle around y-axis
  * **gamma** (float) – The angle around z-axis
  * **x_i** (float) – x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
  * **y_i** (float) – y-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the y-position of chief ray intersection in metrology coordinates
  * **z_i** (float) – z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
  * **z2d_measured** (numpy.ndarray) – The measured height map
* **Returns:**
  **z2d** – The height map
* **Return type:**
  numpy.ndarray

### xmf.generate_2d_cylinder_height(standard_height_function: LambdaType, x2d: ndarray, y2d: ndarray, p: float, q: float, theta: float, x_i: float, z_i: float, alpha: float, beta: float, gamma: float, z2d_measured: ndarray = None)

Geneate 2D cylinder surface height map with (`p`, `q`, `theta`, `x_i`, `y_i`, `z_i`, `alpha`, `beta`, `gamma`)

* **Parameters:**
  * **standard_height_function** (function) – The standard height function
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **p** (float) – The `p` value: the distance from the source to the chief ray intersection
  * **q** (float) – The `q` value: the distance from the chief ray intersection to the focus
  * **theta** (float) – The grazing angle
  * **alpha** (float) – The angle around x-axis
  * **beta** (float) – The angle around y-axis
  * **gamma** (float) – The angle around z-axis
  * **x_i** (float) – x-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the x-position of chief ray intersection in metrology coordinates
  * **z_i** (float) – z-translation in the conversion from standard mirror coordinates to metrology coordinates, also revealing the z-position of chief ray intersection in metrology coordinates
  * **z2d_measured** (numpy.ndarray) – The measured height map
* **Returns:**
  **z2d** – The height map
* **Return type:**
  numpy.ndarray

### xmf.standard_concave_ellipsoid_height(x2d: ndarray, y2d: ndarray, abs_p: float, abs_q: float, theta: float, return_z2d_expression_as_extra: bool = False)

The standard 2D concave ellipsoid height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z2d_expression_as_extra** (bool) – If True, return the z2d_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.standard_concave_elliptic_cylinder_height(x: ndarray, abs_p: float, abs_q: float, theta: float, return_z_expression_as_extra: bool = False)

The standard convex elliptic cylinder height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z_expression_as_extra** (bool) – If True, return the z_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.standard_concave_elliptic_cylinder_xslope(x: ndarray, abs_p: float, abs_q: float, theta: float)

The standard concave elliptic cylinder x-slope with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
* **Returns:**
  **sx** – The x-slope
* **Return type:**
  numpy.ndarray

### xmf.standard_concave_hyperbolic_cylinder_height(x: ndarray, abs_p: float, abs_q: float, theta: float, return_z_expression_as_extra: bool = False)

The standard 2D concave hyperbolic height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The 2D x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z_expression_as_extra** (bool) – If True, return the z_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.standard_concave_hyperbolic_cylinder_xslope(x: ndarray, abs_p: float, abs_q: float, theta: float)

The standard concave hyperbolic cylinder x-slope with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
* **Returns:**
  **sx** – The x-slope
* **Return type:**
  numpy.ndarray

### xmf.standard_concave_hyperboloid_height(x2d: ndarray, y2d: ndarray, abs_p: float, abs_q: float, theta: float, return_z2d_expression_as_extra: bool = False)

The standard 2D concave hyperboloid height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z2d_expression_as_extra** (bool) – If True, return the z2d_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.standard_convex_ellipsoid_height(x2d: ndarray, y2d: ndarray, abs_p: float, abs_q: float, theta: float, return_z2d_expression_as_extra: bool = False)

The standard 2D convex ellipsoid height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z2d_expression_as_extra** (bool) – If True, return the z2d_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.standard_convex_elliptic_cylinder_height(x: ndarray, abs_p: float, abs_q: float, theta: float, return_z_expression_as_extra: bool = False)

The standard convex elliptic cylinder height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z_expression_as_extra** (bool) – If True, return the z_expression as well
* **Returns:**
  **z** – The height
* **Return type:**
  numpy.ndarray

### xmf.standard_convex_elliptic_cylinder_xslope(x: ndarray, abs_p: float, abs_q: float, theta: float)

The standard convex elliptic cylinder x-slope with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
* **Returns:**
  **sx** – The x-slope
* **Return type:**
  numpy.ndarray

### xmf.standard_convex_hyperbolic_cylinder_height(x: ndarray, abs_p: float, abs_q: float, theta: float, return_z_expression_as_extra: bool = False)

The standard 2D convex hyperbolic height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The 2D x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z_expression_as_extra** (bool) – If True, return the z_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray

### xmf.standard_convex_hyperbolic_cylinder_xslope(x: ndarray, abs_p: float, abs_q: float, theta: float)

The standard convex hyperbolic cylinder x-slope with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x** (numpy.ndarray) – The x coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
* **Returns:**
  **sx** – The x-slope
* **Return type:**
  numpy.ndarray

### xmf.standard_convex_hyperboloid_height(x2d: ndarray, y2d: ndarray, abs_p: float, abs_q: float, theta: float, return_z2d_expression_as_extra: bool = False)

The standard 2D convex hyperboloid height with (`abs_p`, `abs_q`, `theta`)

* **Parameters:**
  * **x2d** (numpy.ndarray) – The 2D x coordinates
  * **y2d** (numpy.ndarray) – The 2D y coordinates
  * **abs_p** (float) – The `abs_p` value: the absolute value of the distance between the source and the chief ray intersection
  * **abs_q** (float) – The `abs_q` value: the absolute value of the distance between the chief ray intersection and the focus
  * **theta** (float) – The grazing angle
  * **return_z2d_expression_as_extra** (bool) – If True, return the z2d_expression as well
* **Returns:**
  **z2d** – The 2D height map
* **Return type:**
  numpy.ndarray
