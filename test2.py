stack_fruit = []
print("Welcome to the Fruit Basket Manager!")
while True:
    action = input ("Choose Add fruit(1), (remove fruit(2)), (View fruit:(3)), (Exit:(4)")
    if action == "1":
        fruit = input("add fruit:")
        stack_fruit.append(fruit)
        print(f"{fruit} added.")
    elif action == '2':
        if stack_fruit:
            print("Removed Fruit:", stack_fruit.pop())
        else:
            print("is empty!")
    elif action == '3':
        print("Fruits:",stack_fruit or "The basket is empty.")
    elif action == '4':
        print("Goodbye!") 
        break
    else:
        print("Invalid choice")   









