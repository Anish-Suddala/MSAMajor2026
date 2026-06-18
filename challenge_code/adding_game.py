import random
def game_level():
    while(True):
            valid_level = {"1","2","3"}
            user_input = input("Enter Level 1, 2, 3: ")
            while user_input not in valid_level:
                print("Invalid Input")
                user_input = input("Enter Level 1, 2, 3: ")
            return user_input


def num_of_questions():
    questions = 0
    while(True):
            valid_range = {"3","4","5","6","7","8","9","10"}
            user_input = input("Enter number of questions to ask: ")
            while user_input not in valid_range:
                print("ERROR: Please enter an integer value between 3 and 10! ")
                user_input = input("Enter number of questions to ask(3-10): ")
            return user_input







def main():
    difficulty = game_level()
    num_questions = num_of_questions()
    random_generator = random.Random()
    score = 0
    
    for i in range(int(num_questions)): 
        attempts = 0
        attempting = True
        if (difficulty == "1"):
            x = random_generator.randint(0,9)
            y = random_generator.randint(0,9)
        elif (difficulty == "2"):
            x = random_generator.randint(10,99)
            y = random_generator.randint(10,99)
        elif (difficulty == "3"):
            x = random_generator.randint(100,999)
            y = random_generator.randint(100,999)
        while (attempts < 3 and attempting):
            user_input = input(f"{x} + {y} = ")
            if (user_input == str(x + y)):
                print("CORRECT")
                score+=1
                attempting = False

            else:
                 print("WRONG")
                 attempts+=1
            x = int(x)
            y = int(y)
        print(f"The correct answer is {x+y}. ")
        
    print(f"You got {score} out of {num_questions} correct: {100*(score/int(num_questions)):.2f}%")
        
            

main()
main()
