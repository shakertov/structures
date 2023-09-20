# Вам дана статистика по числу запросов в секунду к
# вашему любимому рекомендательному сервису.
# Измерения велись n секунд.
# В секунду i поступает qi запросов.
# Примените метод скользящего среднего с длиной
# окна k к этим данным и выведите результат.

from typing import List, Tuple


def read_input() -> Tuple[List[int], int, int]:
	num = int(input())
	array = list(map(int, list(input().strip().split())))
	window_size = int(input())

	return array, num, window_size

def moving_average() -> List[int]:
	result = []
	current_sum = sum(array[0:window_size])
	result.append(current_sum / window_size)

	for i in range(0, len(array) - window_size):
		current_sum -= array[i]
		current_sum += array[i + window_size]
		result.append(current_sum / window_size)

	return result


array, num, window_size = read_input()
print(*moving_average())
