# Write your MySQL query statement below
select activity_date as day ,count(distinct user_id) as active_users 
from activity 
group by activity_date 
having (activity_date > "2019-06-27" AND activity_date <= "2019-07-27") ;