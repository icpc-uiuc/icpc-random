# Ramdom Is The Best
import random
random.seed(2333)

def generate_int_with_range(low: int, high: int, count: int): # [low, high)
	assert low < high
	assert count > 0
	return [random.randint(low, high - 1) for _ in range(count)]


def get_random_permutation(n: int):
	permutation = [i for i in range(n)]
	random.shuffle(permutation)
	return permutation

def generate_random_tree(number_of_vertices: int):
	n = number_of_vertices
	assert n >= 2
	perm = get_random_permutation(n)
	edges = [(perm[0], perm[1])]
	for i in range(2, n):
		attach = random.randint(0, i - 1)
		edges.append((perm[attach], perm[i]))
	return edges


def generate_non_decreasing_sequence(low: int, high: int, n: int):
	seq = generate_int_with_range(low, high, n)
	seq = sorted(seq)
	return seq


# print(generate_int_with_range(0, 10, 100))
# print(generate_random_tree(6))
print(generate_non_decreasing_sequence(5, 20, 40))