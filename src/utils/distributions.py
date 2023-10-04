#gy7ejg
# week3
#1
class LogisticDistribution:
    def __init__(self, rand: np.random.Generator, loc: float, scale: float):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def generate_random(self, size: int = 1) -> List[float]:
        return self.rand.logistic(self.loc, self.scale, size).tolist()

#2
    def pdf(self, x: float) -> float:

        exp_term = math.exp(-(x - self.loc) / self.scale)
        return exp_term / (self.scale * (1 + exp_term)**2)
#3
    def cdf(self, x: float) -> float:

        scaled_x = (x - self.loc) / self.scale
        return 1 / (1 + exp(-scaled_x))

#4
    def ppf(self, p: float) -> float:

        if 0 < p < 1:
            scaled_p = log(p / (1 - p))
            return self.loc + self.scale * scaled_p
        else:
            raise ValueError("A valószínűség értéke 0 és 1 között kell legyen.")
#5
    def gen_rand(self) -> float:

        u = random()
        return self.loc + self.scale * log(u / (1 - u))
#6
    def mean(self) -> float:

        if self.scale == 0:
            raise Exception("Moment undefined")

        return self.loc + self.scale * 0.57721566490153286060  # Euler-Mascheroni konstans
#7
    def variance(self) -> float:

        if self.scale == 0:
            raise Exception("Moment undefined")

        scale_pi_square = self.scale * pi
        return scale_pi_square ** 2 / 3
#8
    def skewness(self) -> float:

        if self.scale == 0:
            raise Exception("Moment undefined")

        scale_sqrt_3 = self.scale * sqrt(3)
        return 0
#9
    def ex_kurtosis(self) -> float:

        if self.scale == 0:
            raise Exception("Moment undefined")

        return 24 / 5
#10
    def mvsk(self) -> List[float]:

        if self.scale == 0:
            raise Exception("Moment undefined")

        mean_val = self.mean()
        variance_val = self.variance()
        skewness_val = 0  # Ferdeség értéke a Logisztikus eloszlásnál
        kurtosis_val = 24 / 5  # Többlet csúcsosság értéke a Logisztikus eloszlásnál

        return [mean_val, variance_val, skewness_val, kurtosis_val]
#11
class ChiSquaredDistribution:
    def __init__(self, rand: random.Random, dof: int):

            self.rand = rand
            self.dof = dof
#12
    def pdf(self, x: float) -> float:

        if x < 0:
            return 0
        coefficient = 1 / (2 ** (self.dof / 2) * gamma(self.dof / 2))
        return coefficient * x ** (self.dof / 2 - 1) * exp(-x / 2)
#13
    def cdf(self, x: float) -> float:

        if x < 0:
            return 0
        return gamma(self.dof / 2, x / 2) / gamma(self.dof / 2)
#14
    def ppf(self, p: float) -> float:

        if not (0 <= p <= 1):
            raise ValueError("A valószínűség értéke 0 és 1 között kell legyen.")
        return 2 * gamma_inv(p, self.dof / 2)
#15
    def gen_rand(self) -> float:

        return sum(self.rand.gauss(0, 1) ** 2 for _ in range(self.dof))
#16
    def mean(self) -> float:

        if self.dof <= 1:
            raise Exception("Moment undefined")

        return self.dof
#17
    def variance(self) -> float:

        if self.dof <= 2:
            raise Exception("Moment undefined")

        return 2 * self.dof
#18
    def skewness(self) -> float:

        if self.dof <= 3:
            raise Exception("Moment undefined")

        return sqrt(8 / self.dof)
#19
    def ex_kurtosis(self) -> float:

        if self.dof <= 4:
            raise Exception("Moment undefined")

        return 12 / self.dof
#20
    def mvsk(self) -> List[float]:

        if self.dof <= 4:
            raise Exception("Moment undefined")

        first_moment = self.mean()
        second_central_moment = self.variance()
        third_central_moment = 0  # A Chi-négyzet eloszlásnál a ferdeség értéke 0
        excess_kurtosis = 12 / self.dof

        return [first_moment, second_central_moment, third_central_moment, excess_kurtosis]