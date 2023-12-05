from BranchAndBound import main as runBranchAndBound
from Greedy import main as runGreedy
from TestCaseGenerator import TestCaseGenerator, TestCase


class Runner:
  def __init__(self) -> None:
    self.tc_generator = TestCaseGenerator(42, [20, 200, 2000])
    self.tc_generator.generate()

  def run(self):
    for case in self.tc_generator.testcases:
      print(f'Running case with size of {case.n} ...')
      print("Running Greedy algorithm ...")
      runGreedy(case.n, case.S, case.W)
      print("Running Branch And Bound algorithm ...")
      runBranchAndBound(case.n, case.S, case.W)
      print("Case finished :D")
      print("========================================================================")


runner = Runner()
runner.run()
