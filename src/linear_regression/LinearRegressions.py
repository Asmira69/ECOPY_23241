#GY7EJG
from pathlib import Path
import pandas as pd
import numpy as np
from scipy.stats import f, t
import typing


datalib = Path.cwd().parent.joinpath('data')

sp500_df = pd.read_parquet(datalib.joinpath('sp500.parquet'), engine='fastparquet')
ff_factors_df = pd.read_parquet(datalib.joinpath('ff_factors.parquet'), engine='fastparquet')
merged_df = pd.merge(sp500_df, ff_factors_df, on='Date', how='left')
merged_df['Excess Return'] = merged_df['Monthly Returns'] - merged_df['RF']
merged_df = merged_df.sort_values(by=['Symbol', 'Date'])
merged_df['ex_ret_1'] = merged_df.groupby('Symbol')['Excess Return'].shift(-1)
merged_df = merged_df.dropna(subset=['ex_ret_1'])
merged_df = merged_df.dropna(subset=['HML'])

amazon_df = merged_df[merged_df['Symbol'] == 'AMZN'].copy()
amazon_df = amazon_df.drop(columns=['Symbol'])
class LinearRegressionNP:
    def __init__(self, left_hand_side, right_hand_side):
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side
        self.coefficients = None

    def fit(self):
        X = np.column_stack((np.ones(len(self.right_hand_side)), self.right_hand_side[['Mkt-RF', 'SMB', 'HML']]))
        y = self.left_hand_side['Excess Return']

        # OLS becslés
        self.coefficients = np.linalg.inv(X.T @ X) @ X.T @ y

    def get_params(self):
        if self.coefficients is None:
            raise ValueError("The model has not been fitted yet. Call the fit method first.")

        beta_params = pd.Series(self.coefficients, index=['Intercept', 'Mkt-RF', 'SMB', 'HML'],
                                name='Beta coefficients')
        return beta_params

    def get_pvalues(self):
        if self.coefficients is None:
            raise ValueError("The model has not been fitted yet. Call the fit method first.")

        X = np.column_stack((np.ones(len(self.right_hand_side)), self.right_hand_side[['Mkt-RF', 'SMB', 'HML']]))
        y = self.left_hand_side['Excess Return']

        residuals = y - X @ self.coefficients
        dof = len(y) - len(self.coefficients)
        standard_errors = np.sqrt(np.sum(residuals ** 2) / dof)

        t_stats = self.coefficients / standard_errors
        p_values = pd.Series(min(t.sf(np.abs(t_stats), dof), 1 - t.sf(np.abs(t_stats), dof)) * 2,
                             index=['Intercept', 'Mkt-RF', 'SMB', 'HML'],
                             name='P-values for the corresponding coefficients')

        return p_values

    def get_wald_test_result(self, R):
        if self.coefficients is None:
            raise ValueError("The model has not been fitted yet. Call the fit method first.")

        X = np.column_stack((np.ones(len(self.right_hand_side)), self.right_hand_side[['Mkt-RF', 'SMB', 'HML']]))
        y = self.left_hand_side['Excess Return']

        residuals = y - X @ self.coefficients
        dof = len(y) - len(self.coefficients)
        SSR_restricted = np.sum(residuals ** 2)

        R = np.array(R)
        q, k = R.shape

        F_statistic = ((SSR_restricted - np.sum(residuals ** 2)) / q) / (np.sum(residuals ** 2) / dof)

        p_value = 1 - f.cdf(F_statistic, q, dof)

        result_string = f"Wald: {F_statistic:.3f}, p-value: {p_value:.3f}"
        return result_string

    def get_model_goodness_values(self):
        if self.coefficients is None:
            raise ValueError("The model has not been fitted yet. Call the fit method first.")

        X = np.column_stack((np.ones(len(self.right_hand_side)), self.right_hand_side[['Mkt-RF', 'SMB', 'HML']]))
        y = self.left_hand_side['Excess Return']

        y_mean = np.mean(y)
        y_pred = X @ self.coefficients
        SSR = np.sum((y_pred - y_mean) ** 2)
        SSE = np.sum((y - y_pred) ** 2)
        SST = SSR + SSE

        centered_r_squared = SSR / SST

        n, k = X.shape
        dof = n - k
        adjusted_r_squared = 1 - (SSE / dof) / (SST / (n - 1))

        result_string = f"Centered R-squared: {centered_r_squared:.3f}, Adjusted R-squared: {adjusted_r_squared:.3f}"
        return result_string