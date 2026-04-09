print("📚 Welcome to Student Result Checker 📚")

while True:
    name = input("\nEnter student name: ")
    score = int(input("Enter exam score: "))

    print("\n--- RESULT ---")

    if score >= 75:
        print(name + ", you got Excellent 🌟")
    elif score >= 50:
        print(name + ", you passed 👍")
    else:
        print(name + ", you failed, try again 💪")

    choice = input("\nCheck another student? (yes/no): ")
    if choice.lower() == "no":
        print("Goodbye 👋")
        break