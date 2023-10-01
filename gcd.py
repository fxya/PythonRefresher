def gcd(a, b):
    if b == 0:
        return a
    else:
        print(f'{a} = {a // b} * ({b}) + {a % b}')
        return gcd(b, a % b)


if __name__ == '__main__':
    print(gcd(234, 66))