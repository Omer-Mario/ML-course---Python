
balance = 999999
annualInterestRate = 0.18

epsilon = 0.001
monthlyInterestRate = annualInterestRate / 12.0
LowerBound = balance / 12
UpperBound = (balance * ((1 + monthlyInterestRate)**12)) / 12.0

while True:
    remaining_balance = balance
    payment = ( LowerBound + UpperBound ) / 2
    for i in range (12):
        unpaid = remaining_balance - payment 
        remaining_balance = unpaid + monthlyInterestRate * unpaid 
    if abs(remaining_balance) < epsilon:
        break
    elif remaining_balance > 0:
        LowerBound = payment
    elif remaining_balance < 0:
        UpperBound = payment 


print("Lowest Payment: " + str(round(payment, 2)))
        

