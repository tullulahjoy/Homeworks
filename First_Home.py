total_cost = float(input("What is the total cost of your dream home?"))
deposit_ambition = float(input("What size deposit are you aiming for? 10 or 20%? (enter as a decimal)"))

if deposit_ambition >= 1:
  deposit_ambition = float(input("Sorry, I need that as a decimal:"))

deposit = total_cost*deposit_ambition
print("With that deposit, you want to save",deposit)

current_savings = 0
r = 0.025
monthly_takehome = float(input("How much do you take home each month?"))
portion_saved = float(input("And how much of that will you save towards the deposit?"))
savings_return = current_savings*(r/12)

if portion_saved < monthly_takehome*0.05:
  portion_saved = float(input("Haha, you joker! Seriously, how much of that will you save towards the deposit?"))

months_to_save = 0
int(float(months_to_save))

while current_savings < deposit:
  current_savings += portion_saved+savings_return
  months_to_save += 1

print("It will take you",months_to_save,"months to save for this house. That's",round(months_to_save/12,2),"years.")
months_to_save = 0
current_savings = 0
answer = (str(input("Are you using a savings scheme with a 25% Government bonus?")))
if answer in ['n','no','N','No']:
  print("Ah, nevermind then.")
elif answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
  while current_savings < (deposit*0.75):
    current_savings += portion_saved+savings_return
    months_to_save += 1
    #print(months_to_save,"months")
print("With a bonus of 25%, it will take you",months_to_save,"months to save for this house. That's",round(months_to_save/12,2),"years.")
  
  
  
  
