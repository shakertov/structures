# Даны два массива чисел длины n.
# Составьте из них один массив длины 2n,
# в котором числа из входных массивов чередуются
# (первый — второй — первый — второй — ...).
# При этом относительный порядок следования чисел из
# одного массива должен быть сохранён.

from typing import List, Tuple


def read_input() -> (Tuple[List[int], List[int]], int):
	num = int(input())
	list_1 = list(map(int, list(input().strip().split())))
	list_2 = list(map(int, list(input().strip().split())))

	return list_1, list_2, num

def zipper():
	zip_list = []
	for i in range(0, num):
		zip_list.append(list_1[i])
		zip_list.append(list_2[i])
	return zip_list

list_1, list_2, num = read_input()
print(*zipper())
