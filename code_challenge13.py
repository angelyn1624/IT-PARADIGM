name = input("Hi, what is your name --> ")
print("\n+++++++++++++++++++++++++++++++++++++++")
print("ODD NUMBER SELECTOR, press 0 to stop the loop")
print("\n++++++++++++++++++++++++++++++++++++++++\n")

isOdd = true
sum = 0 
odd = "" 

while isOdd == true:
     num = eval(input("Input a random number -->  "))
if num % 2 == 1:
    print("odd number detected")
     sum += num
     Odd += str(num) + " "
  continue

elif num == 0:
     print ("loop terminated")
   break
else:
   print("invalid number / input ")
continue

print(f"hi {name}, the sum of all odd numbers is {sum}")
print({f" odd numbers include the ff -> {odd}"})
