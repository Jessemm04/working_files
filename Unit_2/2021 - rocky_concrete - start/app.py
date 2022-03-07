from flask import Flask, render_template, url_for, request, redirect
import sqlite3
import os

app = Flask(__name__)

#connect to the database
con = sqlite3.connect("rockyconcrete.db", check_same_thread=False)
con.row_factory = sqlite3.Row

#create a cursor/pointer to navigate the database
cur = con.cursor()

@app.route('/')
@app.route('/index')
def index():
    sql = """
        select *
        from customers
        order by cust_name asc;"""
    cur.execute(sql)
    results = cur.fetchall()

    return render_template("index.html", customers=results, title='Customer List')

@app.route('/customer_details', methods=['GET'])
def customer_details():
    if request.args.get('cid'):
        id = int(request.args.get('cid'))

        sql = """
        select *
        from customers
        where cust_no = ?;
        """
        cur.execute(sql, (id,))
        customer_results = cur.fetchone()

        sql = """
        select count(distinct o.order_no) as 'Order Count', max(order_date) as 'Last Order', 
        sum(order_qty * order_price) as 'Total Orders'
        from orders o, order_details od
        where o.order_no = od.order_no
        and cust_no = ?;
        """

        cur.execute(sql, (id,))
        order_count = cur.fetchone()

        sql = """
        select *
        from orders
        where cust_no = ?;
        """

        cur.execute(sql, (id,))
        order_history = cur.fetchall()

        return render_template('customer_details.html', title='Customer Details',
                               cdetails=customer_results, ocount=order_count, ohist=order_history)

    else:
        return redirect(url_for('index'))

@app.route('/order_details', methods=['GET'])
def order_details():
    if request.args.get('oid'):
        id = request.args.get('oid')

        sql = """
        select od.order_no, order_qty, order_price, description, o.order_date, p.prod_code, order_qty*order_price as 'Total Price'
        from order_details od, products p, orders o
        where p.prod_code = od.prod_code
        and o.order_no = od.order_no
        and o.order_no = ?;
        """

        cur.execute(sql, (id,))
        order_details = cur.fetchall()

        sql = """
        select sum(order_qty*order_price) as 'Order Total'
        from order_details
        where order_no = ?;
        """

        cur.execute(sql, (id,))
        order_total = cur.fetchone()

        return render_template('order_details.html', title='Order Details', id=id, odetails=order_details, ototal=order_total)

    else:
        return redirect(url_for('customer_details'))


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host,port,debug=True)

    # order histroy: order numbers, and order dates for that customer