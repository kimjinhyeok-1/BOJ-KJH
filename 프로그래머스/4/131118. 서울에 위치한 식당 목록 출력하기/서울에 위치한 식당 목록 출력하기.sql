-- 코드를 입력하세요
SELECT 
r.rest_id, 
i.rest_name, 
i.food_type, 
i.favorites,
i.address, 
round(sum(r.review_score)/count(r.review_score), 2) as score
from rest_info i, rest_review r
where i.rest_id = r.rest_id
and address like '서울%'
group by r.rest_id
order by score desc