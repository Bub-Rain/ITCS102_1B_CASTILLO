money = eval(input("Money to deposit --->"))

dot = money // 1000
dofh = money % 1000 // 500
doth = money % 1000 % 500 // 200
donh = money % 1000 % 500 % 200 // 100
doft = money % 1000 % 500 % 200 % 100 // 50
dotw = money % 1000 % 500 % 200 % 100 % 50 // 20
dotn = money % 1000 % 500 % 200 % 100 % 50 % 20 // 10
dofv = money % 1000 % 500 % 200 % 100 % 50 % 20 % 10 // 5
done = money % 1000 % 500 % 200 % 100 % 50 % 20 % 10 % 5 // 1

print("1000 -", dot)
print("500 -", dofh)
print("200 -", doth)
print("100 -", donh)
print("50 -", doft)
print("20 -", dotw)
print("10 -", dotn)
print("5 -", dofv)
print("1 -", done)