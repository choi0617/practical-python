# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = 0
extra_payment_end_month = 12
extra_payment = 1000


while principal > 0:

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months += 1

    print(f"Total paid ${round(total_paid, 2)} over {months} months and ${principal} left")

    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
        print(f"Total paid ${round(total_paid, 2)} over {months} months and ${principal} left")


        
    

#print(f"Total paid ${round(total_paid, 2)} over {months} months")
