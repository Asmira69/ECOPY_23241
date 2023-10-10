#GY7EJG
#week3
import pyerf
import typing
import random
import math

####################################DISTRIBUTIONS#############################

class FirstClass:
    pass

class SecondClass:
    def __init__ (self, rand):
        self.random = rand
class UniformDistribution:
    def __init__(self, rand, a, b):
        self.rand = rand
        self.a = a
        self.b = b

    def pdf(self, x):
        if x >= self.a and x <= self.b:
            return 1.0 / (self.b - self.a)
        else:
            return 0.0
    def cdf(self, x):
        if x < self.a:
            return 0.0
        elif x >= self.a and x <= self.b:
            return (x - self.a) / (self.b - self.a)
        else:
            return 1.0

    def ppf(self, p):
        if p < 0:
            return self.a
        elif p > 1:
            return self.b
        return self.a + p * (self.b - self.a)

    def gen_rand(self):
        return self.rand.uniform(self.a, self.b)

    def mean(self):
        if self.a == self.b:
          raise Exception("Moment undefined")
        return (self.a + self.b) / 2.0

    def median(self):
        return (self.b + self.a) / 2

    def variance(self):
        if self.a == self.b:
            raise Exception("Moment undefined")
        #return ((self.b - self.a) ** 2) / 12
        return (self.b - self.a) / 12

    def skewness(self):
        if self.a == self.b:
            raise Exception("Moment undefined")
        return 0.0
    def ex_kurtosis(self):
        if self.a == self.b:
            raise Exception("Moment undefined")
        return 1.8-3

    def mvsk(self):
        if self.a == self.b:
            raise Exception("Moments undefined")
        mean = self.mean()
        variance = self.variance()
        skewness = self.skewness()
        ex_kurtosis = self.ex_kurtosis()
        return [mean, variance, skewness, ex_kurtosis]


import math
import random
from pyerf import pyerf
class NormalDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def pdf(self, x):
        return (1 / (self.scale**0.5 * ((2 * math.pi) ** 0.5))) * (math.e ** (-0.5 * (((x - self.loc) / self.scale**0.5) ** 2)))

    def cdf(self, x):
        return 0.5 * (1 + math.erf((x - self.loc) / (self.scale**0.5 * (2 ** 0.5))))

    def ppf(self, p):
        if p < 0 or p > 1:
            raise ValueError("p must be between 0 and 1")
        return self.loc + self.scale**0.5 * (2 ** 0.5) * pyerf.erfinv(2 * p - 1)

    def gen_rand(self):
        return random.normalvariate(self.loc, math.sqrt(self.scale))

    def mean(self):
        return self.loc

    def median(self):
        return self.loc

    def variance(self):
            return self.scale

    def skewness(self):
        return 0

    def ex_kurtosis(self):
        return 0

    def mvsk(self):
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]


class CauchyDistribution:
    def __init__(self, rand, x0, gamma):
        self.rand = rand
        self.loc = x0
        self.scale = gamma

    def pdf(self, x):
        if self.scale <= 0:
            return 0.0
        else:
            return 1.0 / (math.pi * self.scale * (1.0 + ((x - self.loc) / self.scale) ** 2))

    def cdf(self, x):
        if self.scale <= 0:
            return 0.0
        else:
            return 0.5 + (1.0 / math.pi) * math.atan((x - self.loc) / self.scale)

    def ppf(self, p):
        if p < 0 or p > 1:
            raise ValueError("Az 'p' értéke 0 és 1 között kell legyen.")
        if p == 0.5:
            return self.loc
        return self.loc + self.scale * math.tan(math.pi * (p - 0.5))


    def gen_rand(self):
        return self.loc + self.scale * math.tan(math.pi * (self.rand.random() - 0.5))

    def mean(self):
        raise Exception("Moment undefined")

    def median(self):
        return self.loc

    def variance(self):
        raise Exception("Moment undefined")

    def skewness(self):
        raise Exception("Moment undefined")

    def ex_kurtosis(self):
        raise Exception("Moment undefined")

    def mvsk(self):
        raise Exception("Moments undefined")

import random
import math
import scipy.special

class LogisticDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.location = loc
        self.scale = scale

    def pdf(self, x):
        coefficient = 1 / (4 * self.scale)
        exponent = -abs((x - self.location) / (2 * self.scale))
        pdf_value = coefficient * math.pow(math.cosh(exponent), -2)
        return pdf_value

    def cdf(self, x):
        cdf_value = 1 / (1 + math.exp(-(x - self.location) / self.scale))
        return cdf_value

    def ppf(self, p):
        ppf_value = self.location + self.scale * math.log(p / (1 - p))
        return ppf_value

    def gen_rand(self):
        u = random.random()
        rand_value = self.location + self.scale * math.log(u / (1 - u))
        return rand_value

    def mean(self):
        if self.scale <= 0:
            raise Exception("Moment undefined")
        return self.location


    def variance(self):
        if self.scale is None:
            raise Exception("Moment undefined")
        var = (math.pi ** 2) * (self.scale ** 2) / 3
        return var


    def skewness(self):
        return 0

    def ex_kurtosis(self):
        return 6/5

    def mvsk(self):
        mean = self.location
        var = (math.pi ** 2) * (self.scale ** 2) / 3
        skewness = 0
        excess_kurtosis = 1.2

        return [mean, var, skewness, excess_kurtosis]
class ChiSquaredDistribution:
    def __init__(self, rand, dof):
        self.rand = rand
        self.dof = dof

    def pdf(self, x):
        if x < 0:
            return 0
        coefficient = (1 / (2 ** (self.dof / 2))) * (1 / math.gamma(self.dof / 2))
        pdf_value = coefficient * (x ** ((self.dof / 2) - 1)) * math.exp(-x / 2)
        return pdf_value

    def cdf(self, x):
        cdf = scipy.special.gammainc((self.dof) / 2.0, x / 2.0)
        return cdf

    def ppf(self, p):
        ppf = 2.0 * scipy.special.gammaincinv((self.dof) / 2.0, p)
        return ppf

    def gen_rand(self):
        u = self.rand.uniform(0,1)
        rand_value = self.ppf(u)
        return rand_value
    def mean(self):
        return self.dof

    def variance(self):
        return 2 * self.dof

    def skewness(self):
        return (8 / self.dof)**0.5

    def ex_kurtosis(self):
        return 12 / self.dof

    def mvsk(self):
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]