    import numpy as np
    import pandas as pd
    from scipy.stats import t, f

    class LinearRegressionGLS:
        def __init__(self, left_hand_side, right_hand_side):
            self.left_hand_side = left_hand_side
            self.right_hand_side = right_hand_side
            self._model = None

        def fit(self):
            # Feasible GLS becslés
            X_ols = np.column_stack((np.ones(len(self.right_hand_side)), self.right_hand_side))
            y_ols = self.left_hand_side
            beta_ols = np.linalg.inv(X_ols.T @ X_ols) @ X_ols.T @ y_ols

            # Hibatagok számolása
            residuals = y_ols - X_ols @ beta_ols

            # Hibatagok négyzete
            residuals_squared = residuals ** 2

            # Új modell becslése
            X_gls = np.column_stack(
                (np.ones(len(self.right_hand_side)), np.log(residuals_squared), self.right_hand_side))
            y_gls = np.log(self.left_hand_side)

            # 5.) Számold ki a becsült értékeket (logaritmikus négyzetes hibákat) és vedd a gyöküket (np.sqrt).
            beta_gls = np.linalg.inv(X_gls.T @ weights_matrix_inverse @ X_gls) @ X_gls.T @ weights_matrix_inverse @ y_gls
            beta_gls = np.sqrt(beta_gls)

            # 6.) A kapott vektornak vedd elemenként az inverzét és helyezd el egy diagonális mátrix főátlójában őket (np.diag).
            weights_matrix_inverse = np.diag(1 / beta_gls)

            # GLS regresszió paraméterei
            beta_gls = np.linalg.inv(X_gls.T @ weights_matrix_inverse @ X_gls) @ X_gls.T @ weights_matrix_inverse @ y_gls

            self._model = {'beta_gls': beta_gls, 'weights_matrix_inverse': weights_matrix_inverse}

        def get_params(self):
            beta_gls = self._model['beta_gls']
            return pd.Series(beta_gls, name='GLS Coefficients')

        def get_pvalues(self):
            X_gls = np.column_stack((np.ones(len(self.right_hand_side)), np.log(self._model['residuals_squared']),self.right_hand_side))
            y_gls = np.log(self.left_hand_side)
            n, k = X_gls.shape
            beta_gls = self._model['beta_gls']
            weights_matrix = np.linalg.inv(X_gls.T @ X_gls)
            residuals = y_gls - X_gls @ beta_gls
            residuals_variance = np.diagonal(residuals @ residuals / n)
            standard_errors = np.sqrt(residuals_variance * np.diagonal(weights_matrix))
            t_statistics = beta_gls / standard_errors
            df = n - k
            p_values = [2 * (1 - t.cdf(abs(t_stat), df)) for t_stat in t_statistics]
            p_values = pd.Series(p_values, name="P-values for corresponding coefficients")
            return p_values

        def get_wald_test_result(self, R):
            X_gls = np.column_stack((np.ones(len(self.right_hand_side)), np.log(self._model['residuals_squared']),self.right_hand_side))
            y_gls = np.log(self.left_hand_side)
            beta_gls = self._model['beta_gls']
            residuals = y_gls - X_gls @ beta_gls
            r_matrix = np.array(R)
            r = r_matrix @ beta_gls
            n = len(self.left_hand_side)
            m, k = r_matrix.shape
            sigma_squared = np.sum(residuals ** 2) / (n - k)
            H = r_matrix @ np.linalg.inv(X_gls.T @ X_gls) @ r_matrix.T
            wald = (r.T @ np.linalg.inv(H) @ r) / (m * sigma_squared)
            p_value = 1 - f.cdf(wald, dfn=m, dfd=n - k)
            return f'Wald: {wald:.3f}, p-value: {p_value:.3f}'

        def get_model_goodness_values(self):
            X_gls = np.column_stack((np.ones(len(self.right_hand_side)), np.log(self._model['residuals_squared']),self.right_hand_side))
            y_gls = np.log(self.left_hand_side)
            n, k = X_gls.shape
            beta_gls = self._model['beta_gls']
            y_pred = X_gls @ beta_gls
            ssr = np.sum((y_pred - np.mean(y_gls)) ** 2)
            sst = np.sum((y_gls - np.mean(y_gls)) ** 2)
            centered_r_squared = ssr / sst
            adjusted_r_squared = 1 - (1 - centered_r_squared) * (n - 1) / (n - k)
            result = f"Centered R-squared: {centered_r_squared:.3f}, Adjusted R-squared: {adjusted_r_squared:.3f}"
            return result