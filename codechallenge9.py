loanamount = 1000
loanyears = 2
rate = 0.00256

remainingloan = loanamount
principal = loanamount / (loanyears * 12)

print("TASK #1")
print("Loan Amount: $", loanamount)
print("Loan Period:", loanyears, "years")

print("\nMonth | Payment | Interest | Principal | Remaining Loan")
print("----------------------------------------------------------")

for x in range(1, (loanyears * 12) + 1):
    interest = remainingloan * rate
    monthlypayment = principal + interest
    remainingloan = remainingloan - principal

    for y in range(1):
        print(f"{x} | ${monthlypayment:.2f} | ${interest:.2f} | ${principal:.2f} | ${remainingloan:.2f}")

# TASK 2
print("\nTASK #2\n")

for x in range(7):
    for y in range(13):
        if x == 6 or x + y == 6 or x == y - 6:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# TASK 3
print("\nTASK #3\n")

for x in range(5):
    for y in range(5):
        if x == 0 or x == 4 or x + y == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()