def calculator():
    print("Welcome to the Simple Calculator!")

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter numeric values.")
            continue

        print("\nChoose an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            result = num1 + num2
            op = '+'
        elif choice == '2':
            result = num1 - num2
            op = '-'
        elif choice == '3':
            result = num1 * num2
            op = '*'
        elif choice == '4':
            if num2 == 0:
                print("❌ Error: Cannot divide by zero!")
                continue
            result = num1 / num2
            op = '/'
        else:
            print("❌ Invalid operation choice.")
            continue

        print(f"✅ Result: {num1} {op} {num2} = {result}")

        # Ask if user wants to continue
        again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("👋 Exiting calculator. Goodbye!")
            break

# Run the calculator
calculator()
