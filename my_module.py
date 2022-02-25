def sum(a, b):
    return a + b


def multiply(a, b):
    return a * b


# TODO: example with args and kwargs

def main(a, b):
    print(f'Sum: 3 + 3 = {sum(a, b)}')
    print(f'multiplication: 3 + 3 = {multiply(a, b)}')


if __name__ == '__main__':
    try:
        a, b = 'a', 3
        main(a, b)
    except TypeError as err:
        print(err)
        a, b = 3, 3
        main(a, b)
