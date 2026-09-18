# LOAN PROGRAM

age = int(input("Enter your age ---> "))
is_employed = bool(input("Are you employed? (True/Leave it blank) ---> "))
cred_score = eval(input("What is your credit score ---> "))
annual_income = eval(input("What is your annual income ---> "))

print("____________________________________________")

has_collateral = bool(input("Do you have any collateral ---> "))

if has_collateral == True:
    collateral_value = int(input("What is the value of your collateral ---> "))
else:
    collateral_value = 0

print("____________________________________________")

longevity = int(input("How many months to pay ---> "))

loan_amount = int(input("How much are you loaning ---> "))

print("____________________________________________")

if age >= 21 and is_employed == True:

    if cred_score >= 750:

        if annual_income >= 200000:
            int_rate_A = 0.75
        else:
            int_rate_A = 0.5

        int_rate_B = 0.15
        int_rate_C = 0.1

        int_rate_set1 = int_rate_A + int_rate_B

        if has_collateral == True:
            int_rate_set2 = int_rate_set1 - int_rate_C

            if collateral_value >= 100000:
                int_rate_set2 = int_rate_set2 - 0.05
        else:
            int_rate_set2 = int_rate_set1

        int_rate = int_rate_set2

        if longevity >= 48:
            int_rate = int_rate * 1.6

        elif longevity >= 36:
            int_rate = int_rate * 1.4

        elif longevity >= 24:
            int_rate = int_rate * 1.25

        elif longevity >= 18:
            int_rate = int_rate * 1.1

        elif longevity >= 12:
            int_rate = int_rate * 1

        elif longevity >= 6:
            int_rate = int_rate * 0.80

        else:
            int_rate = int_rate * 1.8

        if loan_amount >= 500000:
            int_rate = int_rate * 1.25

        elif loan_amount >= 100000:
            int_rate = int_rate * 1.05

        else:
            int_rate = int_rate * 0.95

        final_amount = loan_amount + (loan_amount * int_rate)

        print("Interest rate --->", int_rate * 100, "%")
        print("Loan amount --->", loan_amount)
        print("Final loan amount --->", final_amount)

    elif cred_score >= 600:
        print("Credit score is below 750.")

    else:
        print("Loan denied. Credit score too low.")

else:
    print("Loan denied. Must be 21 or older and employed.")
