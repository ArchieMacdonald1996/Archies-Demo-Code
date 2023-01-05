# Stock Manager - Archie Macdonald #

## Description ##
 This project is a stock management tool for a shoe retailer

## Contents: ##
1. Packages
2. Functions/Classes
3. Main Menu Options
4. Input Files

## 1) Packages ##

Packages required for this program are:

__tabulate__ from __tabulate__  
__itemgetter__ from __operator__

## 2) Functions/Classes ##

 Below you will find a list of classes/functions used in this project
 and descriptions of how they work. Also included are any
 dependencies between functions.

### Classes ###

 __Shoes__
 Class for items in the invnetory. The attributes stored
 are: country, code, product name, cost and quantity.
 This class has methods for returning the name, code, cost
 and quantity of a given object.
                       
### Functions ###

 __read_shoes_data__
 This function opens and reads the inventory.txt file
 then populates the "shoe_objects" list with each shoe
 product for use by other functions.
                     
 __capture_shoes__
 This function allows the user to add a new model of shoe
 to the inventory. There are checks in place to make sure
 that the name and code of the new shoe aren't duplicates
 and that the values entered for the cost and quantity are
 whole numbers. The user will be asked to confirm that the
 details entered are correct before they are written to the
 inventory.txt file. Takes the shoes_objects list as an input.
                       
 Dependencies - duplicate_checker
                       
 __duplicate_checker__
 Prompts users to enter either the name or code for a new
 shoe, then checks to see if that name/code is already in use.
 If this is the case, the user is asked to enter a suitable
 alternative. The relevant name/code is then returned to the
 capture_shoes function. Takes the relevant attribute and the
 shoes_objects list as inputs.
                       
 __view_all__
 Iterates through shoes_objects list and reads them as strings,
 then creates a list of those strings. This new list is tabulated
 and presented as a spreadsheet of all information currently saved
 to the inventory.txt file. Takes shoes_objects list as input.
                       
 Dependencies - tabulate
                       
 __re_stock__
 Checks current stock levels and returns the shoe model with
 the lowest current stock. The user is then asked if they want
 to add additional stock. If so, they can enter an integer to
 increase the current stock value of that item. Takes shoes_objects
 list as input.
                       
 Dependencies - itemgetter
                       
 __search_shoes__
 User can search for a particular item by entering the relevant
 product code. If the entered code is invalid, user is presented with
 a reminder to check that the cached inventory is updated. If the item
 is found successfully, the details of that item are printed to the
 console. Takes the shoes_objects list and the relevant code as inputs.
                       
 __value_per_item__
 Prints a spreadsheet of all items in the inventory along with their
 stock level, price and the total value of that stock. Takes the shoes_objects
 list as an input. 
                       
 Dependencies - tabulate
                       
 __highest_qty__
 Returns the item with the highest current stock and prints a message
 confirming that they are eligible for store discount. Takes shoes_objects
 list as input.
                       
 Dependencies - itemgetter


## 3) Main Menu ##

 The main menu offers four basic options to all users:

> u  - Update Inventory List  
> a  - Add New Product  
> v  - View Current Stock  
> r  - Restock  
> s  - Search Product  
> cv - Current Stock Value  
> h  - Highest Stock  
> e  - Exit Program  

 Entering an invalid choice will reprint the menu and ask the user to try
 again.
 
## 4) Input Files ##

 This reads and writes to one file: inventory.txt
 
 The file must be stored in the same location as the program code file. The
 format of the code must be as follows:
 
> Country,Code,Product,Cost,Quantity  
> South Africa,SKU44386,Air Max 90,2300,20  
> China,SKU90000,Jordan 1,3200,50  
> ...

The reading of the file is very sensitive to formatting, so if any issues
present themselves with the reading of the file, check that the format is
correct then try again.

