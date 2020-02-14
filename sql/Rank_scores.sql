# Write your MySQL query statement below
select Scores.Score, 
(select count(distinct a.Score) from Scores a where Scores.Score <= a.Score) as Rank
from Scores
order by Scores.Score desc