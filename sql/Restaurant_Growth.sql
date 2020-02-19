# Write your MySQL query statement below
select t.visited_on, sum(amount) as amount, round(sum(amount)/7.0, 2) as average_amount
from (select distinct visited_on from Customer limit 6, 100000) t, Customer c 
where datediff(t.visited_on, c.visited_on) <= 6 and datediff(t.visited_on, c.visited_on) >= 0
group by t.visited_on