# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 19:27:31 2020

@author: Souhardya
"""

#Importing the other modules
import Sales as sal
import Inventory as inv
import numpy as np
import warnings
warnings.filterwarnings("ignore")


#Creates inventory instance for dataframe in inventory module
def create_inventory():
    print('Enter the product number:: ')
    prod_num = int(input())
    print('Enter the product name:: ')
    prod_name = input()
    print('Enter the product type [Grocery/Dairy/Cosmetics] ::')
    prod_type = input()
    print('Enter the product price ::')
    price = float(input())
    print('Enter the number of products ::')
    quantity = int(input())
    inv.add_product(prod_num = prod_num, prod_name = prod_name, prod_type = prod_type, price = price,quantity = quantity)

#Creates sales record for dataframe in sales module    
def create_sales():
    print('Enter the date :: ')
    date = input()
    print('Enter the product number :: ')
    prod_num = int(input())
    print('Enter the product name :: ')
    prod_name = input()
    print('Enter the product type [Grocery/Dairy/Cosmetics] ::')
    prod_type = input()
    print('Enter the product price ::')
    price = float(input())
    print('Enter the number of products ::')
    quantity = int(input())
    sal.add_product(date = date, prod_num = prod_num, prod_name = prod_name, prod_type = prod_type, price = price,quantity = quantity)

#Modifying inventory product fields
def modify_inventory(prod_num):
    inv.modify_prod(prod_num)

#Modifying sales record fields    
def modify_sales(prod_num):
    sal.modify_product(prod_num)

#Deleting a particular inventory product    
def delete_inv(prod_num):
    inv.del_prod(prod_num)

#Deleting sales record    
def delete_sales(prod_num):
    sal.del_prod

#Displays inventory table as a whole    
def display_inv_db():
    print(inv.database)

#Displays sales table as a whole    
def display_sales_db():
    print(sal.database)
    
#Displays a particular inventory product fields
def display_inv_prod(prod_num):
    inv.display(prod_num)

#Displays a particular sales record fields    
def display_sale_record(prod_num):
    sal.display(prod_num)
    


#Declaring flag variable and user type respectively
flag = 1
user = ''

#Menu based application iterating infinitely unless exitting is inititated by user
while flag == 1:
    print("Welcome!!!")
    print("Please enter A if you are administrator and an S if you are a Salesperson")
    user = input()
    if user != 'A' and user!= 'S':
        print("Invalid user input!! \n Try again!!")
        continue
    print('Please select an option from the following :: \n\n')
    print('------------------------------------------------')
    print('|(1) Adding a product to the inventory         |')
    print('|(2) Adding a sale to the records              |')
    print('|(3) Modifying an inventory product            |')
    print('|(4) Modifying a sale record                   |')
    print('|(5) Deleting inventory product                |')
    print('|(6) Deleting sales record                     |')
    print('|(7) Displaying inventory product              |')
    print('|(8) Displaying sales record                   |')
    print('|(9) Displaying inventory database             |')
    print('|(10) Displaying sales database                |')
    print('------------------------------------------------')
    print('Please input the option number                 ')
    choice = int(input())
    if choice > 10 or choice <1:
        print('Invalid choice!!\nTry Again!')
        continue
    
    if choice == 1:
        if user == 'A':
            create_inventory()
        else:
            print('Access Denied!!')
            continue;
    elif choice == 2:
        create_sales()#both
    elif choice == 3:
        if user == 'A':
            print("Please enter the product number :: ")
            prod_num = int(input())
            modify_inventory(prod_num)
        else: 
            print('Access Denied!!')
    elif choice == 4:
        print("Please enter the product number :: ")
        prod_num = int(input())   
        modify_sales(prod_num)
    elif choice == 5:
        if user == 'A':
            print("Please enter the product number :: ")
            prod_num = int(input())        
            delete_inv(prod_num) 
        else:
            print("Access Denied!!")
    elif choice == 6:
        if user == 'A':
            print("Please enter the product number :: ")
            prod_num = int(input())         
            delete_sales(prod_num)
        else:
            print("Access Denied!!")
    elif choice == 7:
        if user == 'A':
            print("Please enter the product number :: ")
            prod_num = int(input())        
            display_inv_prod(prod_num)
        else:
            print("Access Denied!!")
    elif choice == 8:
        print("Please enter the product number :: ")
        prod_num = int(input())
        display_sale_record(prod_num)
    elif choice == 9:
        if user == 'A':
            display_inv_db()
        else:
            print("Access Denied!!")
    elif choice == 10:
        if user == 'A':
            display_sales_db()
        else:
            print("Access Denied!!")
    print('Do you want to exit the application ??(Yes/No)')
    exit_choice = input()
    if exit_choice == 'Yes':
        break
        

#Calculating the total price in inventory and sales record database
total_price_inv = inv.database.total_cost.sum()
total_price_sales = sal.database.total_cost.sum()

print("PRINTING REPORT!!")
print("Total price in Inventory :: ", total_price_inv)
print("\nTotal price in Sales :: ", total_price_sales)

"""
The following code takes care of these considerations:--
->The sum of quantities of a particular product in the sales module is tallied with the Inventory module and report is generated on the current stock of products.
->The total cost in the sales module is tallied with sum of the prices of individual products sold."""
sum_c = 0
sum_q = 0
i = 0
for prod_num_inv in inv.database.prod_num:
    for prod_num_sal in sal.database.prod_num:
        if prod_num_inv == prod_num_sal:
            sum_c = sal.database['total_cost'][sal.database[sal.database['prod_num'] == prod_num_sal].index].sum()
            sum_q = sal.database['quantity'][sal.database[sal.database['prod_num'] == prod_num_sal].index].sum()
    print("The total quantity in sales for product number {prod_num} is = ".format(prod_num = prod_num_inv), sum_q)
    print("The total quantity in sales for product number {prod_num} is = ".format(prod_num = prod_num_inv), inv.database['quantity'][inv.database[inv.database['prod_num'] == prod_num_inv].index][i])
    if sum_q == inv.database['quantity'][inv.database[inv.database['prod_num'] == prod_num_inv].index][i]:
        print("Records tally for product number {prod_num} ".format(prod_num = prod_num_inv))
    else:
        print('Records do not tally for product number {prod_num}'.format(prod_num = prod_num_inv))
        
    print("The total cost in sales for product number {prod_num} is = ".format(prod_num = prod_num_inv), sum_c)
    print("The total cost in inventory for product number {prod_num} is = ".format(prod_num = prod_num_inv), inv.database['total_cost'][inv.database[inv.database['prod_num'] == prod_num_inv].index][i])
    if sum_c == inv.database['total_cost'][inv.database[inv.database['prod_num'] == prod_num_inv].index][i]:
        print("Records tally for product number {prod_num} ".format(prod_num = prod_num_inv))
    else:
        print('Records do not tally for product number {prod_num}'.format(prod_num = prod_num_inv))
    sum_c = 0
    sum_q = 0
    i+=1


 




