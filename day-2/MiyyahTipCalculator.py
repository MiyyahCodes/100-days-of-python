#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to Miyyah Tip Calculator!")

total_bill = float(input("What was the total bill?\n$"))

percentage_to_give = int(
    input("What percentage tip would you like to give? 10, 12 or 15?\n"))

num_of_people = int(input("How many people are to split the bill?\n"))

bill_percent_to_give = total_bill / 100 * percentage_to_give

bill_and_tip = total_bill + bill_percent_to_give

each_person_share = round(bill_and_tip / num_of_people , 2)

each_person_bill = f"Each person should pay: ${each_person_share}"

print(each_person_bill)
