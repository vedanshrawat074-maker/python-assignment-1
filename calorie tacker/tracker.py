# Vedansh Rawat 03/11/2025 Building A Calorie Tracking console Application
from datetime import datetime
print("Welcome to the Calorie Tracker!\nYou can log your meals and view your total calorie intake for the day.")
meals=[] # a list to store meal names
calories=[] # a lsit to store calorie intake
number_of_meals=int(input('enter the number of meals you want to enter:'))
for i in range(number_of_meals): 
    meal=input('enter the meal name:')
    calorie=float(input('enter the calorie intake from this meal:'))
    meals.append(meal) # adding meal name to the list
    calories.append(calorie) # adding calorie intake to the list
total_calories=sum(calories) # calculating total calorie intake
if number_of_meals>0:# to avoid division by zero error
    average_calories= total_calories/number_of_meals
else:
    average_calories=0
calorie_limit=int(input('enter your daily calorie limit:'))
if total_calories>calorie_limit: # checking if user has exceeded their calorie limit
    exceeded=total_calories-calorie_limit
    print('you have exceeded your daily calorie limit! by',exceeded,'calories!!!!')
else:
    remaining=calorie_limit-total_calories
    print('congralutions!! you are within your daily calorie limit! you can still consume',remaining,'calories today.')   
print("\n---------- Meal Summary ----------") # printing a formatted summary
print(f"{'Meal':<20} | {'Calories'}")
print("-" * 32)
for i in range(number_of_meals):
    print(f"{meals[i]:<20} | {calories[i]:>9.2f}")
print("-" * 32)
print(f"{'Total:':<20} | {total_calories:>9.2f}")
print(f"{'Average:':<20} | {average_calories:>9.2f}")
print("--------------------------------\n")
print("Thank you for using the Calorie Tracker. Stay healthy!")
save=input(print('do you want to save this report? (yes/no):')).lower()
if save == "yes":
    with open ('data.txt','w') as file:
        current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"---------- Meal Summary{current_time} ----------\n")
        file.write(f"{'Meal':<20} | {'Calories'}\n")
        file.write("-" * 32 +'\n')
        for i in range(number_of_meals):
            file.write(f"{meals[i]:<20} | {calories[i]:>9.2f}\n")
        file.write("-" * 32 +'\n')
        file.write(f"{'Total:':<20} | {total_calories:>9.2f}\n")
        file.write(f"{'Average:':<20} | {average_calories:>9.2f}\n")
        file.write("--------------------------------\n")


