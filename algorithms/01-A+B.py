# Считайте и сложите два числа.
# Результат необходимо вывести на стандартный поток вывода
# или в файл, указанный в условии задачи.

from typing import Tuple


def read_input() -> Tuple[int, int]:
	a = int(input())
	b = int(input())
	return a, b

def get_sum() -> int:
	summ = a + b
	return summ

a, b = read_input()
print(get_sum())
