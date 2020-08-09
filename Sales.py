
#Importing the libraries
import pandas as pd

#Storing column tables in a list
column_names = ['Date', 'prod_num', 'prod_name',  'quantity', 'price', 'total_cost']
#Creating a dataframe with these columns
database = pd.DataFrame(columns = column_names)


#Adding a sale to the record 
def add_product(date, prod_num, prod_name, prod_type, price, quantity):
        total_cost = price*quantity
        dict ={'Date': date,
               'prod_num': prod_num,
               'prod_name': prod_name,
               'prod_type': prod_type,
               'price': price,
               'quantity': quantity,
               'total_cost': total_cost}
        global database
        database = database.append(dict, ignore_index=True)
        print("Product added!!")
 
#Deleting a sale from the record      
def del_prod(prod_num):
    global database
    database = database[database.prod_num != prod_num]
    print('Deleted!!')

#Modifying a sale from the record and displaying the new entry    
def modify_prod(prod_num):
    global database
    print("Enter the date ::")
    database['Date'][database[database['prod_num'] == prod_num].index] = input()
    print("Enter the product name ::")
    database['prod_name'][database[database['prod_num'] == prod_num].index] = input()
    print("Enter the product type ::")
    database['prod_type'][database[database['prod_num'] == prod_num].index] = input()
    print("Enter the price ::")
    database['price'][database[database['prod_num'] == prod_num].index] = float(input())
    print("Enter the quantity ::")
    database['quantity'][database[database['prod_num'] == prod_num].index] = int(input())
    database['total_cost'][database[database['prod_num'] == prod_num].index] = database['price'][database[database['prod_num'] == prod_num].index] * database['quantity'][database[database['prod_num'] == prod_num].index]
    print('The new entry is :--\n\n')
    display(prod_num)

#Display the fields of a particular sale   
def display(prod_num):
    global database
    print('The date name is :: ',  database['Date'][database[database['prod_num'] == prod_num].index].values[0])
    print('The product name is :: ',  database['prod_name'][database[database['prod_num'] == prod_num].index].values[0])
    print("The product type is ::" , database['prod_type'][database[database['prod_num'] == prod_num].index].values[0])
    print('The price of the product is ::', database['price'][database[database['prod_num'] == prod_num].index].values[0] )
    print('The quantity of the product is ::', database['quantity'][database[database['prod_num'] == prod_num].index].values[0] )
    print('The total cost of the product is ::', database['total_cost'][database[database['prod_num'] == prod_num].index].values[0] )
    
    
#Test

"""add_product(date = '1/1/1', prod_num = 1, prod_name = 'apple', prod_type = 'fruit', price = 1,quantity = 50)
add_product(date = '1/1/1', prod_num = 2, prod_name = 'banana', prod_type = 'fruit', price = 2,quantity = 50)
modify_prod(1)
display(2)"""