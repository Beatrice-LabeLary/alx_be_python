#promtping user to get data
monthlyIncome = input("Enter your monthly income: ")
monthlyExpenses = input("Enter your total monthly expenses: ")

#Calculions
monthlySavings = int(monthlyIncome) - int(monthlyExpenses)
projectedSavings = int(monthlySavings * 12 + (monthlySavings * 12 * 0.05))

#printing results
print("Your monthly savings are $", monthlySavings, ".")
print("Projected savings after one year, with interest, is: $", projectedSavings, ".")