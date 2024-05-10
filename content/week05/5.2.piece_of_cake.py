
def piece_of_cake(prices, **quantities):
    optionals = quantities.pop('optionals', [])
    
    total_price = 0
    for ingredient, quantity in quantities.items():
        if ingredient not in optionals and ingredient in prices:
            total_price += (quantity / 100) * prices[ingredient]
    
    return total_price

def test_get_recipe_price():
    assert piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100) == 44
    assert piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300) == 54
    assert piece_of_cake({}) == 0
    
    print('All tests passed!')

if __name__ == '__main__':
    test_get_recipe_price()