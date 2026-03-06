-- 코드를 작성해주세요
with t as(
    select sum(code) as tc
    from skillcodes
    where category = 'Front End'
)

select id, email, first_name, last_name
from developers
where skill_code & (select tc from t) > 0 
order by id asc