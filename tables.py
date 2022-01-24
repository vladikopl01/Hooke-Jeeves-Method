from math import ceil

from scipy.optimize import fmin

from functions import *


def AnalyticData():
  def func1(x): return f1(x[0], x[1])
  def func2(x): return f2(x[0], x[1])
  analytic = [
      fmin(func1, const.x0, ftol=const.eps, full_output=True, disp=False),
      fmin(func2, const.x0, ftol=const.eps, full_output=True, disp=False)
  ]

  print('=' * 67)
  print("│ {:^63} │".format('Analytic solution'))
  print('=' * 67)
  print("│ {:^8s} │ {:^10s} │ {:^11s} │ {:^11s} │ {:^11s} │".
        format('Function', 'Iterations', 'x1', 'x2', 'F(x1, x2)'))
  print('=' * 67)

  for i in range(len(analytic)):
    print("│ {:8d} │ {:10} │ {:11.5} │ {:11.5} │ {:11.5} │".
          format(i + 1,
                 analytic[i][2],
                 analytic[i][0][0],
                 analytic[i][0][1],
                 analytic[i][1]))
    print('─' * 67)


def ResultData(xs1, xs2):
  print('=' * 67)
  print("│ {:^63} │".format('Minimize solution'))
  print('=' * 67)
  print("│ {:^8s} │ {:^10s} │ {:^11s} │ {:^11s} │ {:^11s} │".
        format('Function', 'Iterations', 'x1', 'x2', 'F(x1, x2)'))
  print('=' * 67)

  xs = [xs1.transpose()[-1], xs2.transpose()[-1]]
  result = [f1(*xs[0]), f2(*xs[1])]
  iterations = [len(xs1.transpose()) - 1, len(xs2.transpose()) - 1]

  for i in range(2):
    print("│ {:8d} │ {:10} │ {:11.5} │ {:11.5} │ {:11.5} │".
          format(i + 1,
                 iterations[i],
                 xs[i][0],
                 xs[i][1],
                 result[i]
                 )
          )
    print('─' * 67)


def FunctionData(f, xs, name):
  print('=' * 49)
  print("│ {:^45} │".format(name))
  print('=' * 49)
  print("│ {:^3s} │ {:^11s} │ {:^11s} │ {:^11s} │".
        format('K', 'x1', 'x2', 'F(x1, x2)'))
  print('=' * 49)

  for i in range(len(xs[0])):
    print("│ {:3d} │ {:11.5} │ {:11.5} │ {:11.5} │".
          format(i if not i else ceil(i / 3),
                 xs[0][i], xs[1][i],
                 f(xs[0][i], xs[1][i])
                 ))
    print('─' * 49)
