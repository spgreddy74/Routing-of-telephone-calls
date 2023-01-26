def find_cheapest_operator(number, price_lists):
   
    cheapest_operator = None
    cheapest_price = float('inf')

    # Iterate through each price list
    for operator, prices in price_lists.items():
        # Iterate through each prefix in the price list
        for prefix in sorted(prices, key=lambda x: len(x), reverse=True):
            if number.startswith(prefix):
                price = prices[prefix]
                # Check if the current operator has a cheaper price than the previous
                if price < cheapest_price:
                    cheapest_operator = operator
                    cheapest_price = price
                break
    return cheapest_operator, cheapest_price

#usage:
price_lists = {
    'Operator A': {
        '1': 0.9,
        '268': 5.1,
        '46': 0.17,
        '4620': 0.0,
        '468': 0.15,
        '4631': 0.15,
        '4673': 0.9,
        '46732': 1.1
    },
    'Operator B': {
        '1': 0.92,
        '44': 0.5,
        '46': 0.2,
        '467': 1.0,
        '48': 1.2
    }
}

number = '46732123456'
cheapest_operator, cheapest_price = find_cheapest_operator(number, price_lists)
print(f'The cheapest operator for number {number} is {cheapest_operator} with a price of {cheapest_price} per minute.')
