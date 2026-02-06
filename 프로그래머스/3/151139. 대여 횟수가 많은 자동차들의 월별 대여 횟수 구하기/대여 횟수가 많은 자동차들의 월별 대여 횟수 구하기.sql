-- 코드를 입력하세요
SELECT month(start_date) as MONTH, CAR_ID, count(*) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_id in (
    select car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where START_DATE >= '2022-08-01' and START_DATE < '2022-11-01'
    group by car_id
    having count(*) >= 5
) 
and START_DATE >= '2022-08-01' and START_DATE < '2022-11-01' 
group by month(start_date), car_id
order by month, car_id desc