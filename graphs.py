import matplotlib.pyplot as plt
from numpy import linspace, meshgrid

import constants as const


def FunctionLevelRoute(f, xs, name=None):
  plt.figure()
  plt.xlabel('X1')
  plt.ylabel('X2')
  plt.xlim(-8.5, 8.5)
  plt.ylim(-8.5, 8.5)

  levels = linspace(
      min(f(xs[0], xs[1])),
      max(f(xs[0], xs[1])),
      const.levels
  )

  x = linspace(const.interval['x1'][0] * 15, const.interval['x1'][1] * 15, 1000)
  y = linspace(const.interval['x2'][0] * 15, const.interval['x2'][1] * 15, 1000)

  X, Y = meshgrid(x, y)
  Z = f(X, Y)

  plt.plot(xs[0], xs[1], 'mo--', label='Minimization route', zorder=4)
  plt.contour(X, Y, Z, levels, colors='purple', zorder=3)
  contourf = plt.contourf(X, Y, Z, levels, cmap='RdPu', zorder=2, alpha=0.7)

  plt.legend()
  plt.colorbar(contourf)
  plt.grid(zorder=1)
  plt.title(name)
  plt.show()


def Xk(xs):
  tmpX1 = xs[0]
  tmpX2 = xs[1]
  K = range(len(tmpX1))

  # X1 graph
  plt.subplot(1, 2, 1)
  plt.xlabel('K')
  plt.ylabel('X1')
  plt.title('X1 steps')
  plt.grid()

  plt.plot(K, tmpX1, 'o--')
  plt.plot(K, tmpX2, 'ko--', color='grey', alpha=0.3)
  plt.legend(['X1', 'X2'])

  # X2 graph
  plt.subplot(1, 2, 2)
  plt.xlabel('K')
  plt.ylabel('X2')
  plt.title('X2 steps')
  plt.grid()

  plt.plot(K, tmpX2, 'o--')
  plt.plot(K, tmpX1, 'o--', color='grey', alpha=0.3)
  plt.legend(['X2', 'X1'])

  plt.show()


def Xs(xs, func_num, name=None):
  plt.xlabel('Xs2')
  plt.ylabel('Xs1')
  plt.title(name)
  plt.grid()

  plt.plot(xs[1], xs[0], 'o-')
  plt.legend([f'X steps'])

  plt.show()


def FunctionK(f, xs, func_num, name=None):
  tmp_func = [f(xs[0][i], xs[1][i]) for i in range(len(xs[0]))]
  K = range(len(tmp_func))

  plt.xlabel('K')
  plt.ylabel(f'F{func_num}')
  plt.title(name)
  plt.grid()

  plt.plot(K, tmp_func, 'mo-')
  plt.legend([f'Function{func_num} values'])

  plt.show()


def Fk(f1, xs1, f2, xs2):
  tmp_func1 = [f1(xs1[0][i], xs1[1][i]) for i in range(1, len(xs1[0]))]
  tmp_func2 = [f2(xs2[0][i], xs2[1][i]) for i in range(1, len(xs2[0]))]

  if len(tmp_func1) < len(tmp_func2):
    for i in range(len(tmp_func1), len(tmp_func2)):
      tmp_func1.append(tmp_func1[-1])
  elif len(tmp_func2) < len(tmp_func1):
    for i in range(len(tmp_func2), len(tmp_func1)):
      tmp_func2.append(tmp_func2[-1])

  K = range(max(len(tmp_func1), len(tmp_func2)))

  # F1 graph
  plt.subplot(1, 2, 1)
  plt.xlabel('K')
  plt.ylabel('Function 1')
  plt.title('Function 1 values')
  plt.grid()

  plt.plot(K, tmp_func1, 'mo--')
  plt.plot(K, tmp_func2, 'ko--', color='grey', alpha=0.3)
  plt.legend(['Function 1', 'Function 2'])

  # F2 graph
  plt.subplot(1, 2, 2)
  plt.xlabel('K')
  plt.ylabel('Function 2')
  plt.title('Function 2 values')
  plt.grid()

  plt.plot(K, tmp_func2, 'mo--')
  plt.plot(K, tmp_func1, 'o--', color='grey', alpha=0.3)
  plt.legend(['Function 2', 'Function 1'])

  plt.show()
