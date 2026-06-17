def main():
    #open menu.txt: create a file handler to open files in read mode
    data_file = open("menu.txt","r")
    print(data_file)

    #create an empty dictionary
    menu_items = {}
    #use a loop to read the contents of the file line by line
    for line_of_data in data_file:        
        item_name_and_price = line_of_data.split(",")
        print(line_of_data)

        #split the line at the comma
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])

        #get the item and price from the list
        #create an entry in the dictionary for the item and price
    #close the file
    menu_items[item_name] = item_price
    data_file.close()
    for items,price in menu_items.items():
        print(f"{items}: ${price}")
main()