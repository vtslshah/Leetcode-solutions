select sales_date, revenue, 
    sum(lag(revenue) over (order by sales_date asc)) as cumulative_revenue
from DailySales order by sales_date;