with employee_reiews as (
    select review_id,employee_id,review_date,rating,
        row_number() over (partition by employee_id order by review_date desc) as row_num,
        (lag(rating) over (partition by employee_id order by review_date desc) - rating) as delta
    from performance_reviews
)

select 
    emp.employee_id,
    emp.name,
    sum(delta) as improvement_score  
from employee_reiews as er
join employees as emp on er.employee_id = emp.employee_id
where row_num > 1 and row_num <= 3
group by emp.employee_id
having count(review_id) = 2 and min(delta) > 0
order by improvement_score desc,emp.name