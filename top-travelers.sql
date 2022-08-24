# Write your MySQL query statement below
select name, sum(if (isnull(distance), 0, distance)) as travelled_distance
from Users u left join Rides r
on u.id = r.user_id
group by u.id
order by travelled_distance desc, name asc;