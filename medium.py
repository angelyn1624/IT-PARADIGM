col = eval(input("Input a number in a column. ", ))

for a in range(1,11,1):
  for j in range(1, col + 1,1):
    print(f"{a}x{j}={a*j}", end="\t\t")
  print()



for b in range(1, 6, 1):
  for c in range(6, b, -1):
    print(" ", end="")
  for d in range(1, b +1, 1):
    print("* " , end="")
  print()
