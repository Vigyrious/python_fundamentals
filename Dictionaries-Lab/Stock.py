elements = input().split(" ")
needed_products = input().split(" ")
bakery = {}

for i in range(0,len(elements),2):
    element = elements[i]
    key = int(elements[i+1])
    bakery[element] = key

for product in needed_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
