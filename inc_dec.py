def increment(value):
    return value + 1

def decrement(value):
    return value - 1

if __name__ == "__main__":
    x = 10
    print(f"{x} incrémenté de 1 est {increment(x)}")
    print(f"{x} décrémenté de 1 est {decrement(x)}")