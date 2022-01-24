from numpy import append, array, fabs, sqrt

import constants as const


def GoldenSection(f, xs, index, a, b):
  koef = (sqrt(5) - 1) / 2.0
  temp = (a + b) / 2

  p = a + (1 - koef) * (b - a)
  q = a + koef * (b - a)

  k = 1
  while fabs(b - a) > const.eps and k < const.k_max:
    xs[index] = p
    cur_a = f(xs[0], xs[1])
    xs[index] = q
    cur_b = f(xs[0], xs[1])

    if cur_a > cur_b:
      a = p
      p = q
      q = a + koef * (b - a)
    else:
      b = q
      q = p
      p = a + (1 - koef) * (b - a)

  temp = (a + b) / 2
  k += 1
  return temp


def HookeJeeves(f, x0, interval):
  cur_x = array([x0])
  temp_x = list(x0)
  start_x = list(x0)

  for index in range(2):
    temp_x[index] = GoldenSection(
        f, list(temp_x), index,
        interval[f'x{index + 1}'][0],
        interval[f'x{index + 1}'][1]
    )
    cur_x = append(cur_x, [temp_x], axis=0)

  new_start_x = list(temp_x)
  k = 1
  while k <= const.k_max:
    temp = pattern_search(f, start_x, new_start_x, interval)
    temp_x = check_bounds(temp, start_x, new_start_x, interval)

    if is_less_than_eps(new_start_x, temp_x):
      break

    cur_x = append(cur_x, [temp_x], axis=0)

    start_x = list(new_start_x)

    for index in range(2):
      temp_x[index] = GoldenSection(
          f, list(temp_x), index,
          interval[f'x{index + 1}'][0],
          interval[f'x{index + 1}'][1]
      )
      cur_x = append(cur_x, [temp_x], axis=0)

    new_start_x = list(temp_x)
    k += 1
  return cur_x.transpose()


def pattern_search(f, X0, X1, interval):
  x = [0, 0]

  def eq_for_x2(x1): return X0[1] + (x1 - X0[0]) * (X1[1] - X0[1]) / (X1[0] - X0[0])

  def new_f():
    def inner(x1, _):
      return f(x1, eq_for_x2(x1))
    return inner

  x[0] = GoldenSection(
      new_f(), list(x), 0,
      interval['x1'][0],
      interval['x1'][1]
  )
  x[1] = eq_for_x2(x[0])

  return x


def is_less_than_eps(X1, X2):
  return sqrt((X2[0] - X1[0])**2 + (X2[1] - X1[1])**2) < const.eps


def check_bounds(x, x0, x1, interval):
  bounds = [interval['x1'][0], interval['x1'][1]]

  if x[0] <= bounds[0]:
    x[0] = bounds[0]
    x[1] = x0[1] + (x[0] - x0[0]) * (x1[1]-x0[1]) / (x1[0] - x0[0])
  if x[0] >= bounds[1]:
    x[0] = bounds[1]
    x[1] = x0[1] + (x[0] - x0[0]) * (x1[1]-x0[1]) / (x1[0] - x0[0])

  if x[1] <= bounds[0]:
    x[1] = bounds[0]
    x[0] = x0[0] + (x[1] - x0[1]) * (x1[0]-x0[0]) / (x1[1] - x0[1])
  if x[1] >= bounds[1]:
    x[1] = bounds[1]
    x[0] = x0[0] + (x[1] - x0[1]) * (x1[0]-x0[0]) / (x1[1] - x0[1])

  return x
