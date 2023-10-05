# Import the datetime module to work with dates and times
from datetime import datetime

# Get the user's name as input
name = input("Enter your name:")

# Define a list of items with their prices
lists = """
Rice     Rs 20/kg
Sugar    Rs 30/kg
Salt     Rs 20/kg
Oil      Rs 80/liter
Lays     Rs 20/each
Maggi    Rs 50/kg
Boost    Rs 90/each
Honey    Rs 399/kg
"""

# Initialize variables to keep track of the total price and the final price
totalprice = 0
finalprice = 0

# Create an empty list to store the selected items and their details
item_list = []

# Create a dictionary called 'items' to store the prices of items
items = {
    'Rice': 20, 'Sugar': 30, 'Salt': 20,
    'Oil': 80, 'Lays': 20,
    'Maggi': 50, 'Boost': 90, 'Honey': 399
}

# Ask the user for an option
options = int(input("For a list of items, press 1: "))

# Check the user's choice
if options == 1:
    # Display the list of items
    print(lists)

# Initialize a serial number
sno = 0

# Start an infinite loop to allow the user to select items
while True:
    # Ask the user if they want to buy an item or exit
    inp1 = int(input("If you want to buy, press 1 or press 2 to exit: "))

    # Check the user's choice
    if inp1 == 2:
        # Exit the loop and end the program
        print("Thanks for your time")
        break
    elif inp1 == 1:
        # The user wants to buy an item

        # Ask for the item name
        item = input("Enter your items: ").capitalize()

        # Ask for the quantity
        quantity = int(input("Enter quantity: "))

        # Check if the item is in the 'items' dictionary
        if item in items.keys():
            # Calculate the price for the selected item and quantity
            price = quantity * items[item]

            sno += 1

            # Add the item details to the 'item_list' and update total price
            item_list.append((sno, item, quantity, price))
            totalprice += price

            # Calculate GST (Goods and Services Tax)
            gst = (totalprice * 5) / 100

            # Calculate the final amount to be paid
            finalamount = gst + totalprice
        else:
            # Item not found in the dictionary
            print("Sorry, the item you entered is not available")

        # Ask if the user wants to proceed with billing
        inp = input("Can I bill the items? (yes or no): ")

        if inp == "yes":
            # User wants to proceed with billing

            # Check if there are items to be billed
            if finalamount != 0:
                # Print the bill details
                print(40 * "=", "Jaideep Supermarket", 40 * "=")
                print(42 * " ", "Narsipatnam", 40 * " ")
                print(name, 60 * " ", "Date:", datetime.now())
                print(100 * "-")
                print("s.no", 3 * "\t", "items", 4 * "\t", "Quantity", 2 * "\t", "Price")
                for sno, item, quantity, price in item_list:
                    print(sno, 4 * "\t", item, 4 * "\t", quantity, 4 * "\t", price)
                print(100 * "-")
                print(10 * "\t", "Total Amount: ", totalprice)
                print(10 * "\t", "GST: ", gst)
                print(100 * "-")
                print(10 * "\t", "Final Amount: ", finalamount)
                print(100 * "-")
                print(30 * " ", "Thanks for Shopping")
                print(100 * "-")
                print()
        elif inp== "no":
            # User does not want to proceed with billing, continue the loop
            pass
        else:
            # User entered an invalid input
            print("You have entered the wrong input")
    else:
        # User chose to exit without making a purchase
        print("Thanks for your time")
        pass


# ******Output*******
# Enter your name:Jai
# For a list of items, press 1: 1
#
# Rice     Rs 20/kg
# Sugar    Rs 30/kg
# Salt     Rs 20/kg
# Oil      Rs 80/liter
# Lays     Rs 20/each
# Maggi    Rs 50/kg
# Boost    Rs 90/each
# Honey    Rs 399/kg
#
# If you want to buy, press 1 or press 2 to exit: 1
# Enter your items: rice
# Enter quantity: 3
# Can I bill the items? (yes or no): no
# If you want to buy, press 1 or press 2 to exit: 1
# Enter your items: lays
# Enter quantity: 5
# Can I bill the items? (yes or no): no
# If you want to buy, press 1 or press 2 to exit: 1
# Enter your items: honey
# Enter quantity: 1
# Can I bill the items? (yes or no): no
# If you want to buy, press 1 or press 2 to exit: 1
# Enter your items: salt
# Enter quantity: 2
# Can I bill the items? (yes or no): no
# If you want to buy, press 1 or press 2 to exit: 1
# Enter your items: maggi
# Enter quantity: 2
# Can I bill the items? (yes or no): yes
# ======================================== Jaideep Supermarket ========================================
#                                            Narsipatnam
# Jai                                                              Date: 2023-09-08 19:22:04.657305
# ----------------------------------------------------------------------------------------------------
# s.no 			 items 				 Quantity 		 Price
# 1 				 Rice 				 3 				 60
# 2 				 Lays 				 5 				 100
# 3 				 Honey 				 1 				 399
# 4 				 Salt 				 2 				 40
# 5 				 Maggi 				 2 				 100
# ----------------------------------------------------------------------------------------------------
# 										 Total Amount:  699
# 										 GST:  34.95
# ----------------------------------------------------------------------------------------------------
# 										 Final Amount:  733.95
# ----------------------------------------------------------------------------------------------------
#                                Thanks for Shopping
# ----------------------------------------------------------------------------------------------------
