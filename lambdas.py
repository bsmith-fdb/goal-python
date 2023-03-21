from functools import reduce

# traditional function
def square(num):
    return num * num


square_lambda = lambda num: num * num

assert square(4) == square_lambda(4)


domain = [1, 2, 3, 4, 5]

our_range = map(lambda num: num * 2, domain)
print(list(our_range))

evens = filter(lambda num: num & 0x1 == 0x0, domain)
print(list(evens))

the_sum = reduce(lambda acc, num: acc + num, domain, 0)
print(the_sum)

words = ['Boss', 'a', 'Alfred', 'fig', 'Daemon', 'dig']
print("Sorting by default: ")
print(sorted(words))

print("Sorting by lambda key")
print(sorted(words, key=lambda s: s.lower()))

print("Sorting with a method")
words.sort(key=str.lower)  # sort in place
print(words)

print("Sorting in reverse")
words.sort(key=str.lower, reverse=True)
print(words)
