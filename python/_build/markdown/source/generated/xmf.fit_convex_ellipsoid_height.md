# xmf.fit_convex_ellipsoid_height

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
