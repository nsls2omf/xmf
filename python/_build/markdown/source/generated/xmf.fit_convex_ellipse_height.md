# xmf.fit_convex_ellipse_height

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
