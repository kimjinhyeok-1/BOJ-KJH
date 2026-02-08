-- 코드를 입력하세요
SELECT
  CAR_ID,
  case 
  when 
  sum(CASE
    WHEN '2022-10-16' BETWEEN START_DATE AND END_DATE
    THEN 1
    ELSE 0
    end) between 0 and 0 
    then '대여 가능'
    else '대여중'
  END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc
