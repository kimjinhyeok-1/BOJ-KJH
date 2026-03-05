-- 코드를 작성해주세요
select distinct d.id, d.email, d.first_name, d.last_name
from skillcodes s join developers d
on (s.code & d.skill_code) > 0
where s.name in ("C#", "Python")
order by d.id asc