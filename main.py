import json
with open("expenses.json") as f:
    items = json.load(f)

    sum = 0
    pet_store_items = items['pet store']
    for item in pet_store_items:
        sum += item['price']
    
    print(sum)
