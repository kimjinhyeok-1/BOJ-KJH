with x as(
    select review_id, count(*) as c
    from rest_review
    group by member_id
)
select m.member_name, r.review_text, date_format(r.review_date,'%Y-%m-%d') as review_date
from member_profile m inner join rest_review r using (member_id)
where m.member_id in
(select member_id
from rest_review
group by member_id
having count(*) = (
    select max(c)
    from x
))
order by review_date asc, review_text asc