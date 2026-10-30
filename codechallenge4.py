# SMALL BUSINESS LOANING SYSTEM

Owner_name = input("Enter the owner's name ---> ")
Owner_age = int(input("Enter the owner's age ---> "))

Has_business = bool(input("Do you have a business? (True/Leave it blank) ---> "))

if Has_business == True:

    Years_in_business = int(input("How many years have you been in business? ---> "))

    if Years_in_business >= 2:

        Monthly_revenue = int(input("What is your monthly revenue? ---> "))
        Annual_revenue = Monthly_revenue * 12

        Has_defaults = int(input("Do you have any outstanding debts/loans? (1 = Yes, 0 = No) ---> "))

        Collateral_name = input("What is your collateral? ---> ")
        Collateral_value = int(input("What is the value of your collateral ---> "))

        cred_score = int(input("What is your credit score? ---> "))

        print("____________________________________________")

        # TIER 1: ANNUAL REVENUE

        if Annual_revenue >= 500000:

            Max_loan_limit = Annual_revenue * 3
            Base_fee_rate1 = 0.015

        else:

            Max_loan_limit = Annual_revenue * 3
            Base_fee_rate1 = 0.3


        # 5000 DIVISIBILITY FEE

        if Max_loan_limit % 5000 != 0:
            Max_loan_limit = Max_loan_limit + 250


        # TIER 2: COLLATERAL

        if Collateral_value >= 3 * Monthly_revenue:

            Base_fee_rate2 = 0.02

        else:

            Base_fee_rate2 = 0.035


        # TIER 3: BUSINESS AGE

        if Years_in_business >= 5:

            Base_fee_rate3 = 0.015

        else:

            Base_fee_rate3 = 0.025


        # COMBINE BASE FEE RATE

        Base_fee_rate = Base_fee_rate1 + Base_fee_rate2 + Base_fee_rate3


        # TIER 4: CREDIT SCORE

        if cred_score < 620:

            print("Access Denied: Inevitable")

        else:

            print("Loan assessment passed.")

            print("____________________________________________")

            print("Owner name --->", Owner_name)
            print("Owner age --->", Owner_age)
            print("Years in business --->", Years_in_business)
            print("Monthly revenue --->", Monthly_revenue)
            print("Annual revenue --->", Annual_revenue)
            print("Outstanding debts/loans --->", Has_defaults)
            print("Collateral --->", Collateral_name)
            print("Collateral value --->", Collateral_value)
            print("Credit score --->", cred_score)

            print("____________________________________________")

            print("Maximum loan limit --->", Max_loan_limit)
            print("Base fee rate --->", Base_fee_rate * 100, "%")

            # LOAN SYSTEM

            loan_amount = int(input("How much are you loaning ---> "))

            if loan_amount <= Max_loan_limit:

                longevity = int(input("How many months to pay ---> "))

                int_rate = Base_fee_rate


                # PAYMENT LONGEVITY

                if longevity >= 60:

                    int_rate = int_rate * 1.8

                elif longevity >= 48:

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


                # LOAN AMOUNT ADJUSTMENT

                if loan_amount >= 500000:

                    int_rate = int_rate * 1.25

                elif loan_amount >= 100000:

                    int_rate = int_rate * 1.05

                else:

                    int_rate = int_rate * 0.95


                # OUTSTANDING DEBT ADJUSTMENT

                if Has_defaults == 1:

                    int_rate = int_rate * 1.15


                # FINAL LOAN AMOUNT

                final_amount = loan_amount + (loan_amount * int_rate)

                print("____________________________________________")

                print("Approved loan amount --->", loan_amount)
                print("Interest/fee rate --->", int_rate * 100, "%")
                print("Final loan amount --->", final_amount)

            else:

                print("Loan denied. Amount exceeds maximum loan limit.")

    else:

        print("Loan denied. Business must be at least 2 years old.")

else:

    print("Loan denied. Applicant must have a business.")