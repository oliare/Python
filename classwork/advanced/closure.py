def outer():

    number = 1

    def inner():
        nonlocal number # get 'number' from outer scope
        print(number)
        number += 1

    return inner

calculate = outer()

calculate()
calculate()
calculate()