import sqlite3

# connect to the database
con = sqlite3.connect('databases/rockyconcrete.db')

# create a cursor/pointer to navigate the database
con.row_factory = sqlite3.Row #enables us to use column headings
cur = con.cursor() # the pointer to use in the database

# Parameter query
choice = input('Enter a choice of either: A. Customer Details, B. Order Details, C. Product Details, D. Quit: ').upper()
while choice != 'D':
    if choice == 'A':
        cust = input('Enter a Customer Name: ').lower()
        sql = """
            select *
            from customers
            where cust_name like ?;"""
        cur.execute(sql, ('%' + cust + '%',))
        results = cur.fetchall()

        if len(results) > 0:
            for row in results:
                print(row['cust_name'], 'lives in', row['street'], 'in', row['town'], 'Their credit limit is',
                      row['cr_limit'], 'and their Current Balance is', row['curr_bal'])
        else:
            print('No records found')
    elif choice == 'B':
        ordnum = (input('Enter an Order Number: '))
        sql = """
                select *
                from order_details
                where order_no like ?;"""
        cur.execute(sql, (ordnum,))
        results = cur.fetchall()

        if len(results) > 0:
            for row in results:
                print(row['order_no'], 'Product Code:', row['prod_code'], 'Order Quantity:', row['order_qty'], 'Order Price:', row['order_price'])
        else:
            print('No records found')
    elif choice == 'C':
        prodname = str(input('Enter a Product Code: ')).upper()
        sql = """
                select *
                from products
                where prod_code like ?;"""
        cur.execute(sql, ('%' + prodname + '%',))
        results = cur.fetchall()

        if len(results) > 0:
            for row in results:
                print(row['prod_code'], 'Description:', row['description'], 'Product Group:', row['prod_group'], 'List Price:', row['list_price'],
                      'Quantity on Hand:', row['qty_on_hand'], 'Remake Level:', row['remake_level'], 'Remake Quantity:', row['remake_qty'])
        else:
            print('No records found')
    elif choice != 'A' and choice != 'B' and choice != 'C' and choice != 'D':
        print('Invalid code entered. Try again')
    choice = input('Enter a choice of either: A. Customer Details, B. Order Details, C. Product Details, D. Quit: ').upper()
print('Goodbye')