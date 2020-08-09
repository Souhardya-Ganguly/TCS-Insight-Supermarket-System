
#Importing libraries
import pandas as pd

#Storing column tables in a list
column_names = ['prod_num', 'prod_name', 'prod_type', 'price', 'quantity']
#Creating a dataframe with these columns
database = pd.DataFrame(columns = column_names)
      
    
#Adding a product to the inventory list    
def add_product(prod_num, prod_name, prod_type, price, quantity):
    c = True
    total_cost = price*quantity    
    dict ={'prod_num': prod_num,
           'prod_name': prod_name,
           'prod_type': prod_type,
           'price': price,
           'quantity': quantity,
           'total_cost': total_cost}
    global database
    c = dict['prod_num'] in database.prod_num
    if c==False:
            database = database.append(dict, ignore_index=True)
            print("Product added!!")
    else:
            print("Product number already exists!! Try Again!")  

#Deleting a product from the inventory list
def del_prod(prod_num):
    global database
    database = database[database.prod_num != prod_num]
    print('Product Deleted!!')

#Modifying a product from the inventory list and displaying the new entry
def modify_prod(prod_num):
    global database
    print("Enter the product name ::")
    database['prod_name'][database[database['prod_num'] == prod_num].index] = input()
    print("Enter the product type ::")
    database['prod_type'][database[database['prod_num'] == prod_num].index] = input()
    print("Enter the price ::")
    database['price'][database[database['prod_num'] == prod_num].index] = float(input())
    print("Enter the quantity ::\n\n")
    database['quantity'][database[database['prod_num'] == prod_num].index] = int(input())
    print('The new entry is :--')
    display(prod_num)
    
#Display the fields of a particular product
def display(prod_num):
    global database
    print('The product name is :: ',  database['prod_name'][database[database['prod_num'] == prod_num].index].values[0])
    print("The product type is ::" , database['prod_type'][database[database['prod_num'] == prod_num].index].values[0])
    print('The price of the product is ::', database['price'][database[database['prod_num'] == prod_num].index].values[0] )
    print('The quantity of the product is ::', database['quantity'][database[database['prod_num'] == prod_num].index].values[0] )
    print('The total cost of the product is ::', database['total_cost'][database[database['prod_num'] == prod_num].index].values[0])


#Test

"""add_product(prod_num = 1, prod_name = 'apple', prod_type = 'fruit', price = 1,quantity = 50)
add_product(prod_num = 2, prod_name = 'apple', prod_type = 'fruit', price = 1,quantity = 50)
modify_prod(1)
display(2)"""