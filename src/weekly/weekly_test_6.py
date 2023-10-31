from pathlib import Path
import pandas as pd
import statsmodels.api as sm
import pathlib
import typing

#GY7EJG

#1
datalib = Path.cwd().parent.joinpath('data')

#1
    df = pd.read_parquet(datalib.joinpath('sp500.parquet'), engine='fastparquet')

#2
    df_ff_factors = pd.read_parquet(datalib.joinpath('ff_factors.parquet'), engine='fastparquet')

#3
    merged_df = pd.merge(df, df_ff_factors, on='Date', how='left')

#4
    merged_df['Excess Return'] = merged_df['Monthly Returns'] - merged_df['RF']

#5
# Sorok rendezése dátum szerint
    merged_df = merged_df.sort_values(by='Date')

# 'ex_ret_1' oszlop létrehozása
    merged_df['ex_ret_1'] = merged_df.groupby('Symbol')['Excess Return'].shift(-1)

#6
# 'ex_ret_1' oszlopban hiányzó sorok törlése
    merged_df = merged_df.dropna(subset=['ex_ret_1'])

# 'HML' oszlopban hiányzó sorok törlése
    merged_df = merged_df.dropna(subset=['HML'])

#7
# Amazon részvényhez tartozó sorok kiválasztása
    amazon_df = merged_df[merged_df['Symbol'] == 'AMZN'].copy()

# 'Symbol' oszlop eltávolítása
    amazon_df = amazon_df.drop(columns=['Symbol'])


class LinearRegressionSM:
    def __init__(self, left_hand_side: pd.DataFrame, right_hand_side: pd.DataFrame):
        self.left_hand_side = left_hand_side
        self.right_hand_side = right_hand_side

    def fit(self):
        X = sm.add_constant(self.right_hand_side)
        y = self.left_hand_side
        model = sm.OLS(y, X).fit()
        self._model = model

    def get_params(self):
        beta_params = self._model.params
        beta_params.name = 'Beta coefficients'
        return beta_params

    def get_pvalues(self):
        pvalues_df = pd.Series(self._model.pvalues, name="P-values for the corresponding coefficients")
        return pvalues_df

    def get_wald_test_result(self, restriction_matrix):
        wald_test = self._model.wald_test(restriction_matrix, scalar=True)
        fvalue = round(wald_test.fvalue, 2)
        pvalue = round(wald_test.pvalue, 3)
        result_string = f"F-value: {fvalue}, p-value: {pvalue}"
        return result_string
    def get_model_goodness_values(self):
        adjusted_r_squared = self._model.rsquared_adj
        aic = self._model.aic
        bic = self._model.bic

        result_string = f"Adjusted R-squared: {adjusted_r_squared:.3f}, Akaike IC: {aic:.2e}, Bayes IC: {bic:.2e}"
        return result_string
