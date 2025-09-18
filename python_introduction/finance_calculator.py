num1 = int(input("Enter your monthly income: "))
num2 = int(input("Enter your total monthly expenses: "))
monthly_savings = num1 - num2
projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print("Your monthly savings are ", monthly_savings)
print("projected savings after one year, with interest, is: ", projected_savings)