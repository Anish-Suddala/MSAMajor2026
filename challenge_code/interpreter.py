#While Loop
#INPUT
# prompt the user to enter the expression

# PROCESS
# Validate the expression format
    # Use the split method to split the expression at the space
    # If the length of the resulting list is not 3 then invalid format
# Validate that X and Z are integers
    # convert to int.
    # if converting causes an exception, then incorrecty format 
# Validate that Y is an acceptable operator (+,-,*,/)
    #use an If statement to determine if Y == (+,-,*,/)
    #invalid format if not
# Validate that when Y is /, Z is not 0
#   Use IF: if U == "/" and Z == 0: divide by zero error
# Do the math

# OUTPUT
# Print the output to user


def math_calculations():
    while(True):
        user_input = input("Enter the expression in X y Z format: ")
        user_input_split = user_input.split(" ")
        if(len(user_input_split) != 3):
            print("Error: Invalid Format")
            continue
        try:
            x = int(user_input_split[0])
            z = int(user_input_split[2])
        except:
            print("Error: Invalid Format")
            continue
        valid = {"+","-","*","/"}
        y = user_input_split[1]
        if y not in valid:
            print("Error: Invalid Format")
            continue
        if (y == "/" and z == 0):
            print("Error: Divide By 0 Error ")
            continue
        result = [x, y, z] 
        break
    return result

def main():
    while True:
        user_input_split = math_calculations()
        if(user_input_split[1] == "+"):
            result = user_input_split[0] + user_input_split[2]
        elif(user_input_split[1] == "-"):
            result = user_input_split[0] - user_input_split[2]
        elif(user_input_split[1] == "*"):
            result = user_input_split[0] * user_input_split[2]
        else:
            result = user_input_split[0] / user_input_split[2]
        print(result)
        
        play_again = input("Would you like to enter a new expression(y/n):" )
        if(play_again != "y"):
            break

main()

            
