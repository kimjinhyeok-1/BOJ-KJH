-- 코드를 작성해주세요
with recursive t as (
    select id, parent_id, 1 as gen
    from ecoli_data
    where parent_id is null
    
    union all
    
    select e.id, e.parent_id, t.gen + 1 as gen
    from ecoli_data e join t
    on t.id = e.parent_id
)
select id
from t
where gen = 3