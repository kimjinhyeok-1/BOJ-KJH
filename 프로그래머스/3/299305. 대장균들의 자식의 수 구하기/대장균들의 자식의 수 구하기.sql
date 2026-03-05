-- 코드를 작성해주세요
select p.id, count(e.id) as child_count
from ecoli_data p left outer join ecoli_data e
on p.id = e.parent_id
group by p.id