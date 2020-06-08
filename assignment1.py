# A program for loan calculations.
# The program prompts for the following: Total amount of loan, Annual interest rate (as a positive integer), and the total duration of loan in years.
# Output includes monthly payment and the loan balance and total amount paid each year.

def loan_info():

    def payment(principal, annual_interest_rate, duration):
        import math
        r = annual_interest_rate/100/12
        n = duration*12
        if r == 0:
            answer_payment = principal/n
        else:
            answer_payment = (principal*r*(1+r)**n)/((1+r)**n-1)
        return(answer_payment)
        
    def remaining_balance(principal, annual_interest_rate, duration , number_of_payments):
        r = annual_interest_rate/100/12
        n = duration*12
        p = number_of_payments
        if r==0:
            answer_remaining = pricipal*(1-p/n)
        else:
            answer_remaining = (principal*((1+r)**n-(1+r)**p))/((1+r)**n-1)
        return(answer_remaining)

    principle=float(input("Enter loan amount: "))
    annual_interest_rate=float(input("Enter annual interest rate (percent):"))
    duration=int(input("Enter loan duration in years: "))
    answer1 = payment(principle, annual_interest_rate, duration)
    print("LOAN AMOUNT:",principle, "INTEREST RATE (PERCENT):",annual_interest_rate)
    print("DURATION (YEARS):",duration, "MONTHLY PAYMENT:", int(answer1))
    for x in range(1, duration+1):
        answer2 = remaining_balance(principle, annual_interest_rate, duration, 12*x)
        print("YEAR:",x, "BALANCE:" ,int(answer2), "TOTAL PAYMENT", int(12*x*(answer1)))
       
loan_info()
