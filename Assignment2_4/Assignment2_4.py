# START
#   PROMPT enter salary
#   PROMPT enter number of dependents
#   CALCULATE Statetax as 6.5% of salary
#   CALCULATE federalTax as 28.0% of salary
#   CALCULATE dependentDeduction as 2.5% of salary per dependent
#   CALCULATE totalWithholding as stateTax + federalTax + dependentDeduction
#   CALCULATE takeHomePay as salary - totalWithholding
#   PRINT stateTax, federalTax, dependents, salary, and takeHomePay
# END

# input statements
salary = float(input("Enter your salary: "))
numDependents = float(input("Enter number of dependents: "))

# calculate taxes here
stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = salary * 0.025 * numDependents
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding 

# output statements
print("state Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take-Home Pay: $" + str(takeHomePay))
