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
class LaplaceDistribution:
    def __init__(self, rand, loc, scale):
        """
        LaplaceDistribution osztály konstruktor.

        Args:
            rand: Véletlenszám generátor objektum.
            loc: Laplace eloszlás várható értéke.
            scale: Laplace eloszlás skálája (variancia).
        """
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def generate_sample(self):
        """
        Generál egy mintát a Laplace eloszlásból.

        Returns:
            float: A generált minta.
        """
        u = self.rand.random() - 0.5  # Szimmetrikus Laplace eloszlás miatt
        if u >= 0:
            return self.loc - self.scale * u * 2.0
        else:
            return self.loc + self.scale * (-u) * 2.0

    def pdf(self, x):
        """
        Kiszámítja az aszimmetrikus Laplace eloszlás valószínűségi sűrűségfüggvényét a megadott x-hez.

        Args:
            x: A valós szám, amelyhez a valószínűségi sűrűségfüggvényt számítjuk.

        Returns:
            float: A valószínűségi sűrűségfüggvény értéke az x-hez.
        """
        abs_diff = abs(x - self.loc)
        if x < self.loc:
            return 0.5 / self.scale * math.exp(abs_diff / self.scale)
        else:
            return 0.5 / self.scale * math.exp(-abs_diff / self.scale)

#3
class LaplaceDistribution:
    def __init__(self, rand, loc, scale):
        """
        LaplaceDistribution osztály konstruktor.

        Args:
            rand: Véletlenszám generátor objektum.
            loc: Laplace eloszlás várható értéke.
            scale: Laplace eloszlás skálája (variancia).
        """
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def generate_sample(self):
        """
        Generál egy mintát a Laplace eloszlásból.

        Returns:
            float: A generált minta.
        """
        u = self.rand.random() - 0.5  # Szimmetrikus Laplace eloszlás miatt
        if u >= 0:
            return self.loc - self.scale * u * 2.0
        else:
            return self.loc + self.scale * (-u) * 2.0

    def pdf(self, x):
        """
        Kiszámítja az aszimmetrikus Laplace eloszlás valószínűségi sűrűségfüggvényét a megadott x-hez.

        Args:
            x: A valós szám, amelyhez a valószínűségi sűrűségfüggvényt számítjuk.

        Returns:
            float: A valószínűségi sűrűségfüggvény értéke az x-hez.
        """
        abs_diff = abs(x - self.loc)
        if x < self.loc:
            return 0.5 / self.scale * math.exp(abs_diff / self.scale)
        else:
            return 0.5 / self.scale * math.exp(-abs_diff / self.scale)

    def cdf(self, x):
        """
        Kiszámítja az aszimmetrikus Laplace eloszlás kumulatív eloszlásfüggvényét a megadott x-hez.

        Args:
            x: A valós szám, amelyhez a kumulatív eloszlásfüggvényt számítjuk.

        Returns:
            float: A kumulatív eloszlásfüggvény értéke az x-hez.
        """
        if x < self.loc:
            return 0.5 * math.exp((x - self.loc) / self.scale)
        else:
            return 1.0 - 0.5 * math.exp(-(x - self.loc) / self.scale)
#4
class LaplaceDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def generate_sample(self):
        u = self.rand.random() - 0.5
        if u >= 0:
            return self.loc - self.scale * u * 2.0
        else:
            return self.loc + self.scale * (-u) * 2.0

    def pdf(self, x):
        abs_diff = abs(x - self.loc)
        if x < self.loc:
            return 0.5 / self.scale * math.exp(abs_diff / self.scale)
        else:
            return 0.5 / self.scale * math.exp(-abs_diff / self.scale)

    def cdf(self, x):
        if x < self.loc:
            return 0.5 * math.exp((x - self.loc) / self.scale)
        else:
            return 1.0 - 0.5 * math.exp(-(x - self.loc) / self.scale)

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Az 'p' értéknek 0 és 1 között kell lennie.")
        if p < 0.5:
            return self.loc - self.scale * math.log(1.0 - 2.0 * p)
        else:
            return self.loc + self.scale * math.log(2.0 * p - 1.0)
#5
class LaplaceDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def generate_sample(self):
        u = self.rand.random() - 0.5
        if u >= 0:
            return self.loc - self.scale * u * 2.0
        else:
            return self.loc + self.scale * (-u) * 2.0

    def pdf(self, x):
        abs_diff = abs(x - self.loc)
        if x < self.loc:
            return 0.5 / self.scale * math.exp(abs_diff / self.scale)
        else:
            return 0.5 / self.scale * math.exp(-abs_diff / self.scale)

    def cdf(self, x):
        if x < self.loc:
            return 0.5 * math.exp((x - self.loc) / self.scale)
        else:
            return 1.0 - 0.5 * math.exp(-(x - self.loc) / self.scale)

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Az 'p' értéknek 0 és 1 között kell lennie.")
        if p < 0.5:
            return self.loc - self.scale * math.log(1.0 - 2.0 * p)
        else:
            return self.loc + self.scale * math.log(2.0 * p - 1.0)

    def gen_random(self):
        u = self.rand.random() - 0.5
        if u >= 0:
            return self.loc - self.scale * u * 2.0
        else:
            return self.loc + self.scale * (-u) * 2.0
#6
class LaplaceDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def generate_sample(self):
        u = self.rand.random() - 0.5
        if u >= 0:
            return self.loc - self.scale * u * 2.0
        else:
            return self.loc + self.scale * (-u) * 2.0

    def pdf(self, x):
        abs_diff = abs(x - self.loc)
        if x < self.loc:
            return 0.5 / self.scale * math.exp(abs_diff / self.scale)
        else:
            return 0.5 / self.scale * math.exp(-abs_diff / self.scale)

    def cdf(self, x):
        if x < self.loc:
            return 0.5 * math.exp((x - self.loc) / self.scale)
        else:
            return 1.0 - 0.5 * math.exp(-(x - self.loc) / self.scale)

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Az 'p' értéknek 0 és 1 között kell lennie.")
        if p < 0.5:
            return self.loc - self.scale * math.log(1.0 - 2.0 * p)
        else:
            return self.loc + self.scale * math.log(2.0 * p - 1.0)

    def gen_random(self):
        u = self.rand.random() - 0.5
        if u >= 0:
            return self.loc - self.scale * u * 2.0
        else:
            return self.loc + self.scale * (-u) * 2.0

    def mean(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return self.loc
#7
class LaplaceDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def generate_sample(self):
        u = self.rand.random() - 0.5
        if u >= 0:
            return self.loc - self.scale * u * 2.0
        else:
            return self.loc + self.scale * (-u) * 2.0

    def pdf(self, x):
        abs_diff = abs(x - self.loc)
        if x < self.loc:
            return 0.5 / self.scale * math.exp(abs_diff / self.scale)
        else:
            return 0.5 / self.scale * math.exp(-abs_diff / self.scale)

    def cdf(self, x):
        if x < self.loc:
            return 0.5 * math.exp((x - self.loc) / self.scale)
        else:
            return 1.0 - 0.5 * math.exp(-(x - self.loc) / self.scale)

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Az 'p' értéknek 0 és 1 között kell lennie.")
        if p < 0.5:
            return self.loc - self.scale * math.log(1.0 - 2.0 * p)
        else:
            return self.loc + self.scale * math.log(2.0 * p - 1.0)

    def gen_random(self):
        u = self.rand.random() - 0.5
        if u >= 0:
            return self.loc - self.scale * u * 2.0
        else:
            return self.loc + self.scale * (-u) * 2.0

    def mean(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return self.loc

    def variance(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return 2.0 * self.scale * self.scale
#8
class LaplaceDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def generate_sample(self):
        u = self.rand.random() - 0.5
        if u >= 0:
            return self.loc - self.scale * u * 2.0
        else:
            return self.loc + self.scale * (-u) * 2.0

    def pdf(self, x):
        abs_diff = abs(x - self.loc)
        if x < self.loc:
            return 0.5 / self.scale * math.exp(abs_diff / self.scale)
        else:
            return 0.5 / self.scale * math.exp(-abs_diff / self.scale)

    def cdf(self, x):
        if x < self.loc:
            return 0.5 * math.exp((x - self.loc) / self.scale)
        else:
            return 1.0 - 0.5 * math.exp(-(x - self.loc) / self.scale)

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Az 'p' értéknek 0 és 1 között kell lennie.")
        if p < 0.5:
            return self.loc - self.scale * math.log(1.0 - 2.0 * p)
        else:
            return self.loc + self.scale * math.log(2.0 * p - 1.0)

    def gen_random(self):
        u = self.rand.random() - 0.5
        if u >= 0:
            return self.loc - self.scale * u * 2.0
        else:
            return self.loc + self.scale * (-u) * 2.0

    def mean(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return self.loc

    def variance(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return 2.0 * self.scale * self.scale

    def skewness(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return 0.0
#9
class LaplaceDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def generate_sample(self):
        u = self.rand.random() - 0.5
        if u >= 0:
            return self.loc - self.scale * u * 2.0
        else:
            return self.loc + self.scale * (-u) * 2.0

    def pdf(self, x):
        abs_diff = abs(x - self.loc)
        if x < self.loc:
            return 0.5 / self.scale * math.exp(abs_diff / self.scale)
        else:
            return 0.5 / self.scale * math.exp(-abs_diff / self.scale)

    def cdf(self, x):
        if x < self.loc:
            return 0.5 * math.exp((x - self.loc) / self.scale)
        else:
            return 1.0 - 0.5 * math.exp(-(x - self.loc) / self.scale)

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Az 'p' értéknek 0 és 1 között kell lennie.")
        if p < 0.5:
            return self.loc - self.scale * math.log(1.0 - 2.0 * p)
        else:
            return self.loc + self.scale * math.log(2.0 * p - 1.0)

    def gen_random(self):
        u = self.rand.random() - 0.5
        if u >= 0:
            return self.loc - self.scale * u * 2.0
        else:
            return self.loc + self.scale * (-u) * 2.0

    def mean(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return self.loc

    def variance(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return 2.0 * self.scale * self.scale

    def skewness(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return 0.0

    def ex_kurtosis(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return 3.0

#10
class LaplaceDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def generate_sample(self):
        u = self.rand.random() - 0.5
        if u >= 0:
            return self.loc - self.scale * u * 2.0
        else:
            return self.loc + self.scale * (-u) * 2.0

    def pdf(self, x):
        abs_diff = abs(x - self.loc)
        if x < self.loc:
            return 0.5 / self.scale * math.exp(abs_diff / self.scale)
        else:
            return 0.5 / self.scale * math.exp(-abs_diff / self.scale)

    def cdf(self, x):
        if x < self.loc:
            return 0.5 * math.exp((x - self.loc) / self.scale)
        else:
            return 1.0 - 0.5 * math.exp(-(x - self.loc) / self.scale)

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Az 'p' értéknek 0 és 1 között kell lennie.")
        if p < 0.5:
            return self.loc - self.scale * math.log(1.0 - 2.0 * p)
        else:
            return self.loc + self.scale * math.log(2.0 * p - 1.0)

    def gen_random(self):
        u = self.rand.random() - 0.5
        if u >= 0:
            return self.loc - self.scale * u * 2.0
        else:
            return self.loc + self.scale * (-u) * 2.0

    def mean(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return self.loc

    def variance(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return 2.0 * self.scale * self.scale

    def skewness(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return 0.0

    def ex_kurtosis(self):
        if self.scale == 0:
            raise Exception("Moment undefined")
        return 3.0

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
class ParetoDistribution:
    def __init__(self, rand, scale, shape):
        self.rand = rand
        self.scale = scale
        self.shape = shape

    def pdf(self, x):
        if x >= self.scale:
            return (self.shape * self.scale**self.shape) / (x**(self.shape + 1))
        else:
            return 0.0
#13
class ParetoDistribution:
    def __init__(self, rand, scale, shape):
        self.rand = rand
        self.scale = scale
        self.shape = shape

    def pdf(self, x):
        if x >= self.scale:
            return (self.shape * self.scale**self.shape) / (x**(self.shape + 1))
        else:
            return 0.0

    def cdf(self, x):
        if x >= self.scale:
            return 1.0 - (self.scale / x)**self.shape
        else:
            return 0.0

#14
    class ParetoDistribution:
    def __init__(self, rand, scale, shape):
        self.rand = rand
        self.scale = scale
        self.shape = shape

    def pdf(self, x):
        if x >= self.scale:
            return (self.shape * self.scale**self.shape) / (x**(self.shape + 1))
        else:
            return 0.0

    def cdf(self, x):
        if x >= self.scale:
            return 1.0 - (self.scale / x)**self.shape
        else:
            return 0.0

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Az 'p' értéknek 0 és 1 között kell lennie.")
        return self.scale / ((1.0 - p)**(1.0/self.shape))
#15
class ParetoDistribution:
    def __init__(self, rand, scale, shape):
        self.rand = rand
        self.scale = scale
        self.shape = shape

    def pdf(self, x):
        if x >= self.scale:
            return (self.shape * self.scale**self.shape) / (x**(self.shape + 1))
        else:
            return 0.0

    def cdf(self, x):
        if x >= self.scale:
            return 1.0 - (self.scale / x)**self.shape
        else:
            return 0.0

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Az 'p' értéknek 0 és 1 között kell lennie.")
        return self.scale / ((1.0 - p)**(1.0/self.shape))

    def gen_random(self):
        u = self.rand.random()
        return self.scale / u**(1.0/self.shape)

#16
class ParetoDistribution:
    def __init__(self, rand, scale, shape):
        self.rand = rand
        self.scale = scale
        self.shape = shape

    def pdf(self, x):
        if x >= self.scale:
            return (self.shape * self.scale**self.shape) / (x**(self.shape + 1))
        else:
            return 0.0

    def cdf(self, x):
        if x >= self.scale:
            return 1.0 - (self.scale / x)**self.shape
        else:
            return 0.0

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Az 'p' értéknek 0 és 1 között kell lennie.")
        return self.scale / ((1.0 - p)**(1.0/self.shape))

    def gen_random(self):
        u = self.rand.random()
        return self.scale / u**(1.0/self.shape)

    def mean(self):
        if self.shape <= 1:
            raise Exception("Moment undefined")
        return (self.shape * self.scale) / (self.shape - 1)

#17
class ParetoDistribution:
    def __init__(self, rand, scale, shape):
        self.rand = rand
        self.scale = scale
        self.shape = shape

    def pdf(self, x):
        if x >= self.scale:
            return (self.shape * self.scale**self.shape) / (x**(self.shape + 1))
        else:
            return 0.0

    def cdf(self, x):
        if x >= self.scale:
            return 1.0 - (self.scale / x)**self.shape
        else:
            return 0.0

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Az 'p' értéknek 0 és 1 között kell lennie.")
        return self.scale / ((1.0 - p)**(1.0/self.shape))

    def gen_random(self):
        u = self.rand.random()
        return self.scale / u**(1.0/self.shape)

    def mean(self):
        if self.shape <= 1:
            raise Exception("Moment undefined")
        return (self.shape * self.scale) / (self.shape - 1)

    def variance(self):
        if self.shape <= 2:
            raise Exception("Moment undefined")
        return (self.scale**2 * self.shape) / ((self.shape - 1)**2 * (self.shape - 2))

#18
class ParetoDistribution:
    def __init__(self, rand, scale, shape):
        self.rand = rand
        self.scale = scale
        self.shape = shape

    def pdf(self, x):
        if x >= self.scale:
            return (self.shape * self.scale**self.shape) / (x**(self.shape + 1))
        else:
            return 0.0

    def cdf(self, x):
        if x >= self.scale:
            return 1.0 - (self.scale / x)**self.shape
        else:
            return 0.0

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Az 'p' értéknek 0 és 1 között kell lennie.")
        return self.scale / ((1.0 - p)**(1.0/self.shape))

    def gen_random(self):
        u = self.rand.random()
        return self.scale / u**(1.0/self.shape)

    def mean(self):
        if self.shape <= 1:
            raise Exception("Moment undefined")
        return (self.shape * self.scale) / (self.shape - 1)

    def variance(self):
        if self.shape <= 2:
            raise Exception("Moment undefined")
        return (self.scale**2 * self.shape) / ((self.shape - 1)**2 * (self.shape - 2))

    def skewness(self):
        if self.shape <= 3:
            raise Exception("Moment undefined")
        return (2.0 * (1.0 + self.shape)) / ((self.shape - 3) * (self.shape - 1)) * math.sqrt((self.shape - 2) / self.shape)

#19
class ParetoDistribution:
    def __init__(self, rand, scale, shape):
        self.rand = rand
        self.scale = scale
        self.shape = shape

    def pdf(self, x):
        if x >= self.scale:
            return (self.shape * self.scale**self.shape) / (x**(self.shape + 1))
        else:
            return 0.0

    def cdf(self, x):
        if x >= self.scale:
            return 1.0 - (self.scale / x)**self.shape
        else:
            return 0.0

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Az 'p' értéknek 0 és 1 között kell lennie.")
        return self.scale / ((1.0 - p)**(1.0/self.shape))

    def gen_random(self):
        u = self.rand.random()
        return self.scale / u**(1.0/self.shape)

    def mean(self):
        if self.shape <= 1:
            raise Exception("Moment undefined")
        return (self.shape * self.scale) / (self.shape - 1)

    def variance(self):
        if self.shape <= 2:
            raise Exception("Moment undefined")
        return (self.scale**2 * self.shape) / ((self.shape - 1)**2 * (self.shape - 2))

    def skewness(self):
        if self.shape <= 3:
            raise Exception("Moment undefined")
        return (2.0 * (1.0 + self.shape)) / ((self.shape - 3) * (self.shape - 1)) * math.sqrt((self.shape - 2) / self.shape)

    def ex_kurtosis(self):
        if self.shape <= 4:
            raise Exception("Moment undefined")
        return (6.0 / self.shape) * ((self.shape**3 + 9*self.shape**2 + 8*self.shape - 6) / (self.shape - 3)) / ((self.shape - 4) / self.shape)

#20
class ParetoDistribution:
    def __init__(self, rand, scale, shape):
        self.rand = rand
        self.scale = scale
        self.shape = shape

    def pdf(self, x):
        if x >= self.scale:
            return (self.shape * self.scale**self.shape) / (x**(self.shape + 1))
        else:
            return 0.0

    def cdf(self, x):
        if x >= self.scale:
            return 1.0 - (self.scale / x)**self.shape
        else:
            return 0.0

    def ppf(self, p):
        if p < 0.0 or p > 1.0:
            raise ValueError("Az 'p' értéknek 0 és 1 között kell lennie.")
        return self.scale / ((1.0 - p)**(1.0/self.shape))

    def gen_random(self):
        u = self.rand.random()
        return self.scale / u**(1.0/self.shape)

    def mean(self):
        if self.shape <= 1:
            raise Exception(