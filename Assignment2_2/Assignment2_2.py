# This program calculates your age in the year 2050.
# Input:  None
# Output: Your current age followed by your age in 2050

# Create your variables here

BEGIN
    Set currentYear = 2024
    Set myCurrentAge =25
END

myNewAge = myCurrentAge + (2050 - currentYear)
print("My Current Age is " + str(myCurrentAge))
print("I will be " + str(myNewAge) + " in 2050.")