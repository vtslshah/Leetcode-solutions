select
    dept.name as Department,
    em1.name as Employee,
    em1.salary as Salary
from employee as em1
Join department as dept on em1.departmentId = dept.id
where em1.salary = (select distinct max(salary) from employee as em2 where em2.departmentId = em1.departmentId) group by em1.id