from pathlib import Path
import pandas as pd
import statsmodels.api as sm


#1
datalib = Path.cwd().parent.joinpath('data')
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
    def __init__(self, left_hand_side, right_hand_side):
        self.left_hand_side = left_hand_side[['Excess Return']]
        self.right_hand_side = right_hand_side[['Mkt-RF', 'SMB', 'HML']]
        self._model = None


#8

    def fit(self):
        # Konstans hozzáadása a független változókhoz
        X = sm.add_constant(self.right_hand_side)
        y = self.left_hand_side
        # Lineáris regresszió illesztése
        self._model = sm.OLS(y, X).fit()

#9
    def get_params(self):

        return pd.Series(self._model.params, name='Beta coefficients')

#10
    def get_pvalues(self):
        return pd.Series(self._model.pvalues, name='P-values for the corresponding coefficients')

#11
   def get_wald_test_result(self, restr_matrix: np.ndarray):
        wald_test = self._model.wald_test(restr_matrix)
        fvalue = round(wald_test.statistic, 3)
        pvalue = round(wald_test.pvalue, 3)
        return f"F-value: {fvalue}, p-value: {pvalue}"

#12
def get_model_goodness_values(self) -> str:
    ars: float = round(self._model.rsquared_adj, 3)
    ak: float = round(self._model.aic, 3)
    by: float = round(self._model.bic, 3)
    return f"Adjusted R-squared: {ars}, Akaike IC: {ak}, Bayes IC: {by}"