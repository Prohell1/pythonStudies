def add(*args):
    print(args[1])

    sum_of_numbers = 0
    for n in args:
        sum_of_numbers += n
    return sum_of_numbers


# print(add(3, 5, 6, 2, 1))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan")
print(my_car.model)
