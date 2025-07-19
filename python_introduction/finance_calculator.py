#promtping user to get data
monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")

#Calculions
monthly_savings = int(monthly_income) - int(monthly_expenses)
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

#printing results
print("Your monthly savings are $", monthly_savings, ".")
print("Projected savings after one year, with interest, is: $", projected_savings, ".")