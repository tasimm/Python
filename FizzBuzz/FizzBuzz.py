target = 100

for number in range(1, target + 1): #add 1 to include 100 in the range
  if number % 3 == 0 and number  % 5 == 0:
    print("FizzBuzz")

  elif number % 3 == 0:
    print("Fizz")

  elif number % 5 == 0:
    print("Buzz")

  else:
    print(number)
