eq = input("Give an equation. For example: 1 + 1 ")
eh = eq.split()
eq1 = eh[0]
eq2 = eh[1]
eq3 = eh[2]
eq1 = int(eq1)
eq3 = int(eq3)
ans = ""
#print(eq1)
#print(eq2)
#print(eq3)
if eq2 == "+":
  ans = eq1 + eq3
elif eq2 == "-":
  ans = eq1 - eq3
elif eq2 == "*":
  ans = eq1 * eq3
elif eq2 == "/":
  ans = eq1 / eq3
print(ans)
