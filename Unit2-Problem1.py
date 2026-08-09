balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12.0


for i in range (12):
    payment = balance * monthlyPaymentRate
    unpaid = balance - payment
    balance = unpaid + (annualInterestRate / 12) * unpaid

print("Remaining balance: " + str(round(balance, 2)))
