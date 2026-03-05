-- 코드를 작성해주세요
with recursive t as (
    select id, parent_id, 1 as gen
    from ecoli_data
    where parent_id is null
    
    union all
    
    select e.id, e.parent_id, t.gen + 1 as gen
    from t join ecoli_data e
    on t.id = e.parent_id
)
select count(*) as count, gen as generation
from t left join ecoli_data e
on t.id = e.parent_id
where e.id is null
group by gen