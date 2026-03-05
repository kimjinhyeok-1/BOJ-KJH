-- 코드를 작성해주세요
select id,
    case k
    when 1 then 'CRITICAL'
    when 2 then 'HIGH'
    when 3 then 'MEDIUM'
    WHEN 4 THEN 'LOW'
    END AS COLONY_NAME
from (select id, 
     ntile(4) over (order by size_of_colony desc) as k
     from ecoli_data) t
ORDER BY ID ASC