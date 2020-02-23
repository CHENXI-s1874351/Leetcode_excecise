# Write your MySQL query statement below
select f1.activity
from friends f1
group by f1.activity
having count(f1.id) between
(select count(f.id)+1
from friends f
group by f.activity
order by count(f.id)
limit 1)
and 
(select count(f.id)-1
from friends f
group by f.activity
order by count(f.id) desc
limit 1)
