
print("Welcome to the Zeze investment portal!")

print("Please input the info required to begin the process")

age = int(input("How old are you? - "))

print(age)

income = int(input("How much are you paid in GHS? - "))
#The issue in your code is in the way you are handling the income input. The print() function is used when displaying output,
# but it does not convert the input to an integer. 
# Additionally, you are trying to convert the result of print(income) to an integer, which won't work as print() returns None.
#incomeVal = int(print(income)) this is your code and it has been changed to the code on the next line
incomeVal = (income)

principal = int(input("How much are you willing to invest?(Investments start from GHS100 and above) - "))
#the print function has been cleared  principalVal = print(principal)


time = int(input('How long do you want to invest?(In years)  - '))
#the print function has been cleared #timeVal =print(time)
timeVal = (time)

print('Interest rate is 16% per annum')
interestRate = (0.16)

#finalAmount = (principalVal * (1 + (interestRate)) ^ (time)) the code has been corrected below
finalAmount = ((principal) * (1 + interestRate)**(time))
print(finalAmount)

print(f"The amount you will be making at the end of the time period is {finalAmount}")
	
