n = 3

def recurse(n):
	if n == 0:
		return 1

	if n < 0:
		return 0

	step1 = recurse(n-1)
	step2 = recurse(n-2)

	return step1 + step2

res = recurse(n)
print(res)