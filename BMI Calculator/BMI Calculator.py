# ask for inputs
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: ")) 

# calculate and round to nearest whole number
bmi = weight / (height * height)
bmi = round(bmi)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese")
else:
  print(f"Your BMI is {bmi}, you are clinically obese")
