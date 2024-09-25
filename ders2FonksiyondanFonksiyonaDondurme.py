def usAlma(number):
    def inner(power):
        return number**power
    return inner

two=usAlma(2)
print(two(3))