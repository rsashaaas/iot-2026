numbers = [9, 5, 10, 2, 24, -1, -48]


def adjacentElementsProduct(numbers ):
    max_product = numbers[0] * numbers[1]

    for i in range(1, len(numbers) - 1):
        product = numbers[i] * numbers[i + 1]

        if product > max_product:
            max_product = product

    return max_product

#hello

result = adjacentElementsProduct(numbers)

print("Початковий список:", numbers)
print("Максимальний добуток:", result)