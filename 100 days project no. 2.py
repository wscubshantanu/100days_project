print("welcome to the tip of calculator!")
bill = float(input("what was the total bill$"))
tip = int(input("what percentage tip would you like to give? 10 12 15"))
people = int(input("how many pepole spilt the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person, 2)
print(f"each person should pay: ${final_amount}")

