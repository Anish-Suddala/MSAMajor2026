#function to load data from a file and return a dictionary
#Input: filename
#Output: dictionary

def load_menu_items(filename:str) -> dict:
    #open menu.txt: create a file handler to open files in read mode
    data_file = open(filename,"r")
    print(data_file)

    #create an empty dictionary
    menu_items = {}
    #use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        item_name_and_price = line_of_data.split(",")
        #split the line at the comma
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])
        #get the item and price from the list
        #create an entry in the dictionary for the item and price
    #close the file
    menu_items[item_name] = item_price
        #get the item and price from the list
        #create an entry in the dictionary for the item and price
    #close the file
    data_file.close()
    return menu_items


def main():
    menu_items = load_menu_items("menu.txt")
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
        