balance = 4773
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
payment = 10

while True:
    remaining_balance = balance
    for i in range(12):
        unpaid = remaining_balance - payment
        remaining_balance = unpaid + monthlyInterestRate * unpaid
    if remaining_balance <= 0:
        break
    else:
        payment += 10

print("Lowest Payment: " + str(payment))
