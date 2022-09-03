# Write your MySQL query statement below
select user_id as buyer_id, join_date, coalesce(od.orders_in_2019,0) as orders_in_2019
from Users u left join 

(select buyer_id, count(Order_id) as orders_in_2019
from Orders where order_date like '%2019%' group by buyer_id) od 
on od.buyer_id = u.user_id