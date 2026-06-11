#Create a decision structure to determine the season: 
# winter, spring, summer, fall
# Ask the user to enter the number of the month. Month must be 1-12
# Output the season
# winter:12,1,2 | spring:3,4,5 | summer: 6,7,8 | fall: 9,10,11
# Enter month number: 11
# Output: It is winter
def main():
    while(True):
        try:
            user_input = int(input("Enter the number of the month: "))
            if user_input < 1:
                print("Error: Month too small")
                continue
            elif user_input == 12 or user_input == 1 or user_input == 2:
                print(f"The season of month {user_input} is winter")
            elif(user_input == 3 or user_input == 4 or user_input == 5):
                print(f"The season of month {user_input} is spring")
            elif(user_input == 6 or user_input == 7 or user_input == 8):
                print(f"The season of month {user_input} is summer")
            elif(user_input == 9 or user_input == 10 or user_input == 11):
                print(f"The season of month {user_input} is fall")
            else:
                print("Error: Month too big")
                continue
            
        except:
            print("Error: Please enter a number between 1 and 12 \n")
            continue
        return user_input
main()


