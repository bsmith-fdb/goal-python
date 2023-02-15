def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step


print(gen_range(10))
print(list(gen_range(10)))
my_gen = gen_range(10)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
# print(next(my_gen))  # Error

for i in gen_range(20, start=13, step=2):
    print(i)


def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


gen = gen_fib()
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print([next(gen) for _ in range(50)][-1])


