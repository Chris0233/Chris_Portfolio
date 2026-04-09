print("🖩 Welcome to Chris's Calculator 🖩")

while True:
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    choice = input("Enter 1, 2, 3, 4, or 5: ")

    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result:", num1 * num2)
    elif choice == "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero")
    elif choice == "5":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice")