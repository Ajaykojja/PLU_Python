prices = [150, 200, 250, 300, 400]

print("Original Book Prices:", prices)

book = int(input("Enter the new book price: "))

found = False

for index in range(len(prices)):
    if book < prices[index]:
        prices.insert(index, book)
        found = True
        break

if found == False:
    prices.append(book)

print("Updated Book Prices:", prices)