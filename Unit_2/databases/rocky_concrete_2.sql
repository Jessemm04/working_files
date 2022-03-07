-- Join Queries

select od.prod_code, description, order_price, order_qty, order_no
from order_details od, products p
where od.prod_code = p.prod_code
and order_no = 1234;

--JQ2
select cust_name, street, town, post_code, order_date
from customers c, orders o
where c.cust_no = o.cust_no
and order_date like '1706%'
order by order_date asc;


-- this is the way mr stansfeild joins tables
select od.prod_code, description, order_price, order_qty, order_no
from order_details od, products p
where od.prod_code = p.prod_code
and order_no = 1234;

-- this is the standard way to join tables, but its harder and longer
select prod_code, description, order_price, order_qty
from order_details od
inner join products p
on od.prod_code = p.prod_code
and order_no = 1234;

--JQ3
select order_no, order_price, prod_code, list_price
from order_details od, products p
where od.prod_code = p.prod_code
and order_price != list_price;
-- you cal also type <> instead of !=

--JQ4
select cust_name, order_date, order_qty * order_price as 'total_price'
from customers c, orders o, order_details od
where c.cust_no = o.cust_no
and o.order_no = od.order_no
and order_qty * order_price > 500
order by order_date asc, Total_Price desc;
-- 3 means column 3, which is 'order_qty * order_price as "total_price"' in the select line

-- JQ5
select p.description, c.cust_name
from customers c, products p, orders o, order_details od
where p.prod_code = od.prod_code
and od.order_no = o.order_no
and o.cust_no = c.cust_no
and c.town = 'Brisbane';

--JQ6
select cust_name, curr_bal, cr_limit, order_date, order_qty * order_price as 'total_price'
from customers c, orders o, order_details od
where c.cust_no = o.cust_no
and o.order_no = od.order_no
and c.curr_bal > cr_limit;

--JQ7
select c.cust_name, prod_code, order_date
from customers c, order_details od, orders o
where c.cust_no = o.cust_no
and o.order_no = od.order_no
and od.prod_code = 'GNOME'
and o.orer_date between 170401 and 170430