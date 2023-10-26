import pandas as pd
import statsmodels.api as sm
#GY7EJG

class LinearRegressionSM:
    def __init__(self, left_hand_side, right_hand_side):
        self.left_hand_side = left_hand_side[['Excess Return']]
        self.right_hand_side = right_hand_side[['Mkt-RF', 'SMB', 'HML']]
        self._model = None


#8

    def fit(self):

        x = sm.add_constant(self.right_hand_side)
        y = self.left_hand_side

        self._model = sm.OLS(y, x).fit()

#9
    def get_params(self):

        return pd.Series(self._model.params, name='Beta coefficients')

#10
    def get_pvalues(self):

        return pd.Series(self._model.pvalues, name='P-values for the corresponding coefficients')



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