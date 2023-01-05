# Thank you for pointing out the TypeError in the product adding function
# this has now been corrected.

# === Packages ===
from tabulate import tabulate
from operator import itemgetter


# === Classes ===
class Shoes:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_name(self):
        return self.product

    def get_code(self):
        return self.code

    def get_cost(self):
        return int(self.cost)

    def get_quantity(self):
        return int(self.quantity)

    def __str__(self):
        return [str(self.country), str(self.code), str(self.product), str(self.cost), str(self.quantity)]


# === Functions ===
def read_shoes_data():
    """Reads inventory.txt file and returns the contents as a list of objects"""
    file_input = []
    with open("inventory.txt", "r") as file:
        for line in file:
            file_input.append(line.strip("\n").split(","))
    object_list = []
    object_name_dict = {}
    skip_line = True
    for item in file_input:
        if skip_line:
            skip_line = False
        else:
            item_ref = item[2].lower().replace(" ", "_")
            object_name_dict[str(item_ref)] = Shoes(item[0], item[1], item[2], item[3], item[4])
            object_list.append(object_name_dict[item_ref])
    return object_list


def capture_shoes(inventory):
    """Allows user to enter in details for a new product then writes it to inventory.txt"""
    user_confirm = False
    while not user_confirm:
        shoe_product = duplicate_checker("name", inventory).replace(",", "")
        shoe_country = input("Please enter the country of origin for the product: ").replace(",", "")
        shoe_code = duplicate_checker("code", inventory).upper().replace(",", "")
        while True:
            try:
                shoe_cost = int(input("Please enter the cost of the product: R").replace(",", ""))
                shoe_quantity = int(input("Please enter the current stock count for the product: ").replace(",", ""))
                break
            except ValueError:
                print("\nPlease enter the values for cost/quantity in whole numbers.\n")
        print(f"""\n\nPlease confirm the details entered for the product:\n
        Product Name: {shoe_product}
        Production Country: {shoe_country}
        Product Code: {shoe_code}
        Product Cost: {shoe_cost}
        Current Stock: {shoe_quantity}""")
        while True:
            user_confirm = input("\nIs the above information correct? (yes/no/cancel): ")
            if user_confirm.lower() == "y" or user_confirm.lower() == "yes":
                new_product = [shoe_country, shoe_code, shoe_product, str(shoe_cost), str(shoe_quantity)]
                print("Thank you for confirming, this product has been added to the inventory.")
                user_confirm = True
                with open("inventory.txt", "a") as file:
                    file.write(",".join(new_product))
                break
            elif user_confirm.lower() == "n" or user_confirm.lower() == "no":
                print("Please re-enter the details.\n")
                user_confirm = False
                break
            elif user_confirm.lower() == "c" or user_confirm.lower() == "cancel":
                print("")
                return
            else:
                print("Please choose a valid response.\n")
    return


def duplicate_checker(attribute, inventory):
    if attribute == "name":
        shoe_name = ""
        name_exists = True
        while name_exists:
            shoe_name = input("Please enter the product name: ")
            for item in inventory:
                if item.get_name() == shoe_name:
                    print("\nThis name is already in use, please choose a new product name.\n")
                    name_exists = True
                    break
                else:
                    name_exists = False
        return shoe_name
    elif attribute == "code":
        shoe_code = ""
        code_exists = True
        while code_exists:
            shoe_code = input("Please enter the product code: ")
            for item in inventory:
                if item.get_code() == shoe_code:
                    print("\nThis code is already in use, please choose a new code.\n")
                    code_exists = True
                    break
                else:
                    code_exists = False
        return shoe_code


def view_all(inventory):
    """Takes list of product objects and converts them to strings/prints them"""
    shoes_list = []
    for item in inventory:
        shoes_list.append(item.__str__())
    print(tabulate(shoes_list, headers=["Country", "Code", "Product", "Cost", "Quantity"]))
    return


def re_stock(inventory):
    """Reads current objects list, sorts it by quantity attribute and
    restocks product with the lowest stock count"""
    while True:
        stock_list = []
        for item in inventory:
            stock_list.append(item.__str__())
        for item in stock_list:
            item[4] = int(item[4])
        stock_list_sorted = sorted(stock_list, key=itemgetter(4))
        lowest_stock = stock_list_sorted[0]
        user_input = input(f"""The product with the lowest stock count is:\n
Product: {lowest_stock[2]}
Current Stock: {lowest_stock[4]}\n
Would you like to restock this product? (y/n): """)
        if user_input.lower() == "y" or user_input.lower() == "yes":
            while True:
                try:
                    restock_amount = int(input("How much stock would you like to add?: "))
                    break
                except ValueError:
                    print("Invalid amount entered, please enter a whole number.\n")
            for item in stock_list:
                if item[2] == lowest_stock[2]:
                    item[4] = (str(restock_amount + item[4]))
                item[4] = str(item[4])
            with open("inventory.txt", "w") as file:
                file.write("Country,Code,Product,Cost,Quantity\n")
                for item in stock_list:
                    file.write(",".join(item) + "\n")
            print(f"Stock quantity for {lowest_stock[2]} updated.\n")
            return
        elif user_input.lower() == "n" or user_input.lower() == "no":
            return
        else:
            print("Please choose a valid option.\n")


def search_shoes(inventory_list, code):
    chosen_item = ""
    item_found = False
    for item in inventory_list:
        item_string = item.__str__()
        if item_string[1] == code:
            chosen_item = item_string
            item_found = True
        else:
            continue
    if item_found:
        print(f"""\n=============PRODUCT DETAILS==============
Code                -      {chosen_item[1]}
Name                -      {chosen_item[2]}
Production Country  -      {chosen_item[0]}
Value               -      {chosen_item[3]}
Current Stock       -      {chosen_item[4]}\n""" + "=" * 42 + "\n")
    else:
        print("Item not found for given code. Have you updated the inventory list?\n")


def value_per_item(inventory):
    value_list = []
    total_value = 0
    for item in inventory:
        item_name = item.get_name()
        cost = item.get_cost()
        quantity = item.get_quantity()
        total = cost * quantity
        value_list.append([item_name, quantity, cost, total])
        total_value += total
    print(" " * 19 + f"Total Stock Value: R{total_value}")
    print(tabulate(value_list, headers=["Product", "Current Stock", "Item Cost", "Total Value"]))
    return


def highest_qty(inventory):
    stock_list = []
    for item in inventory:
        stock_list.append(item.__str__())
    for item in stock_list:
        item[4] = int(item[4])
    stock_list_sorted = sorted(stock_list, key=itemgetter(4), reverse=True)
    highest_stock = stock_list_sorted[0]
    print(f"The {highest_stock[2]} has the highest stock count and is eligible for store discount.")


# === Lists ===
shoes_objects = read_shoes_data()

# === Main Program ====
print("#" * 25 + "\n" + "#   Inventory Checker   #\n" + "#" * 25 + "\n")
while True:
    menu_choice = input("""Please select a menu option:
u  - Update Inventory List
a  - Add New Product
v  - View Current Stock
r  - Restock
s  - Search Product
cv - Current Stock Value
h  - Highest Stock
e  - Exit Program
    
Option: """).lower()
    if menu_choice == "u":
        shoes_objects = read_shoes_data()
        print("Inventory List Updated")
        print("")
    elif menu_choice == "a":
        print("\n==========ADD NEW PRODUCT==========")
        capture_shoes(shoes_objects)
        print("=" * 63 + "\n")
    elif menu_choice == "v":
        print("\n" + "=" * 23 + "CURRENT INVENTORY" + "=" * 23)
        view_all(shoes_objects)
        print("=" * 63 + "\n")
    elif menu_choice == "r":
        re_stock(shoes_objects)
    elif menu_choice == "s":
        search_shoes(shoes_objects, input("\nPlease enter the code for the product you wish to search: ").upper())
    elif menu_choice == "cv":
        print("\n" + "=" * 27 + "STOCK VALUE" + "=" * 27)
        value_per_item(shoes_objects)
        print("=" * 65 + "\n")
    elif menu_choice == "h":
        print("")
        highest_qty(shoes_objects)
        print("")
    elif menu_choice == "e":
        print("Goodbye for now!")
        exit()
    else:
        print("\nPlease choose a valid menu option.\n")
