-- 코드를 작성해주세요
with t as(
    select max(size_of_colony) as soc, year(DIFFERENTIATION_DATE) as yr
    from ecoli_data
    group by year(DIFFERENTIATION_DATE)
)
select t.yr as YEAR, (t.soc - e.size_of_colony) as YEAR_DEV, e.ID
from t join ecoli_data e
on t.yr = year(e.DIFFERENTIATION_DATE)
order by year asc, YEAR_DEV asc