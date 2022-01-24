import graphs as graph
import tables as table
from functions import *
from methods import *


def main():
  table.AnalyticData()

  xs1 = HookeJeeves(f1, const.x0, const.interval)
  xs2 = HookeJeeves(f2, const.x0, const.interval)

  table.ResultData(xs1, xs2)
  table.FunctionData(f1, xs1, name='Function 1')
  table.FunctionData(f2, xs2, name='Function 2')

  graph.Xk(xs1)
  graph.Xk(xs2)

  graph.Xs(xs1, func_num=1, name='Function 1')
  graph.Xs(xs2, func_num=2, name='Function 2')

  graph.Fk(f1, xs1, f2, xs2)

  graph.FunctionLevelRoute(f1, xs1, name='Function 1')
  graph.FunctionK(f1, xs1, func_num=1, name='Function 1')

  graph.FunctionLevelRoute(f2, xs2, name='Function 2')
  graph.FunctionK(f2, xs2, func_num=2, name='Function 2')


if __name__ == '__main__':
  main()
