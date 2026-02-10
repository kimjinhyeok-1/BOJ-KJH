-- 코드를 입력하세요
SELECT year(s.sales_date) as year, month(s.sales_date)as month, i.gender, count(distinct i.user_id)
from user_info i join online_sale s
on i.user_id = s.user_id 
where i.gender is not null
group by year(s.sales_date), month(s.sales_date), gender
order by year, month, gender