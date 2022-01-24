import constants as const


def f1(x1, x2):
  return (x1 - 2. * x2)**2. + (3. * x2 - const.N)**2.


def f2(x1, x2):
  return (3. * const.N * x2 - x1**2.)**2. + (const.N - x1)**2.
