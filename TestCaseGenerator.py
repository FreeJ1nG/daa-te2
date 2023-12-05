from math import sqrt
import random


class TestCase:
  def __init__(self, n: int, S: list[set[int]], W: list[int]) -> None:
    self.n = n
    self.S = S
    self.W = W
    self.size = len(S)

  def __str__(self) -> str:
    return f'TestCase(m={self.size}, n={self.n}, S={self.S}, W={self.W})'


class TestCaseGenerator:
  def __init__(self, random_seed: int, sizes: list[int]) -> None:
    random.seed(random_seed)
    self.sizes = sizes
    self.testcases: list[TestCase] = []
    self.SUBSET_AMOUNT = 20
    self.MAX_W = 40

  def generate(self):
    for size in self.sizes:
      self._generate_single_case(size)

  def _generate_single_case(self, size: int):
    S = []
    W = []
    for _ in range(self.SUBSET_AMOUNT):
      S_i = set()
      set_size = random.randint(size // 2, size)
      for _ in range(set_size):
        S_i.add(random.randint(1, size))
      S.append(S_i)
      W.append(random.randint(1, self.MAX_W))
    self.testcases.append(TestCase(size, S, W))


tc_generator = TestCaseGenerator(42, [20, 200, 2000])
tc_generator.generate()
cases = tc_generator.testcases
for case in cases:
  print(case)
