#1
class LaplaceDistribution:
    def __init__(self, rand, loc, scale):

        self.rand = rand
        self.loc = loc
        self.scale = scale

    def generate_sample(self):

        u = self.rand.random() - 0.5  # Szimmetrikus Laplace eloszlás miatt
        if u >= 0:
            return self.loc - self.scale * u * 2.0
        else:
            return self.loc + self.scale * (-u) * 2.0

#2

    def pdf(self, x):
        exponent = -abs(x - self.loc) / self.scale
        probability = (1 / (2 * self.scale)) * math.exp(exponent)
        if x < self.loc:
            probability *= 1
        else:
            probability *= 1
        return probability
#3
    def cdf(self, x):

        if x < self.loc:
            return 0.5 * math.exp((x - self.loc) / self.scale)
        else:
            return 1.0 - 0.5 * math.exp(-(x - self.loc) / self.scale)
#4

    def ppf(self, p):
        if p < 0 or p > 1:
            raise ValueError("A valószínűség értéke 0 és 1 között kell legyen.")
        if p < 0.5:
            ppf_value = self.loc + self.scale * math.log(2 * p )
        else:
            ppf_value = self.loc - self.scale * math.log(2 * (1 - p) )
        return ppf_value
#5
    def gen_rand(self):
        u = random.uniform(0, 1)
        if u < 0.5:
            random_value = self.loc + self.scale * math.log(2 * u)
        else:
            random_value = self.loc - self.scale * math.log(2 * (1 - u))
        return random_value

#6
    def mean(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return self.loc
#7
    def variance(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return 2.0 * self.scale * self.scale
#8
    def skewness(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return 0.0
#9
    def ex_kurtosis(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return 3.0

#10

    def mvsk(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]

#11
class ParetoDistribution:
    def __init__(self, rand, scale, shape):
        self.rand = rand
        self.scale = scale
        self.shape = shape

#12
    def pdf(self, x):
        if x >= self.scale:
            return (self.shape * self.scale**self.shape) / (x**(self.shape + 1))
        else:
            return 0.0
#13

    def cdf(self, x):
        if x >= self.scale:
            return 1.0 - (self.scale / x)**self.shape
        else:
            return 0.0

#14
    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Az 'p' értéknek 0 és 1 között kell lennie.")
        return self.scale / ((1.0 - p)**(1.0/self.shape))
#15
    def gen_rand(self):
        u = random.uniform(0, 1)
        return self.ppf(u)
#16
    def mean(self):
        if self.shape <= 1:
            raise Exception("Moment undefined")
        else:
            return (self.shape * self.scale) / (self.shape - 1)
#17
    def variance(self):
        if self.shape > 2:
            return (self.scale ** 2 * self.shape) / ((self.shape - 1) ** 2 * (self.shape - 2))
        else:
            raise Exception("Moment undefined")
#18
    def skewness(self):
        if self.shape <= 3:
            raise Exception("Moment undefined")
        else:
            return (2 * (1 + self.shape)) / (self.shape - 3) * ((self.shape - 2) / self.shape) ** 0.5
#19
    def ex_kurtosis(self):
        if self.shape <= 4:
            raise Exception("Moment undefined")
        else:
            return (6 * (self.shape ** 3 + self.shape ** 2 - 6 * self.shape - 2)) / (self.shape * (self.shape - 3) * (self.shape - 4))

#20
    def mvsk(self):
        if self.shape <= 1:
            raise Exception("Moment undefined")
        else:
            return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]