product = [102, 107, 209, 127, 567, 765, 988]
search_id = int(input("Enter the product ID to search: "))
low = 0
high = len(product) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if product[mid] == search_id:
        found = True
        print(f"Product Found at index: {mid}")
        break
    elif product[mid] < search_id:
        low = mid + 1
    else:
        high = mid - 1
        
if not found:
    print("Product Not Available.")