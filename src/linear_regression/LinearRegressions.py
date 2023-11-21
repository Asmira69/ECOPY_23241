import pandas as pd
import numpy as np
from scipy.stats import t, f

class LinearRegressionGLS:
    def __init__(self, left_hand_side, right_hand_side):
        self.left_hand_side = left_hand_side.values
        self.right_hand_side = right_hand_side.values

    def fit(self):
        self.X = np.column_stack((np.ones(len(self.right_hand_side)), self.right_hand_side))
        self.Y = self.left_hand_side
        beta_ols = np.linalg.inv(self.X.T @ self.X) @ self.X.T @self.Y
        resid_ols = self.Y - self.X @ beta_ols
        log_resid_ols = np.log(resid_ols ** 2)
        beta_omega = np.linalg.inv(self.X.T @ self.X) @ self.X.T @ log_resid_ols
        V_inv_diag = 1 / np.sqrt(np.exp(self.X @ beta_omega))
        self.V_inv = np.diag(V_inv_diag)
        beta_gls = np.linalg.inv(self.X.T @ self.V_inv @ self.X) @ self.X.T @ self.V_inv @ self.Y
        self.beta_params = beta_gls

    def get_params(self):
        return pd.Series(self.beta_params, name='Beta_coeffs')

    def get_pvalues(self):
        self.fit()
        dof = len(self.Y) - self.X.shape[1]
        residuals = self.Y - self.X @ self.beta_params
        residual_variance = (residuals @ residuals) / dof
        t_stat = self.beta_params / np.sqrt(np.diag(residual_variance*np.linalg.inv(self.X.T @ self.V_inv @ self.X)))
        p_values = pd.Series([min(value, 1 - value) * 2 for value in t.cdf(-np.abs(t_stat), df=dof)],name='P-values for the corresponding coefficients')
        return p_values

    def get_wald_test_result(self, restrictions):
        self.fit()
        r_matrix = np.array(restrictions)
        r_vector = r_matrix @ self.beta_params
        n = len(self.Y)
        m, k = r_matrix.shape
        residuals = self.Y - self.X @ self.beta_params
        residual_variance = (residuals @ residuals) / (n - k)
        H_matrix = r_matrix @ np.linalg.inv(self.X.T @ self.V_inv @ self.X) @ r_matrix.T
        wald_value = (r_vector.T @ np.linalg.inv(H_matrix) @ r_vector) / (m * residual_variance)
        p_value = 1 - f.cdf(wald_value, dfn=m, dfd=n - k)
        return f'Wald: {wald_value:.3f}, p-value: {p_value:.3f}'

    def get_model_goodness_values(self):
        self.fit()
        total_sum_of_squares = self.Y.T @ self.V_inv @ self.Y
        residual_sum_of_squares = self.Y.T @ self.V_inv @ self.X @ np.linalg.inv(
            self.X.T @ self.V_inv @ self.X) @ self.X.T @ self.V_inv @ self.Y
        centered_r_squared = 1 - (residual_sum_of_squares / total_sum_of_squares)
        adjusted_r_squared = 1 - (residual_sum_of_squares / (len(self.Y) - self.X.shape[1])) * (
                len(self.Y) - 1) / total_sum_of_squares
        return f"Centered R-squared: {centered_r_squared:.3f}, Adjusted R-squared: {adjusted_r_squared:.3f}"