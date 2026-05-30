print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Currency Converter")

choice = int(input("Enter choice: "))

if choice == 1:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print("Result =", a + b)

elif choice == 2:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print("Result =", a - b)

elif choice == 3:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print("Result =", a * b)

elif choice == 4:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print("Result =", a / b)

elif choice == 5:

    print("Available Currencies:")
    print("BDT = Bangladeshi Taka")
    print("USD = US Dollar")
    print("GBP = British Pound")
    print("INR = Indian Rupee")
    print("AED = UAE Dirham")

    from_currency = input("From: ").upper()
    to_currency = input("To: ").upper()

    amount = float(input("Enter amount: "))

    rates = {
        "BDT": 1,
        "USD": 122,
        "GBP": 165,
        "INR": 1.43,
        "AED": 33
    }

    bdt_amount = amount * rates[from_currency]
    converted_amount = bdt_amount / rates[to_currency]

    print("Converted Amount =", converted_amount)

else:
    print("Invalid Choice")
