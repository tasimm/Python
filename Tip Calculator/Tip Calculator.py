print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 15, 18, or 20? "))

people = int(input("How many people are splitting the bill? "))

bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people

# format to ensure two decimal places are always present for dollar amounts
final_amount = "{:.2f}".format(bill_per_person)

print(f"Total bill with {tip}% tip: ${bill_with_tip}")
print(f"Bill per person: ${bill_per_person}")
