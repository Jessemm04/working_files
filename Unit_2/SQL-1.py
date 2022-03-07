import sqlite3

# connect to the database
con = sqlite3.connect('databases/rockyconcrete.db')

# create a cursor/pointer to navigate the database
con.row_factory = sqlite3.Row #enables us to use column headings
cur = con.cursor() # the pointer to use in the database

# sql = """
#         select *
#         from customers
#         where town = 'Brisbane';"""
# #triple quote to put single quote elements inside of big string
#
# cur.execute(sql)
# results = cur.fetchall()
#
# print(type(results))
# print(len(results))
# print(results) #answer is row objects because row.factory was used before

#parameter query
town = input('Enter the the town to search for: ')
credit = int(input('Enter a minimum credit limit to search for: '))

sql = """
    select *
    from customers
    where town like ?
    and cr_limit >= ?;""" #? is a placeholder

cur.execute(sql,('%' + town + '%', credit)) #comma needed make it iterable when 1 variable. Order matters
results = cur.fetchall()


if len(results) > 0:
    for row in results:
        print(row['cust_name'], 'lives in', row['street'], 'in',row['town'], 'and their credit limit is', row['cr_limit'])
else:
    print('No records found')
