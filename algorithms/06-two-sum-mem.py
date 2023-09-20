# Рита и Гоша играют в игру.
# У Риты есть n фишек, на каждой из которых
# написано количество очков. Сначала Гоша называет число k,
# затем Рита должна выбрать две фишки,
# сумма очков на которых равна заданному числу.
# Рите надоело искать фишки самой,
# и она решила применить свои навыки программирования
# для решения этой задачи. Помогите ей написать
# программу для поиска нужных фишек.

from typing import List, Tuple, Optional


def read_input() -> Tuple[list, int, int]:
	num = int(input())
	array = list(map(int, list(input().strip().split())))
	summ = int(input())

	return array, num, summ

def two_sum_with_mem() -> Optional[Tuple[int, int]]:
	buff = set()

	for number in array:
		difference = summ - number
		if number in buff:
			return number, difference
		else:
			buff.add(difference)
	return None

def print_result(result: Optional[Tuple[int, int]]):
	if result == None:
		print(None)
	else:
		print(' '.join(map(str, result)))

array, num, summ = read_input()
print_result(two_sum_with_mem())
