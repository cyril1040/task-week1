full_name = input(" enter your full name: ").split()
age = int(input(" enter your age: "))
gender = input(" enter gender: ")
number = input(" enter phone number: ")
if age >= 18:
    print(full_name[0] + " welcome to our boutique" )

    our_products = {"bags": 80, "shirts": 100, "shoes": 40, "trousers": 80, "belts": 20, "underwears": 75, "cap": 10, "wrist_watch": 55}
    for key, values in our_products.items():
        print(key, values)
    total_cost = 0
    print(" 'done' to see the total")
    while True:
        a = input( " select an item to buy: ")
        if a.lower() in our_products:
            total_cost = total_cost + our_products[a]
        elif a.lower() == 'done':
            break
        else:
            print(" item is unavailable")
    print("the total cost of selected goods is ", str(total_cost))
    print(" thanks", full_name[1], "for patronising us")
else:
    print(" sorry you must be upto 18")






