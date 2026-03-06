with fe as (
    select sum(code) as code_sum
    from skillcodes
    where category = 'Front End'
),
p as (
    select sum(code) as py_code
    from skillcodes
    where name = 'Python'
),
c as (
    select sum(code) as cs_code
    from skillcodes
    where name = 'C#'
)

SELECT grade, id, email
FROM (
    SELECT
        d.id,
        d.email,
        CASE
    WHEN (d.skill_code & fe.code_sum) > 0
     AND (d.skill_code & p.py_code) > 0 THEN 'A'
    WHEN (d.skill_code & c.cs_code) > 0 THEN 'B'
    WHEN (d.skill_code & fe.code_sum) > 0 THEN 'C'
END AS grade
    FROM developers d
    CROSS JOIN fe
    CROSS JOIN p
    CROSS JOIN c
) x
WHERE grade IS NOT NULL
ORDER BY grade ASC, id ASC;