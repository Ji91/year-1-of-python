income = float(input("Enter the annual income: "))


if income < 85528:
    tax = (income * 0.18) - 556.2
    print(tax)
if income > 85528:
    tax = 14839.2 + (0.32 * (income - 85528))
    print(tax)

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

if tax < 0:
    print("The tax is therefore, 0.0 thalers")


