import sqlite3

# connect to the database
con = sqlite3.connect('databases/rockyconcrete.db')

# create a cursor/pointer to navigate the database
con.row_factory = sqlite3.Row #enables us to use column headings
cur = con.cursor() # the pointer to use in the database

# Parameter query
cust = input('Enter a customers name: ')

sql = """
    select cust_name, cust_no, (cr_limit - curr_bal) as 'Credit'
    from customers
    where cust_name like ?;
"""

cur.execute(sql,('%' + cust + '%',))
# comma needed make it iterable when 1 variable. Order matters
results = cur.fetchall()

for row in results:

    sql = """
        select max(order_no), max(order_date)
        from orders
        where cust_no = ?;
"""
    cur.execute(sql, (row['cust_no'],))
    # comma needed make it iterable when 1 variable. Order matters
    results = cur.fetchone()

if len(results) > 0:
    for row in results:
        print(row['cust_name'], 'Customer number: ', row['cust_no'], 'Credit: ', row['Credit'])
        print('Recent Order   Number: ', row['order_no'], 'Recent Order Date', ['order_date'])
else:
    print('No records found')