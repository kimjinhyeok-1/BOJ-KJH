-- 코드를 작성해주세요
select e.id, e.genotype, p.genotype as parent_genotype
from ecoli_data p join ecoli_data e
on p.id = e.parent_id
where (p.genotype & e.genotype) = p.genotype