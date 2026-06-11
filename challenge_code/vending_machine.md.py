# store input in a variable
# Amount due variable will be 50
#Create a while loop(while amount due is greater than 0)
#Prompt the user to insert a coin
# use a try except block to only accept values of 1,5,10,25
#validate the coin
#Algorithm: If it is validated as acceptable Amountdue-=input. Update the amount due
# any other cases will be handled by the except block(continue)
# Stop when the change owed becomes 0 or less than 0. Print Change Owed

def main():
        amount_due = 50
        valid = [1,5,10,25]
        print("Vending Machine ------\n")
        while(amount_due > 0):
              print(f"Amount due: {amount_due}")
              try: 
                   insert_coin = int(input("Insert Coin: "))
                   if insert_coin in valid:
                         amount_due-=insert_coin
              except:
                    continue
        print(f"Change Owed: {amount_due * -1}")
main()                    
              
                