SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d') as PUBLISHED_DATE
from BOOK 
where published_date >= '2021-01-01' and published_date < '2022-01-01'
and CATEGORY ='인문'
order by PUBLISHED_DATE