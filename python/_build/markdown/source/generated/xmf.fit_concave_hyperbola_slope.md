# xmf.fit_concave_hyperbola_slope

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
