-- 코드를 입력하세요
SELECT b.author_id, a.author_name, category,
sum(sales * price) as total_sales


from book b join author a on b.author_id = a.author_id
join book_sales s on b.book_id = s.book_id
where sales_date >= '2022-01-01' and sales_date < '2022-02-01'
group by b.author_id, a.author_name, category
order by author_id, category desc