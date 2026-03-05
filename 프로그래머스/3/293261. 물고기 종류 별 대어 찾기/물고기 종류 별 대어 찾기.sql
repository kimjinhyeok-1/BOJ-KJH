-- 코드를 작성해주세요
select c.id, b.fish_name, t.k as length
from (select fish_type, max(length) as k
     from fish_info
     where length is not null
     group by fish_type) t 
     join fish_name_info b
on t.fish_type = b.fish_type 
join fish_info c on t.k = c.length and t.fish_type = c.fish_type