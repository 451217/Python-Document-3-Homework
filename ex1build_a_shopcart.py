# from IPython.display import clear_output #print('\n'100) in VS

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

# 1) Build a Shopping Cart
# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

# TO DO:
# First I need to define a function called shopping cart
# then I need to define an empty dictionary
# next create a while true flag variable
# create a while loop based on true flag variable:
    # next I need to ask the user if they want to see the shopping cart (dictionary),  
    # add an item, delete an item, or quit                                              --  INPUT
    # if user wants to see the cart
        #print cart/dictionary
    #if user wants to add to the cart
        #add item to the dictionary
    #if user wants to delete an item
        #delete item from dictionary0
    #if user quits
        #print cart/dictionary
        #use this statement to clear output --  print('\n'100)
        #break loop


def shopping_cart():
    cart_dict = {}
    shopping = True
    print("\n Hi, Thank you for visiting today.")
    while shopping:
        to_do = input("\n What would you like to do? 'add item', 'delete item', 'see cart', 'quit' ")

        if to_do == 'quit':
            print (f'Here is your list: {cart_dict}')
            pass #add clear output here - does not work in vs code
            print("\n Thank you for shopping with us! Have a great day  : )")
            break
        
        if to_do == 'add item':
            item_key = input("\nWhat would you like to add? ")
            item_value = input ("\nHow many would you like? ")
            cart_dict[item_key] = item_value

        if to_do == 'delete item':
            delete_key = input("\nWhat would you like to remove? ")
            del cart_dict[delete_key]
            print("\nItem was removed, cart is now:")
            print (f'\n {cart_dict}')

        if to_do == 'see cart':
            print (f'\n {cart_dict}')

shopping_cart()