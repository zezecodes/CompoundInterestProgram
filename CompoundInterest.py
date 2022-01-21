
print("Welcome to the Zeze investment portal!")

print("Please input the info required to begin the process")

age = int(input("How old are you? - "))

print(age)

income = int(input("How much are you paid in GHS? - "))

incomeVal = (print(income))

principal = int(input("How much are you willing to invest?(Investments start from GHS100 and above) - "))

principalVal = (print(principal))

time = int(input('How long do you want to invest?(In years)  - '))

timeVal = (print(time))

print('Interest rate is 16% per annum')
interestRate = float(0.16)

finalAmount = float(principalVal * (1 + (interestRate)) ^ (time))

print(finalAmount)

print("This how much you'll be making at the end of the time period")
	
