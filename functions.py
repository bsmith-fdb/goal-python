def print_something(something, some_other_thing):
    print(something, some_other_thing)


print_something("hey", "dude")

print_something(1, 2)


def add_two(num):
    return num + 2


result = add_two(6)
print(result)


def contact_card(name, age, car_model):  # <-- parameters
    print(name, age, car_model)


contact_card("ben", 21, "lexus")  # <-- arguments
contact_card(age=32, name="randy", car_model="honda")
contact_card("duke", car_model="humvee", age=68)


def can_drive(age, driving_age=16):  # default arguments
    return age >= driving_age


print(can_drive(21))
print(can_drive(9))


def funk():
    return print("hello from funk()")


funk()
