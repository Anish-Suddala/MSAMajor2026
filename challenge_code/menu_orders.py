def main():
    menu = {"Baja Taco": 4.00, 
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00} 
    lower_case_dict = {k.lower(): v for k, v in menu.items()}
    price = 0
    user_input = ""
    break_statement = "end"
    while(user_input.lower()!="end"):
        try:
            user_input = input("Item: ")
            if user_input in menu.keys() or user_input.lower() in lower_case_dict:
                price+=menu[user_input]
                print(f"Total: ${price:.2f}")
        except:
            if(user_input.lower() == break_statement):
                break
            continue

main()
        