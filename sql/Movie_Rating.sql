# Write your MySQL query statement below
(select u.name as results
from Movie_Rating m, Users u
where m.user_id = u.user_id
group by u.user_id
order by count(m.movie_id) desc, u.name
limit 1)
union
(select m.title as results
from Movie_Rating r, Movies m 
where m.movie_id = r.movie_id and date_format(r.created_at, '%Y-%m') = '2020-02'
group by m.movie_id
order by avg(r.rating) desc, m.title
limit 1)

