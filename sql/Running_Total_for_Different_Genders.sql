# Write your MySQL query statement below
select s1.gender as gender, s1.day as day, sum(s2.score_points) as total
from Scores s1, Scores s2
where datediff(s1.day, s2.day) >= 0 and s1.gender = s2.gender
group by s1.gender, s1.day
order by s1.gender, s1.day
