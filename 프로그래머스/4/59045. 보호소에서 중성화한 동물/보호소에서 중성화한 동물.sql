-- 코드를 입력하세요
SELECT i.animal_id, o.animal_type, o.name
from animal_ins i inner join animal_outs o using(animal_id)
where i.sex_upon_intake like 'intact%' 
and (o.sex_upon_outcome like ('spayed%') 
or o.sex_upon_outcome like('neutered%'))
order by i.animal_id