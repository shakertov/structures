# затем Рита должна выбрать две фишки,
# сумма очков на которых равна заданному числу.
# Рите надоело искать фишки самой,
# и она решила применить свои навыки программирования
# для решения этой задачи. Помогите ей написать
# программу для поиска нужных фишек.

from typing import List, Tuple, Optional

def read_input() -> Tuple[List, int, int]:
	num = int(input())
	array = list(map(int, list(input().strip().split())))
	summ = int(input())

	return array, num, summ

def two_sum_with_sort() -> Tuple[int, int]:
	array.sort()

	left = 0
	right = len(array) - 1

	while left < right:
		current_sum = array[left] + array[right]
		if current_sum == summ:
			return array[left], array[right]
		if current_sum < summ:
			left += 1
		else:
			right -= 1

	return None



def print_result(result: Optional[Tuple[int, int]]):
	if result == None:
		print(None)
	else:
		print(' '.join(map(str, result)))

array, num, summ = read_input()
print_result(two_sum_with_sort())
