# why use optionals if can just skip writing one of the args and the outcome will be the same?
def piece_of_cake(prices, optionals = [], **kwargs):
    acc = 0
    for key in kwargs:
        if key not in optionals:
            acc += (float(prices[key])/100.0) * kwargs[key]
    return acc

# version without optionals
def piece_of_cake_2(prices, **kwargs):
    acc = 0
    for key in kwargs:
        acc += (float(prices[key])/100.0) * kwargs[key]
    return acc

def main():
    print(piece_of_cake({'chocolate':18, 'milk':20}, optionals=['milk'], chocolate=100))
    print(piece_of_cake_2({'chocolate': 18, 'milk': 20}, chocolate=200))

if __name__ == '__main__':
    main()