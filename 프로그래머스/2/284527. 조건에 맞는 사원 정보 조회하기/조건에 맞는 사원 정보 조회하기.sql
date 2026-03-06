with t as(
select emp_no, sum(score) as ss
from hr_grade
where year = '2022'
group by emp_no
order by ss desc
limit 1)

select t.ss as score,
t.emp_no,
e.emp_name,
e.position,
e.email
from hr_employees e join t using (emp_no)
